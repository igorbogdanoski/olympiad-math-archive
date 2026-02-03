import os
import uvicorn
import json
import re
import subprocess
import uuid
import tempfile
import sys
import shutil
from typing import List, Optional, Dict, Any

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import pymongo
import frontmatter
import markdown
from google import genai
from playwright.async_api import async_playwright
from celery.result import AsyncResult
from celery_worker import celery_app, generate_pdf_task, generate_video_task
from models.test_instance import TestInstance
from tools.qr_generator import create_qr_code
from routers import dashboard, problems, lesson_planner, quiz_generator
from database import get_database
from dotenv import load_dotenv

# Import our "Brain"
from prompt_builder import build_system_prompt, build_lesson_plan_prompt
from worksheet_generator import generate_worksheet_html

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

# --- CONFIGURATION ---
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
GENAI_API_KEY = os.getenv("GENAI_API_KEY") or os.getenv("GOOGLE_API_KEY")
API_BASE_URL = os.getenv("PUBLIC_API_URL", "http://localhost:8000")

ai_client = None
if not GENAI_API_KEY or GENAI_API_KEY == "YOUR_NEW_SECURE_API_KEY_HERE":
    print("WARNING: GENAI_API_KEY not found in environment variables! AI features will fail.")
else:
    ai_client = genai.Client(api_key=GENAI_API_KEY)

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(dashboard.router, prefix="/api")
app.include_router(problems.router, prefix="/api")
app.include_router(lesson_planner.router)
app.include_router(quiz_generator.router)

# MongoDB Connection
db = get_database()
collection = db["curriculum"]
problems_collection = db["problems"]

# Ensure videos and worksheets directory exists
os.makedirs("videos", exist_ok=True)
os.makedirs("worksheets", exist_ok=True)

# Static files
app.mount("/videos", StaticFiles(directory="videos"), name="videos")
app.mount("/worksheets", StaticFiles(directory="worksheets"), name="worksheets")

# --- MODELS ---

class Activity(BaseModel):
    title: str
    description: Optional[str] = None

class Theme(BaseModel):
    title: str
    objectives: List[str] = []
    standards: List[str] = []
    activities: List[str] = []

class LessonRequest(BaseModel):
    grade: str
    themeIndex: int
    activityIndex: int

class LessonIntro(BaseModel):
    duration: str
    hook: str
    context: str

class LessonCoreActivity(BaseModel):
    duration: str
    description: str
    visual_focus: str
    key_questions: List[str]

class LessonOlympiadBridge(BaseModel):
    duration: str
    connection: str
    example_problem_brief: str

class LessonAssessment(BaseModel):
    duration: str
    method: str
    homework_suggestion: str

class LessonPlan(BaseModel):
    title: str
    standard_code: Optional[str] = None
    intro: LessonIntro
    core_activity: LessonCoreActivity
    olympiad_bridge: LessonOlympiadBridge
    assessment: LessonAssessment

class PresentationRequest(BaseModel):
    plan: LessonPlan

class ProblemSearchRequest(BaseModel):
    query: Optional[str] = None
    grade: Optional[str] = None
    topic: Optional[str] = None
    difficulty: Optional[int] = None
    limit: int = 20

class StandardFilterRequest(BaseModel):
    standardCode: str
    limit: int = 10

class ManimRequest(BaseModel):
    grade: str
    topic: str
    activity: str

class VideoRequest(BaseModel):
    text: str
    grade: str

class WorksheetRequest(BaseModel):
    standardCode: str
    teacherMode: Optional[bool] = False

class WorksheetPDFRequest(BaseModel):
    items: List[Dict[str, Any]]
    header: Dict[str, str]
    include_answer_key: Optional[bool] = False

# --- HELPERS ---

CSS_STYLE_PDF = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    body { font-family: 'Inter', sans-serif; line-height: 1.6; color: #333; max-width: 900px; margin: 0 auto; padding: 20px; background-color: white; }
    .sheet-container { background: white; padding: 40px; border-radius: 16px; position: relative; }
    header { text-align: center; border-bottom: 4px solid #3b82f6; padding-bottom: 20px; margin-bottom: 30px; }
    h1 { color: #1e293b; margin: 0; font-size: 28px; letter-spacing: -0.5px; }
    .meta-info { color: #64748b; margin-top: 10px; font-size: 14px; font-weight: 500; }
    .problem-box { margin-bottom: 25px; padding: 25px; border: 1px solid #e2e8f0; border-radius: 12px; background: #fff; border-color: #3b82f6; background: #f8faff; position: relative; }
    .problem-number { position: absolute; top: -12px; left: 20px; background: #3b82f6; color: white; padding: 2px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; }
    .content-body p { margin-top: 0; margin-bottom: 12px; }
    .content-body p:last-child { margin-bottom: 0; }
    footer { margin-top: 40px; text-align: center; font-size: 10px; color: #94a3b8; border-top: 1px solid #e2e8f0; padding-top: 10px; }
</style>
"""

def process_latex(text: str):
    text = re.sub(r'\$\$(.*?)\$\$', r'\\\[ \1 \\\]', text, flags=re.DOTALL)
    text = re.sub(r'\$([^\$]+)\$', r'\\\( \1 \\\)', text)
    return text

def render_content(text: str):
    if not text: return ""
    # Support for GeoGebra [geogebra:ID]
    text = re.sub(
        r'\[geogebra:([a-zA-Z0-9]+)\]', 
        r'<div class="geogebra-container" style="margin: 20px 0; border-radius: 12px; overflow: hidden; border: 1px solid #e2e8f0;"><iframe src="https://www.geogebra.org/material/iframe/id/\1/width/800/height/600/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="100%" height="400px" style="border:0px;"></iframe></div>', 
        text
    )
    processed_text = process_latex(text)
    return markdown.markdown(processed_text, extensions=['extra', 'nl2br', 'sane_lists'])

# --- ENDPOINTS ---

@app.get("/")
def read_root():
    return {"message": "MathSathi Backend is Running! "}

@app.get("/api/tasks/{task_id}")
async def get_task_status(task_id: str):
    """
    Checks the status of a Celery background task.
    """
    task_result = AsyncResult(task_id, app=celery_app)
    result = {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None
    }
    return result

@app.get("/grades")
def get_grades():
    """Returns a list of all available grades in the database."""
    # Get distinct grades and sort them logically if possible, or just return list
    grades = collection.distinct("grade")
    return {"count": len(grades), "grades": grades}

@app.get("/curriculum/{grade}")
def get_curriculum(grade: str):
    """Returns the full curriculum for a specific grade."""
    data = collection.find_one({"grade": grade}, {"_id": 0})
    if not data:
        raise HTTPException(status_code=404, detail="Grade not found")
    
    # Ensure frontend compatibility by adding grade_level if it's missing
    grade_level = data.get("grade_level", data.get("grade"))
    
    return {**data, "grade_level": grade_level}

@app.post("/generate-lesson")
async def generate_lesson(request: LessonRequest):
    """
    Generates Manim Python code using Gemini AI.
    """
    if not GENAI_API_KEY:
        raise HTTPException(status_code=503, detail="Gemini API Key is not configured on the server.")

    safe_print(f"Received request for Grade: {request.grade}, Theme: {request.themeIndex}, Activity: {request.activityIndex}")

    # 1. Fetch data from DB
    grade_data = collection.find_one({"grade": request.grade})
    
    if not grade_data:
        raise HTTPException(status_code=404, detail="Grade data not found")
    
    try:
        # Safely access the nested lists
        themes_list = grade_data.get('themes', [])
        if request.themeIndex >= len(themes_list):
             raise IndexError(f"Theme index {request.themeIndex} out of range.")
             
        theme_data = themes_list[request.themeIndex]
        
        activities_list = theme_data.get('activities', [])
        if request.activityIndex >= len(activities_list):
             raise IndexError(f"Activity index {request.activityIndex} out of range.")

        activity = activities_list[request.activityIndex]
        
        # Prepare context for the prompt builder
        lesson_context = {
            "grade": request.grade,
            "title": theme_data.get('title', 'Unknown Topic'),
            "objectives": theme_data.get('objectives', []),
            "standards": theme_data.get('standards', [])
        }
        
    except (IndexError, KeyError, TypeError) as e:
        safe_print(f"Data Error: {e}")
        raise HTTPException(status_code=400, detail=f"Invalid data structure or index: {str(e)}")

    # 2. Build the Prompt
    final_prompt = build_system_prompt(lesson_context, activity)
    
    print("Prompt constructed. Sending to Gemini...")

    # 3. Call Gemini API
    try:
        model = genai.GenerativeModel('gemini-1.5-pro') 
        response = model.generate_content(final_prompt)
        
        raw_text = response.text
        
        # Clean up the code block markdown
        pattern = r"```python(.*?)```"
        match = re.search(pattern, raw_text, re.DOTALL)
        if match:
            cleaned_code = match.group(1).strip()
        else:
            cleaned_code = raw_text.replace("```python", "").replace("```", "").strip()
        
        print("Code generated successfully!")
        return {"code": cleaned_code, "prompt_used": final_prompt}

    except Exception as e:
        print(f"Error calling Gemini: {e}")
        raise HTTPException(status_code=500, detail=f"AI Generation failed: {str(e)}")

@app.post("/generate-video")
async def generate_video(request: VideoRequest):
    """
    Generates and renders a Manim video lesson using Gemini AI.
    """
    if not GENAI_API_KEY:
        raise HTTPException(status_code=503, detail="Gemini API Key is not configured on the server.")

    safe_print(f"Received video request for Grade: {request.grade}")

    # 1. Try to find context in DB for better prompt
    grade_data = collection.find_one({"grade": request.grade})
    lesson_context = {"grade": request.grade, "title": "Математика"}
    
    if grade_data:
        for theme in grade_data.get('themes', []):
            # Check if our target text is in this theme's objectives or activities
            combined = str(theme.get('objectives', [])) + str(theme.get('activities', []))
            if request.text in combined or any(request.text in str(obj) for obj in theme.get('objectives', [])):
                lesson_context["title"] = theme.get('title', 'Математика')
                lesson_context["objectives"] = theme.get('objectives', [])
                lesson_context["standards"] = theme.get('standards', [])
                break

    # 2. Build the Prompt
    final_prompt = build_system_prompt(lesson_context, request.text)
    
    # 3. Call Gemini API
    try:
        # Using gemini-3-flash-preview for better logic and high-quality script generation
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(final_prompt)
        
        raw_text = response.text
        
        # Clean up the code block markdown
        pattern = r"```python(.*?)```"
        match = re.search(pattern, raw_text, re.DOTALL)
        if match:
            cleaned_code = match.group(1).strip()
        else:
            cleaned_code = raw_text.replace("```python", "").replace("```", "").strip()
        
        # 4. Start Background Task
        video_id = str(uuid.uuid4())
        task = generate_video_task.delay(cleaned_code, video_id)
        
        return {
            "task_id": task.id,
            "status": "pending",
            "message": "Video generation started in background."
        }

    except Exception as e:
        print(f"Error in generate_video: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-lesson-plan")
async def generate_lesson_plan(request: LessonRequest):
    """
    Generates a full lesson plan in JSON format using Gemini AI.
    """
    if not GENAI_API_KEY:
        raise HTTPException(status_code=503, detail="Gemini API Key is not configured on the server.")

    # 1. Fetch data from DB
    grade_data = collection.find_one({"grade": request.grade})
    if not grade_data:
        raise HTTPException(status_code=404, detail="Grade data not found")
    
    try:
        themes_list = grade_data.get('themes', [])
        theme_data = themes_list[request.themeIndex]
        activity = theme_data.get('activities', [])[request.activityIndex]
        
        lesson_context = {
            "grade": request.grade,
            "title": theme_data.get('title', 'Unknown Topic'),
            "objectives": theme_data.get('objectives', []),
            "standards": theme_data.get('standards', [])
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Invalid data selection: {str(e)}")

    # 2. Build the Prompt
    final_prompt = build_lesson_plan_prompt(lesson_context, activity)
    
    # 3. Call Gemini API
    try:
        # Use JSON mode for 100% reliability
        model = genai.GenerativeModel(
            'gemini-1.5-pro',
            generation_config={"response_mime_type": "application/json"}
        ) 
        response = model.generate_content(final_prompt)
        
        raw_text = response.text
        
        import json
        plan_data = json.loads(raw_text)
        
        # Add standard code if possible
        standards_with_codes = theme_data.get('standards_with_codes', [])
        if request.activityIndex < len(standards_with_codes):
            plan_data["standard_code"] = standards_with_codes[request.activityIndex]['code']
        elif standards_with_codes:
            plan_data["standard_code"] = standards_with_codes[0]['code']

        # Validate with Pydantic
        validated_plan = LessonPlan(**plan_data)
        
        return validated_plan.dict()

    except Exception as e:
        print(f"Error generating lesson plan: {e}")
        # If it fails, try a manual cleanup as fallback
        try:
            cleaned_json = raw_text.replace("```json", "").replace("```", "").strip()
            return json.loads(cleaned_json)
        except:
            raise HTTPException(status_code=500, detail=f"Failed to generate valid lesson plan: {str(e)}")

@app.post("/generate-presentation")
async def generate_presentation(request: PresentationRequest):
    """
    Transforms a lesson plan into a Reveal.js presentation (HTML).
    """
    plan = request.plan
    
    html_template = f"""
    <!doctype html>
    <html lang="mk">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
        <title>{plan.title}</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/theme/league.min.css">
        <script>
            window.MathJax = {{
                tex: {{
                    inlineMath: [['\\\\(', '\\\\)']],
                    displayMath: [['\\\\[', '\\\\]']],
                    processEscapes: true
                }}
            }};
        </script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
    </head>
    <body>
        <div class="reveal">
            <div class="slides">
                <!-- Title Slide -->
                <section data-background-gradient="linear-gradient(to bottom, #283048, #859398)">
                    <h1>{plan.title}</h1>
                    <p>Наставно Сценарио</p>
                    <div style="margin-top: 50px; font-size: 0.6em;">Подготвено од МатАрхива AI</div>
                </section>

                <!-- Intro Slide -->
                <section>
                    <section>
                        <h2>01. Вовед ({plan.intro.duration})</h2>
                        <hr>
                        <blockquote style="font-style: italic;">
                            "{plan.intro.hook}"
                        </blockquote>
                    </section>
                    <section>
                        <h3>Контекст</h3>
                        <p>{plan.intro.context}</p>
                    </section>
                </section>

                <!-- Core Activity -->
                <section>
                    <section>
                        <h2>02. Главна Активност ({plan.core_activity.duration})</h2>
                        <hr>
                        <p>{plan.core_activity.description}</p>
                    </section>
                    <section>
                        <h3>Визуелен Фокус</h3>
                        <div style="background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px;">
                            {plan.core_activity.visual_focus}
                        </div>
                    </section>
                    <section>
                        <h3>Клучни прашања</h3>
                        <ul>
                            {"".join([f"<li>{q}</li>" for q in plan.core_activity.key_questions])}
                        </ul>
                    </section>
                </section>

                <!-- Olympiad Bridge -->
                <section data-background-color="#4a148c">
                    <h2>03. Олимписки Мост ({plan.olympiad_bridge.duration})</h2>
                    <hr>
                    <p>{plan.olympiad_bridge.connection}</p>
                    <div style="background: rgba(0,0,0,0.3); padding: 20px; border-radius: 10px; font-size: 0.8em;">
                        <strong>Предизвик:</strong> {plan.olympiad_bridge.example_problem_brief}
                    </div>
                </section>

                <!-- Assessment -->
                <section>
                    <h2>04. Евалуација ({plan.assessment.duration})</h2>
                    <hr>
                    <h3>Како ќе провериме?</h3>
                    <p>{plan.assessment.method}</p>
                    <div style="margin-top: 30px; border-left: 5px solid #00c853; padding-left: 20px;">
                        <strong>Домашна:</strong> {plan.assessment.homework_suggestion}
                    </div>
                </section>

                <section>
                    <h2>Благодариме!</h2>
                    <p>Среќен час!</p>
                </section>
            </div>
        </div>

        <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.5.0/reveal.min.js"></script>
        <script>
            Reveal.initialize({{
                hash: true,
                center: true,
                transition: 'slide'
            }});
        </script>
    </body>
    </html>
    """
    return {"html": html_template}

@app.post("/generate-manim")
async def generate_manim(request: ManimRequest):
    """
    Generates a Manim animation based on a specific activity.
    """
    if not GENAI_API_KEY:
        raise HTTPException(status_code=503, detail="Gemini API Key is not configured.")

    # 1. Build the specialized Manim prompt
    # We reuse build_system_prompt from prompt_builder.py which is already CoT-optimized
    lesson_context = {
        "grade": request.grade,
        "title": request.topic
    }
    final_prompt = build_system_prompt(lesson_context, request.activity)
    
    # 2. Call Gemini
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content(final_prompt)
        raw_text = response.text
        
        # Extract code
        pattern = r"```python(.*?)```"
        match = re.search(pattern, raw_text, re.DOTALL)
        if match:
            cleaned_code = match.group(1).strip()
        else:
            cleaned_code = raw_text.replace("```python", "").replace("```", "").strip()
            
        # 3. Start background task
        video_id = str(uuid.uuid4())
        task = generate_video_task.delay(cleaned_code, video_id)
        
        return {
            "task_id": task.id,
            "status": "pending",
            "message": "Manim animation generation started."
        }
    except Exception as e:
        print(f"Error in generate_manim: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/problems/search")
async def search_problems(request: ProblemSearchRequest):
    """
    Search for problems in MongoDB with filtering.
    """
    query_filter = {}
    
    if request.query:
        # Simple regex search in title or content
        regex_query = {"$regex": request.query, "$options": "i"}
        query_filter["$or"] = [
            {"title": regex_query},
            {"content_markdown": regex_query}
        ]
    
    if request.grade:
        query_filter["grade"] = str(request.grade)
        
    if request.topic:
        query_filter["topic"] = {"$regex": request.topic, "$options": "i"}
        
    if request.difficulty:
        query_filter["difficulty"] = request.difficulty

    # Perform search
    cursor = problems_collection.find(query_filter).limit(request.limit)
    results = []
    
    for doc in cursor:
        results.append({
            "id": doc.get("problem_id"),
            "title": doc.get("title"),
            "content_markdown": doc.get("content_markdown"),
            "solution": doc.get("solution", ""),
            "topic": doc.get("topic"),
            "difficulty": doc.get("difficulty"),
            "path": doc.get("source_path")
        })
            
    return {"problems": results}

@app.post("/api/problems/by-standard")
async def get_problems_by_standard(request: StandardFilterRequest):
    """
    Finds problems mapped to a curriculum standard.
    Hybrid Logic:
    1. Primary: Match by curriculum_codes
    2. Fallback: Search by standard name/keywords if primary has few results
    """
    code = request.standardCode
    
    # 1. Direct match
    cursor = problems_collection.find({"curriculum_codes": code}).limit(request.limit)
    results = []
    for doc in cursor:
        results.append({
            "id": doc.get("problem_id"),
            "title": doc.get("title"),
            "content_markdown": doc.get("content_markdown"),
            "topic": doc.get("topic"),
            "difficulty": doc.get("difficulty"),
            "curriculum_codes": doc.get("curriculum_codes", [])
        })
    
    # 2. Hybrid Fallback (if we need more problems)
    if len(results) < 3:
        # Find the standard name from curriculum SSOT to use as search query
        # Standard code format example: MAT-O-G9-T3-S4
        grade_match = re.search(r'G(\d+)', code)
        if grade_match:
            grade_key = f"grade_{grade_match.group(1)}"
            grade_data = db["curriculum"].find_one({"grade": grade_key})
            
            if grade_data:
                standard_text = ""
                for theme in grade_data.get("themes", []):
                    if theme.get("code") == code:
                        standard_text = theme.get("name")
                        break
                    for s in theme.get("standards_with_codes", []):
                        if s.get("code") == code:
                            standard_text = s.get("description")
                            break
                
                if standard_text:
                    # Simple text search fallback (avoiding already found IDs)
                    existing_ids = [r["id"] for r in results]
                    regex_query = {"$regex": standard_text[:30], "$options": "i"} # Take first 30 chars
                    
                    fallback_cursor = problems_collection.find({
                        "problem_id": {"$nin": existing_ids},
                        "grade": grade_key.replace("grade_", ""),
                        "$or": [
                            {"title": regex_query},
                            {"content_markdown": regex_query},
                            {"tags": {"$in": [standard_text.lower()]}}
                        ]
                    }).limit(request.limit - len(results))
                    
                    for doc in fallback_cursor:
                        results.append({
                            "id": doc.get("problem_id"),
                            "title": doc.get("title"),
                            "content_markdown": doc.get("content_markdown"),
                            "topic": doc.get("topic"),
                            "difficulty": doc.get("difficulty"),
                            "curriculum_codes": doc.get("curriculum_codes", []),
                            "is_fallback": True
                        })

    # 3. Add one "Olympiad Challenge" (Hard problem from same grade/topic if possible)
    if results:
        topic = results[0]["topic"]
        hard_problem = problems_collection.find_one({
            "problem_id": {"$nin": [r["id"] for r in results]},
            "difficulty": {"$gte": 4},
            "topic": topic
        })
        if hard_problem:
            results.append({
                "id": hard_problem.get("problem_id"),
                "title": f"🌟 Олимписки предизвик: {hard_problem.get('title')}",
                "content_markdown": hard_problem.get("content_markdown"),
                "topic": hard_problem.get("topic"),
                "difficulty": hard_problem.get("difficulty"),
                "curriculum_codes": hard_problem.get("curriculum_codes", []),
                "is_challenge": True
            })

    return {"problems": results}

@app.post("/api/pdf/generate")
async def generate_pdf(request: WorksheetPDFRequest):
    """
    Generates a PDF from selected problems using Playwright.
    """
    html_content = f"""
    <!DOCTYPE html>
    <html lang="mk">
    <head>
        <meta charset="UTF-8">
        <script>
            window.MathJax = {{
                tex: {{
                    inlineMath: [['\\\\(', '\\\\)']],
                    displayMath: [['\\\\[', '\\\\]']],
                    processEscapes: true
                }}
            }};
        </script>
        <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
        {CSS_STYLE_PDF}
    </head>
    <body>
        <div class="sheet-container">
            <header>
                <h1>{request.header.get('title', 'Наставен лист')}</h1>
                <div class="meta-info">
                    {request.header.get('teacher', '')} • {request.header.get('date', '')} • {request.header.get('grade', '')} одд.
                </div>
            </header>
    """
    
    for i, item in enumerate(request.items):
        html_content += f"""
            <div class="problem-box">
                <div class="problem-number">Задача {i+1}</div>
                <div class="content-body">{render_content(item.get('content_markdown', ''))}</div>
            </div>
        """
    
    if request.include_answer_key:
        html_content += f"""
            <div style="page-break-before: always;"></div>
            <header>
                <h1>Клуч со одговори</h1>
                <div class="meta-info">
                    {request.header.get('title', 'Наставен лист')}
                </div>
            </header>
        """
        for i, item in enumerate(request.items):
            if item.get('solution'):
                html_content += f"""
                    <div class="problem-box" style="border-color: #10b981; background: #f0fdf4;">
                        <div class="problem-number" style="background: #10b981;">Решение {i+1}</div>
                        <div class="content-body">{render_content(item.get('solution', ''))}</div>
                    </div>
                """
        
    html_content += """
            <footer>
                <p>Генерирано со МатАрхива AI</p>
            </footer>
        </div>
        <script>
            window.addEventListener('load', () => {
                if (window.MathJax && window.MathJax.typesetPromise) {
                    window.MathJax.typesetPromise().then(() => {
                        window.mathjaxFinished = true;
                    });
                } else {
                    window.mathjaxFinished = true;
                }
            });
        </script>
    </body>
    </html>
    """
    
    pdf_id = str(uuid.uuid4())
    pdf_filename = f"worksheet_{pdf_id}.pdf"
    
    # --- QR & TEST REGISTRATION ---
    test_id = str(uuid.uuid4())[:8].upper()
    qr_base64 = create_qr_code(test_id)
    
    # Inject QR into HTML
    qr_html = f"""
    <div style="position: absolute; top: 20px; right: 20px; text-align: center;">
        <img src="{qr_base64}" style="width: 80px; height: 80px;">
        <div style="font-family: monospace; font-size: 10px; color: #64748b;">ID: {test_id}</div>
    </div>
    """
    html_content = html_content.replace('<div class="sheet-container">', f'<div class="sheet-container">{qr_html}')
    
    # Register in DB
    solutions_list = []
    for i, item in enumerate(request.items):
        solutions_list.append({
            "problem_index": i + 1,
            "content_snippet": (item.get('content_markdown', '')[:50] + "..."),
            "correct_answer": item.get('solution', 'Нема решение'),
            "points": item.get('points', 1)
        })
    
    test_instance = TestInstance(
        _id=test_id,
        grade=request.header.get('grade', 'Непознато'),
        topic=request.header.get('title', 'Непозната тема'),
        solutions=solutions_list
    )
    db["test_instances"].insert_one(test_instance.dict(by_alias=True))
    # ------------------------------
    
    # Start background task
    task = generate_pdf_task.delay(html_content, pdf_filename)
    
    return {
        "task_id": task.id,
        "status": "pending",
        "message": "PDF generation started in background."
    }

class MutateRequest(BaseModel):
    problem_id: str
    content: str
    count: int = 1

@app.post("/api/problems/mutate")
async def mutate_problem(request: MutateRequest):
    """
    Uses Gemini AI to generate variations of a math problem.
    """
    if not GENAI_API_KEY:
        raise HTTPException(status_code=500, detail="Gemini API Key not configured")

    prompt = f"""
    You are an expert mathematics teacher. Take the following math problem and generate {request.count} variations.
    The variations must:
    1. Keep the exact same mathematical logic and difficulty.
    2. Change the numerical values and names/context if appropriate.
    3. Be written in Macedonian (Cyrillic).
    4. Return the result as a JSON list of objects, each with 'content_markdown' and 'solution' fields.
    
    Problem:
    {request.content}
    
    Output ONLY valid JSON.
    """
    
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        text = response.text
        
        # Extract JSON from response
        json_match = re.search(r'\[.*\]', text, re.DOTALL)
        if json_match:
            try:
                variations = json.loads(json_match.group(0))
                return {"variations": variations}
            except json.JSONDecodeError:
                return {"raw_ai_response": text, "error": "Failed to parse JSON"}
        else:
            # Fallback if AI didn't return pure JSON
            return {"raw_ai_response": text}
            
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate-worksheet")
async def generate_worksheet(request: WorksheetRequest):
    """
    Generates an HTML worksheet based on a specific curriculum standard code.
    """
    html = generate_worksheet_html(request.standardCode, teacher_mode=request.teacherMode)
    if not html:
        raise HTTPException(status_code=404, detail="Standard code not found or generation failed")
    
    return {"html": html}

@app.post("/api/tests/register")
async def register_test(test_data: TestInstance):
    """Registers a new test instance and its solutions."""
    # Зачувај во колекцијата 'test_instances'
    result = db["test_instances"].insert_one(test_data.dict(by_alias=True))
    return {"status": "success", "id": test_data.id}

@app.get("/api/tests/{test_id}")
async def get_test_solution(test_id: str):
    """Retrieves solutions for a specific test via its ID."""
    test = db["test_instances"].find_one({"_id": test_id})
    
    if not test:
        raise HTTPException(status_code=404, detail="Тестот не е пронајден")
    
    # Convert _id to string for JSON serialization if necessary
    test["_id"] = str(test["_id"])
    return test

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)

@app.get("/health")
def health_check():
    return {"status": "ok"}
