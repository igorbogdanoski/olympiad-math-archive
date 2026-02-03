# -*- coding: utf-8 -*-
"""
Worksheet Router - PDF Generation API
Created: February 3, 2026
Purpose: Generate PDF worksheets from selected problems
Updated: February 3, 2026 - Migrated from ReportLab to WeasyPrint for native Cyrillic support
"""
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import Response, JSONResponse
from pydantic import BaseModel
from typing import List, Optional
from io import BytesIO
from datetime import datetime
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import json
import sys

# Add parent directory to path for config imports
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config.worksheet_templates import TEMPLATES, get_template, calculate_problem_counts

router = APIRouter()

# Initialize Jinja2 environment for HTML templates
template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
env = Environment(
    loader=FileSystemLoader(template_dir),
    autoescape=select_autoescape(['html', 'xml'])
)


class Problem(BaseModel):
    """Problem model for worksheet generation"""
    id: str
    problem_id: Optional[str] = None
    content: str
    solution: Optional[str] = None
    difficulty: Optional[int] = None
    grade: Optional[int] = None
    topic: Optional[str] = None


class WorksheetRequest(BaseModel):
    """Request model for worksheet generation"""
    title: str
    description: Optional[str] = None
    problems: List[Problem]
    include_solutions: bool = True
    school_name: Optional[str] = None
    teacher_name: Optional[str] = None
    grade: Optional[int] = None
    labels: Optional[dict] = None  # Macedonian labels from frontend (Approach 3)
    template_id: Optional[str] = None  # Template identifier (e.g., "standard_test")
    export_options: Optional[dict] = None  # Export options (answer key, QR code, etc.)


def clean_text_for_html(text: str) -> str:
    """Clean text for HTML rendering - remove LaTeX delimiters, convert to Unicode"""
    if not text:
        return ""
    
    # Ensure text is string (not bytes)
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    
    # Remove LaTeX math delimiters
    text = text.replace('\\(', '').replace('\\)', '')
    text = text.replace('\\[', '<br>').replace('\\]', '<br>')
    text = text.replace('$$', '<br>')
    text = text.replace('$', '')
    
    # Replace common LaTeX symbols with Unicode equivalents
    text = text.replace('\\pi', 'π')
    text = text.replace('\\alpha', 'α')
    text = text.replace('\\beta', 'β')
    text = text.replace('\\theta', 'θ')
    text = text.replace('\\sum', '∑')
    text = text.replace('\\sqrt', '√')
    text = text.replace('\\infty', '∞')
    text = text.replace('\\leq', '≤')
    text = text.replace('\\geq', '≥')
    text = text.replace('\\neq', '≠')
    text = text.replace('\\times', '×')
    text = text.replace('\\div', '÷')
    
    # Note: No need to escape HTML - Jinja2 autoescape handles this
    return text


def generate_worksheet_pdf(data: WorksheetRequest) -> BytesIO:
    """Generate PDF worksheet using WeasyPrint (native UTF-8/Cyrillic support)"""
    # Approach 3 (Hybrid): Default labels (English fallback)
    default_labels = {
        "school": "School:",
        "teacher": "Teacher:",
        "grade": "Grade:",
        "student": "Student:",
        "date": "Date:",
        "problem_count": "Number of Problems:",
        "description": "Description:",
        "problem": "Problem",
        "solutions": "Solutions",
        "solution": "Solution",
        "generated_via": "Generated via"
    }
    
    # Use labels from frontend or fallback to English (Approach 3)
    labels = data.labels if data.labels else default_labels
    
    # Prepare metadata
    metadata = {}
    if data.school_name:
        metadata['school'] = data.school_name
    if data.teacher_name:
        metadata['teacher'] = data.teacher_name
    if data.grade:
        metadata['grade'] = data.grade
    if data.description:
        metadata['description'] = data.description
    metadata['date'] = True
    metadata['problem_count'] = True
    metadata['student'] = True  # Show student name field
    
    # Clean problem content
    problems = []
    for problem in data.problems:
        problems.append({
            'id': problem.id,
            'content': clean_text_for_html(problem.content),
            'solution': clean_text_for_html(problem.solution) if problem.solution else None
        })
    
    # Footer text
    footer_text = f"{labels.get('generated_via', 'Generated via')} Olympiad Math Archive | app.mismath.net | {datetime.now().strftime('%d.%m.%Y %H:%M')}"
    
    # Render HTML template
    template = env.get_template('worksheet_template.html')
    html_content = template.render(
        title=data.title,
        labels=labels,
        metadata=metadata,
        problems=problems,
        include_solutions=data.include_solutions,
        footer_text=footer_text
    )
    
    # Generate PDF with WeasyPrint
    buffer = BytesIO()
    HTML(string=html_content).write_pdf(buffer)
    buffer.seek(0)
    return buffer


@router.post("/worksheet/generate-pdf")
async def generate_worksheet_pdf_endpoint(request: Request):
    """Generate worksheet PDF with UTF-8 Cyrillic support"""
    try:
        # Manually parse request body as UTF-8 to avoid latin-1 encoding issues
        body_bytes = await request.body()
        body_str = body_bytes.decode('utf-8')
        data_dict = json.loads(body_str)
        
        # Convert dict to WorksheetRequest model
        data = WorksheetRequest(**data_dict)
    except UnicodeDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid UTF-8 encoding: {str(e)}")
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Request parsing failed: {str(e)}")
    
    """
    Generate PDF worksheet from selected problems
    
    Request Body:
    {
        "title": "Геометрија - Триаголници",
        "description": "Работен лист за 7 одделение",
        "problems": [
            {
                "id": "1",
                "problem_id": "sigma_138_1874",
                "content": "Најдете ја површината...",
                "solution": "Користиме формула...",
                "difficulty": 3,
                "grade": 7,
                "topic": "geometry"
            }
        ],
        "include_solutions": true,
        "school_name": "ОУ Кирил и Методиј",
        "teacher_name": "Марија Петровска",
        "grade": 7
    }
    
    Returns: PDF file (application/pdf)
    """
    try:
        # Validate input
        if not data.problems:
            raise HTTPException(status_code=400, detail="No problems provided")
        
        if len(data.problems) > 50:
            raise HTTPException(status_code=400, detail="Maximum 50 problems allowed")
        
        # Generate PDF
        pdf_buffer = generate_worksheet_pdf(data)
        
        # Generate filename (ASCII-safe to avoid HTTP header encoding issues)
        safe_title = data.title.encode('ascii', 'ignore').decode('ascii') or 'worksheet'
        filename = f"worksheet_{safe_title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
        
        # Return PDF
        return Response(
            content=pdf_buffer.getvalue(),
            media_type="application/pdf",
            headers={
                "Content-Disposition": f"attachment; filename={filename}",
                "Content-Type": "application/pdf"
            }
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF generation failed: {str(e)}")


@router.post("/worksheet/preview-html")
async def preview_worksheet_html(data: WorksheetRequest):
    """
    Preview worksheet (for debugging)
    
    Returns: JSON with problem list
    """
    try:
        return {
            "title": data.title,
            "description": data.description,
            "problem_count": len(data.problems),
            "problems": [
                {
                    "id": p.id,
                    "problem_id": p.problem_id,
                    "content_preview": p.content[:100] if p.content else "No content"
                }
                for p in data.problems
            ]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Preview failed: {str(e)}")


@router.get("/worksheet/templates")
async def get_worksheet_templates():
    """
    Get all available worksheet templates
    
    Returns: JSON with template list
    """
    try:
        return {
            "templates": TEMPLATES,
            "count": len(TEMPLATES)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get templates: {str(e)}")


@router.get("/worksheet/templates/{template_id}")
async def get_template_details(template_id: str):
    """
    Get details for a specific template
    
    Returns: JSON with template configuration
    """
    try:
        template = get_template(template_id)
        if not template:
            raise HTTPException(status_code=404, detail=f"Template '{template_id}' not found")
        
        # Calculate problem counts
        problem_counts = calculate_problem_counts(template_id)
        
        return {
            "template": template,
            "problem_counts": problem_counts
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get template: {str(e)}")


class TemplateSelectionRequest(BaseModel):
    """Request model for template-based problem selection"""
    template_id: str
    topic: Optional[str] = None  # Filter by topic (geometry, algebra, etc.)
    grade: Optional[int] = None  # Filter by grade level
    bro_standards: Optional[List[str]] = None  # Filter by БРО standards


@router.post("/worksheet/select-problems")
async def select_problems_from_template(data: TemplateSelectionRequest):
    """
    Auto-select problems based on template configuration
    
    This is a placeholder - actual implementation would query MongoDB
    For now, returns mock data structure
    
    Returns: JSON with selected problems
    """
    try:
        template = get_template(data.template_id)
        if not template:
            raise HTTPException(status_code=404, detail=f"Template '{data.template_id}' not found")
        
        problem_counts = calculate_problem_counts(data.template_id)
        
        # TODO: Implement actual database query
        # For now, return structure that frontend expects
        return {
            "template_id": data.template_id,
            "template_name": template["name"],
            "problem_counts": problem_counts,
            "filters": {
                "topic": data.topic,
                "grade": data.grade,
                "bro_standards": data.bro_standards
            },
            "message": "Problem selection endpoint ready. Database integration needed.",
            "next_step": "Integrate with MongoDB problems collection"
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Problem selection failed: {str(e)}")
