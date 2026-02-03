"""
Worksheet Router - PDF Generation API
Created: February 3, 2026
Purpose: Generate PDF worksheets from selected problems
"""
from fastapi import APIRouter, HTTPException
from fastapi.responses import Response
from pydantic import BaseModel
from typing import List, Optional
from io import BytesIO
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os
import html

router = APIRouter()

# Register Unicode font for Cyrillic support
# Use Arial (available on all Windows systems)
font_paths = [
    "C:\\Windows\\Fonts\\arial.ttf",  # Arial Regular
    "C:\\Windows\\Fonts\\Arial.ttf",  # Case variation
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",  # Linux
]

font_registered = False
for font_path in font_paths:
    if os.path.exists(font_path):
        try:
            # Register font for Cyrillic support (TrueType fonts support Unicode by default)
            pdfmetrics.registerFont(TTFont('CustomFont', font_path))
            pdfmetrics.registerFont(TTFont('CustomFont-Bold', font_path))  # Reuse for bold
            font_registered = True
            break
        except Exception as e:
            print(f"Font registration error: {e}")
            continue

# If no font found, we'll use built-in fonts (limited Cyrillic support)
DEFAULT_FONT = 'CustomFont' if font_registered else 'Helvetica'


def encode_for_reportlab(text: str) -> str:
    """Encode Unicode (Cyrillic) characters as numeric HTML entities for ReportLab"""
    if not text:
        return ""
    result = []
    for char in text:
        # ASCII characters pass through (except special HTML chars)
        if ord(char) < 128:
            if char == '&':
                result.append('&amp;')
            elif char == '<':
                result.append('&lt;')
            elif char == '>':
                result.append('&gt;')
            else:
                result.append(char)
        else:
            # Non-ASCII (Cyrillic, Greek, etc.) as numeric entities
            result.append(f'&#{ord(char)};')
    return ''.join(result)


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


def clean_text_for_pdf(text: str) -> str:
    """Clean text for PDF rendering - remove LaTeX delimiters and encode for ReportLab"""
    if not text:
        return ""
    
    # Ensure text is properly decoded/encoded as UTF-8
    if isinstance(text, bytes):
        text = text.decode('utf-8')
    
    # Remove LaTeX math delimiters (we'll render them as plain text for now)
    text = text.replace('\\(', '').replace('\\)', '')
    text = text.replace('\\[', '\n').replace('\\]', '\n')
    text = text.replace('$$', '\n').replace('$$', '\n')
    text = text.replace('$', '')
    # Replace common LaTeX symbols with Unicode
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
    
    # Encode Cyrillic and other Unicode as numeric HTML entities for ReportLab
    text = encode_for_reportlab(text)
    
    return text


def generate_worksheet_pdf(data: WorksheetRequest) -> BytesIO:
    """Generate PDF worksheet using ReportLab"""
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
    
    # Use labels from frontend or fallback to English
    raw_labels = data.labels if data.labels else default_labels
    
    # Encode all label values for ReportLab (handles Cyrillic)
    labels = {}
    for key, value in raw_labels.items():
        labels[key] = encode_for_reportlab(value) if value else ""
    
    buffer = BytesIO()
    
    # Create PDF document
    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=2*cm,
        leftMargin=2*cm,
        topMargin=2*cm,
        bottomMargin=2*cm
    )
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#2C3E50'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName=DEFAULT_FONT
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.HexColor('#4CAF50'),
        spaceAfter=8,
        spaceBefore=8,
        fontName=DEFAULT_FONT
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=6,
        fontName=DEFAULT_FONT
    )
    
    solution_style = ParagraphStyle(
        'Solution',
        parent=styles['Normal'],
        fontSize=10,
        leftIndent=20,
        textColor=colors.HexColor('#2E7D32'),
        fontName=DEFAULT_FONT
    )
    
    # Build document content
    story = []
    
    # Title
    story.append(Paragraph(clean_text_for_pdf(data.title), title_style))
    story.append(Spacer(1, 0.5*cm))
    
    # Metadata as paragraphs (avoid Table with Cyrillic)
    meta_style = ParagraphStyle(
        'Meta',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.grey,
        fontName=DEFAULT_FONT
    )
    
    # Use dynamic labels from request (Approach 3)
    if data.school_name:
        label = clean_text_for_pdf(labels.get('school', 'School:'))
        value = clean_text_for_pdf(data.school_name)
        story.append(Paragraph(f"<b>{label}</b> {value}", meta_style))
    if data.teacher_name:
        label = clean_text_for_pdf(labels.get('teacher', 'Teacher:'))
        value = clean_text_for_pdf(data.teacher_name)
        story.append(Paragraph(f"<b>{label}</b> {value}", meta_style))
    if data.grade:
        label = clean_text_for_pdf(labels.get('grade', 'Grade:'))
        story.append(Paragraph(f"<b>{label}</b> {data.grade}", meta_style))
    if data.description:
        label = clean_text_for_pdf(labels.get('description', 'Description:'))
        value = clean_text_for_pdf(data.description)
        story.append(Paragraph(f"<b>{label}</b> {value}", meta_style))
    
    date_label = clean_text_for_pdf(labels.get('date', 'Date:'))
    story.append(Paragraph(f"<b>{date_label}</b> {datetime.now().strftime('%d.%m.%Y')}", meta_style))
    
    count_label = clean_text_for_pdf(labels.get('problem_count', 'Number of Problems:'))
    story.append(Paragraph(f"<b>{count_label}</b> {len(data.problems)}", meta_style))
    story.append(Spacer(1, 0.8*cm))
    
    # Problems
    for i, problem in enumerate(data.problems, 1):
        # Clean title or use fallback
        if problem.problem_id:
            problem_title = clean_text_for_pdf(problem.problem_id)
        else:
            problem_label = labels.get('problem', 'Problem')
            problem_title = f"{problem_label} {i}"
        
        # Problem header
        story.append(Paragraph(
            f"<b>{i}. {problem_title}</b>",
            heading_style
        ))
        
        # Problem content
        content = clean_text_for_pdf(problem.content)
        story.append(Paragraph(content, normal_style))
        story.append(Spacer(1, 0.5*cm))
    
    # Solutions section
    if data.include_solutions:
        story.append(PageBreak())
        solutions_title = clean_text_for_pdf(labels.get('solutions', 'Solutions'))
        story.append(Paragraph(solutions_title, title_style))
        story.append(Spacer(1, 0.5*cm))
        
        for i, problem in enumerate(data.problems, 1):
            if problem.solution:
                if problem.problem_id:
                    problem_title = clean_text_for_pdf(problem.problem_id)
                else:
                    problem_label = labels.get('problem', 'Problem')
                    problem_title = f"{problem_label} {i}"
                solution_label = clean_text_for_pdf(labels.get('solution', 'Solution'))
                story.append(Paragraph(
                    f"<b>{i}. {problem_title} - {solution_label}</b>",
                    heading_style
                ))
                solution = clean_text_for_pdf(problem.solution)
                story.append(Paragraph(solution, solution_style))
                story.append(Spacer(1, 0.4*cm))
    
    # Footer
    story.append(Spacer(1, 1*cm))
    generated_label = clean_text_for_pdf(labels.get('generated_via', 'Generated via'))
    footer_text = f"{generated_label} Olympiad Math Archive | app.mismath.net | {datetime.now().strftime('%d.%m.%Y %H:%M')}"
    story.append(Paragraph(footer_text, ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.grey,
        alignment=TA_CENTER,
        fontName=DEFAULT_FONT
    )))
    
    # Build PDF
    doc.build(story)
    buffer.seek(0)
    return buffer


@router.post("/worksheet/generate-pdf")
async def generate_worksheet_pdf_endpoint(data: WorksheetRequest):
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
        
        # Generate filename
        filename = f"worksheet_{data.title.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.pdf"
        
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
