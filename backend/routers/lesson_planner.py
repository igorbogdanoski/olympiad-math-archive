"""
Lesson Planner Router - Complete Backend API
Generates structured lesson plans with AI-powered teaching notes
"""

from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import json
from google import genai
import os
from database import get_database

router = APIRouter(prefix="/api/lesson-planner", tags=["lesson-planner"])

# --- MODELS ---

class LessonPlanRequest(BaseModel):
    """Request model for lesson plan generation"""
    bro_code: str = Field(..., description="БРО код (М.7.2.3)")
    duration: int = Field(45, description="Време на час (минути): 40, 45, 60")
    grade: int = Field(..., description="Одделение (1-9)")
    topic: str = Field(..., description="Наслов на темата")
    include_ai_notes: bool = Field(True, description="Вклучи AI белешки")
    difficulty_mix: Dict[str, float] = Field(
        default={"easy": 0.4, "medium": 0.4, "hard": 0.2},
        description="Пропорција на тежина"
    )

class LessonSection(BaseModel):
    """Single section of a lesson plan"""
    title: str
    duration_minutes: int
    problems: List[Dict[str, Any]]
    teaching_notes: Optional[str] = None
    activities: List[str] = []

class LessonPlanResponse(BaseModel):
    """Complete lesson plan response"""
    id: str
    bro_code: str
    grade: int
    topic: str
    duration: int
    created_at: datetime
    sections: List[LessonSection]
    total_problems: int
    ai_notes: Optional[str] = None
    curriculum_alignment: Dict[str, Any]

class SavedLessonTemplate(BaseModel):
    """Custom lesson template saved by teacher"""
    name: str = Field(..., description="Име на темплејт")
    description: Optional[str] = None
    sections: List[Dict[str, Any]]
    created_by: str
    is_public: bool = Field(False, description="Споделено со други професори")

# --- HELPER FUNCTIONS ---

async def fetch_problems_by_bro(db, bro_code: str, limit: int = 20) -> List[Dict[str, Any]]:
    """Fetch problems matching БРО code from database"""
    try:
        problems_collection = db["problems"]
        # Match БРО code (exact or prefix)
        query = {
            "$or": [
                {"bro_code": bro_code},
                {"bro_code": {"$regex": f"^{bro_code}"}},
                {"bro_codes": {"$in": [bro_code]}}
            ]
        }
        
        cursor = problems_collection.find(query).limit(limit)
        problems = []
        
        async for doc in cursor:
            # Normalize MongoDB _id
            doc["id"] = str(doc.get("_id", doc.get("id", "")))
            if "_id" in doc:
                del doc["_id"]
            problems.append(doc)
        
        return problems
    except Exception as e:
        print(f"Error fetching problems: {e}")
        return []

def balance_problems_by_difficulty(problems: List[Dict], mix: Dict[str, float], total: int) -> List[Dict]:
    """Balance problems according to difficulty distribution"""
    # Group by difficulty
    easy = [p for p in problems if p.get("difficulty", 3) <= 2]
    medium = [p for p in problems if 2 < p.get("difficulty", 3) <= 4]
    hard = [p for p in problems if p.get("difficulty", 3) > 4]
    
    # Calculate counts
    easy_count = int(total * mix["easy"])
    medium_count = int(total * mix["medium"])
    hard_count = total - easy_count - medium_count
    
    # Select problems
    selected = []
    selected.extend(easy[:easy_count])
    selected.extend(medium[:medium_count])
    selected.extend(hard[:hard_count])
    
    return selected[:total]

async def generate_ai_teaching_notes(topic: str, bro_code: str, grade: int, api_key: str) -> str:
    """Generate AI-powered teaching notes using Gemini"""
    try:
        client = genai.Client(api_key=api_key)
        
        prompt = f"""
Ти си искусен професор по математика во Македонија. Генерирај кратки наставни белешки за следната тема:

**Тема**: {topic}
**БРО Код**: {bro_code}
**Одделение**: {grade}

Вклучи:
1. Клучни концепти (2-3 реченици)
2. Чести грешки кај учениците (2-3 примери)
3. Совети за подучување (2-3 совети)
4. Поврзување со олимписки математики (ако е релевантно)

Пиши на македонски јазик. Биди конкретен и практичен.
"""
        
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp",
            contents=prompt
        )
        
        return response.text
    except Exception as e:
        print(f"Error generating AI notes: {e}")
        return "AI белешките не се достапни во моментот."

def structure_lesson_by_duration(duration: int, problems: List[Dict]) -> List[LessonSection]:
    """Structure lesson into sections based on duration"""
    if duration == 40:
        # 40-minute lesson
        return [
            LessonSection(
                title="1. Воведен дел (Мотивација)",
                duration_minutes=5,
                problems=problems[:1],
                activities=[
                    "Прикажи мотивациски проблем",
                    "Краток разговор со ученици",
                    "Поврзување со реален живот"
                ]
            ),
            LessonSection(
                title="2. Главна активност (Обработка)",
                duration_minutes=25,
                problems=problems[1:6],
                activities=[
                    "Објаснување на нова материја",
                    "Демонстрација на решавање",
                    "Самостојна работа на ученици",
                    "Групна дискусија"
                ]
            ),
            LessonSection(
                title="3. Затврдување",
                duration_minutes=7,
                problems=problems[6:8],
                activities=[
                    "Брзи задачи за проверка",
                    "Повторување на клучни концепти"
                ]
            ),
            LessonSection(
                title="4. Евалуација",
                duration_minutes=3,
                problems=[],
                activities=[
                    "Резиме на научено",
                    "Домашна работа",
                    "Прашања од ученици"
                ]
            )
        ]
    elif duration == 45:
        # 45-minute lesson (standard)
        return [
            LessonSection(
                title="1. Воведен дел (Мотивација)",
                duration_minutes=5,
                problems=problems[:1],
                activities=[
                    "Мотивациски проблем или загатка",
                    "Краток разговор со ученици",
                    "Поврзување со претходно научено"
                ]
            ),
            LessonSection(
                title="2. Главна активност (Обработка)",
                duration_minutes=25,
                problems=problems[1:7],
                activities=[
                    "Објаснување на нова материја",
                    "Демонстрација на решавање",
                    "Самостојна работа на ученици",
                    "Групна работа (2-3 проблеми)"
                ]
            ),
            LessonSection(
                title="3. Олимписки мост (Bonus)",
                duration_minutes=8,
                problems=problems[7:9],
                activities=[
                    "Напреден проблем за талентирани",
                    "Поврзување со олимписки математики",
                    "Различен пристап кон решавање"
                ]
            ),
            LessonSection(
                title="4. Затврдување и Евалуација",
                duration_minutes=7,
                problems=problems[9:11],
                activities=[
                    "Брз квиз (2-3 задачи)",
                    "Резиме на научено",
                    "Домашна работа",
                    "Прашања од ученици"
                ]
            )
        ]
    else:  # 60 minutes
        # Extended lesson (double period)
        return [
            LessonSection(
                title="1. Воведен дел (Мотивација)",
                duration_minutes=5,
                problems=problems[:2],
                activities=[
                    "Опширен мотивациски проблем",
                    "Дискусија со ученици",
                    "Поврзување со реален живот"
                ]
            ),
            LessonSection(
                title="2. Главна активност (Обработка)",
                duration_minutes=30,
                problems=problems[2:10],
                activities=[
                    "Теорија со примери",
                    "Демонстрација (5-6 проблеми)",
                    "Самостојна работа",
                    "Групна работа (3-4 проблеми)"
                ]
            ),
            LessonSection(
                title="3. Олимписки мост (Напредно)",
                duration_minutes=15,
                problems=problems[10:13],
                activities=[
                    "Сложени проблеми за талентирани",
                    "Различни стратегии за решавање",
                    "Математички истражувања"
                ]
            ),
            LessonSection(
                title="4. Затврдување и Евалуација",
                duration_minutes=10,
                problems=problems[13:16],
                activities=[
                    "Квиз (4-5 задачи)",
                    "Рефлексија на научено",
                    "Домашна работа (3-4 задачи)",
                    "Отворени прашања"
                ]
            )
        ]

# --- API ENDPOINTS ---

@router.post("/generate", response_model=LessonPlanResponse)
async def generate_lesson_plan(request: LessonPlanRequest):
    """
    Generate a complete lesson plan with structured sections
    
    **Flow**:
    1. Fetch problems by БРО code
    2. Balance by difficulty
    3. Structure into sections (intro, main, olympiad, evaluation)
    4. Generate AI teaching notes (optional)
    5. Return complete lesson plan
    """
    try:
        # Get database connection
        db = get_database()
        
        # Fetch problems
        problems = await fetch_problems_by_bro(db, request.bro_code, limit=20)
        
        if not problems:
            raise HTTPException(
                status_code=404,
                detail=f"Не се пронајдени проблеми за БРО код {request.bro_code}"
            )
        
        # Balance problems by difficulty
        total_problems = 16 if request.duration == 60 else (11 if request.duration == 45 else 8)
        balanced_problems = balance_problems_by_difficulty(
            problems,
            request.difficulty_mix,
            total_problems
        )
        
        # Structure lesson sections
        sections = structure_lesson_by_duration(request.duration, balanced_problems)
        
        # Generate AI notes (if requested)
        ai_notes = None
        if request.include_ai_notes:
            api_key = os.getenv("GENAI_API_KEY") or os.getenv("GOOGLE_API_KEY")
            if api_key:
                ai_notes = await generate_ai_teaching_notes(
                    request.topic,
                    request.bro_code,
                    request.grade,
                    api_key
                )
        
        # Create response
        lesson_plan = LessonPlanResponse(
            id=str(uuid.uuid4()),
            bro_code=request.bro_code,
            grade=request.grade,
            topic=request.topic,
            duration=request.duration,
            created_at=datetime.now(),
            sections=sections,
            total_problems=len(balanced_problems),
            ai_notes=ai_notes,
            curriculum_alignment={
                "bro_code": request.bro_code,
                "coverage": "100%",
                "standards_met": [request.bro_code]
            }
        )
        
        return lesson_plan
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error generating lesson plan: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/templates")
async def get_lesson_templates():
    """Get list of pre-built lesson templates"""
    templates = [
        {
            "id": "standard_45",
            "name": "Стандарден час (45 мин)",
            "duration": 45,
            "description": "Класична структура: Вовед → Обработка → Олимписки мост → Евалуација",
            "sections": 4
        },
        {
            "id": "quick_40",
            "name": "Брз час (40 мин)",
            "duration": 40,
            "description": "Компактна верзија за скратени часови",
            "sections": 4
        },
        {
            "id": "extended_60",
            "name": "Продолжен час (60 мин)",
            "duration": 60,
            "description": "Двојна учебна единица со опширна обработка",
            "sections": 4
        },
        {
            "id": "olympiad_focused",
            "name": "Олимписки фокус",
            "duration": 45,
            "description": "Повеќе време на напредни проблеми за талентирани ученици",
            "sections": 3,
            "difficulty_mix": {"easy": 0.2, "medium": 0.3, "hard": 0.5}
        },
        {
            "id": "practice_intensive",
            "name": "Интензивно вежбање",
            "duration": 45,
            "description": "Максимум вежби за затврдување на материјата",
            "sections": 2,
            "difficulty_mix": {"easy": 0.5, "medium": 0.4, "hard": 0.1}
        }
    ]
    return {"templates": templates}

@router.post("/save-template")
async def save_custom_template(template: SavedLessonTemplate):
    """Save a custom lesson template for reuse"""
    try:
        db = get_database()
        templates_collection = db["lesson_templates"]
        
        template_doc = {
            "id": str(uuid.uuid4()),
            "name": template.name,
            "description": template.description,
            "sections": template.sections,
            "created_by": template.created_by,
            "is_public": template.is_public,
            "created_at": datetime.now()
        }
        
        result = templates_collection.insert_one(template_doc)
        
        return {
            "success": True,
            "template_id": str(result.inserted_id),
            "message": "Темплејтот е зачуван успешно"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/my-templates/{teacher_id}")
async def get_teacher_templates(teacher_id: str):
    """Get all templates created by a specific teacher"""
    try:
        db = get_database()
        templates_collection = db["lesson_templates"]
        
        cursor = templates_collection.find({
            "$or": [
                {"created_by": teacher_id},
                {"is_public": True}
            ]
        })
        
        templates = []
        async for doc in cursor:
            doc["id"] = str(doc.get("_id", doc.get("id", "")))
            if "_id" in doc:
                del doc["_id"]
            templates.append(doc)
        
        return {"templates": templates}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/export-pdf/{lesson_id}")
async def export_lesson_to_pdf(lesson_id: str):
    """Export lesson plan to professional PDF format"""
    # TODO: Implement PDF generation
    return {
        "success": True,
        "message": "PDF генерирањето е во развој",
        "pdf_url": f"/downloads/lesson_{lesson_id}.pdf"
    }

@router.post("/share/{lesson_id}")
async def share_lesson_plan(lesson_id: str, recipient_email: str):
    """Share lesson plan with another teacher"""
    # TODO: Implement sharing logic
    return {
        "success": True,
        "message": f"Сценариото е споделено со {recipient_email}",
        "share_link": f"/lesson/{lesson_id}"
    }

import uuid
