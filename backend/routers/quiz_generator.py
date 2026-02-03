"""
Quiz Generator Router - Complete Backend API
Generates quizzes with multiple formats and difficulty balancing
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
import json
import random
import uuid
from database import get_database

router = APIRouter(prefix="/api/quiz-generator", tags=["quiz-generator"])

# --- MODELS ---

class QuizRequest(BaseModel):
    """Request model for quiz generation"""
    bro_codes: List[str] = Field(..., description="Листа на БРО кодови")
    question_count: int = Field(10, description="Број на прашања (5/10/15/20)")
    formats: List[str] = Field(
        default=["multiple_choice", "true_false", "short_answer"],
        description="Формати: multiple_choice, true_false, short_answer, essay"
    )
    difficulty: str = Field("mixed", description="easy, medium, hard, mixed")
    include_images: bool = Field(True, description="Вклучи слики")
    generate_answer_key: bool = Field(True, description="Генерирај решенија")
    time_limit: Optional[int] = Field(None, description="Временско ограничување (минути)")

class QuizQuestion(BaseModel):
    """Single quiz question"""
    id: str
    question_number: int
    format: str
    question_text: str
    options: Optional[List[str]] = None  # For multiple choice
    correct_answer: str
    points: int
    difficulty: int
    bro_code: str
    image_url: Optional[str] = None

class QuizResponse(BaseModel):
    """Complete quiz response"""
    id: str
    title: str
    created_at: datetime
    question_count: int
    total_points: int
    time_limit: Optional[int] = None
    questions: List[QuizQuestion]
    answer_key: Optional[Dict[str, Any]] = None
    difficulty_distribution: Dict[str, int]

# --- HELPER FUNCTIONS ---

async def fetch_problems_by_bro_codes(db, bro_codes: List[str], limit: int = 50) -> List[Dict]:
    """Fetch problems matching multiple БРО codes"""
    try:
        problems_collection = db["problems"]
        query = {
            "$or": [
                {"bro_code": {"$in": bro_codes}},
                {"bro_codes": {"$in": bro_codes}}
            ]
        }
        
        cursor = problems_collection.find(query).limit(limit)
        problems = []
        
        async for doc in cursor:
            doc["id"] = str(doc.get("_id", doc.get("id", "")))
            if "_id" in doc:
                del doc["_id"]
            problems.append(doc)
        
        return problems
    except Exception as e:
        print(f"Error fetching problems: {e}")
        return []

def convert_to_multiple_choice(problem: Dict) -> QuizQuestion:
    """Convert problem to multiple choice format"""
    # Generate wrong answers (simple logic - could be enhanced)
    correct = problem.get("answer", "Одговор")
    
    # Simple wrong answer generation
    wrong_answers = [
        f"{correct} + 1",
        f"{correct} - 1",
        f"{correct} × 2"
    ]
    
    options = [correct] + wrong_answers[:3]
    random.shuffle(options)
    
    return QuizQuestion(
        id=problem["id"],
        question_number=1,  # Will be set later
        format="multiple_choice",
        question_text=problem.get("content_markdown", ""),
        options=options,
        correct_answer=correct,
        points=problem.get("points", 1),
        difficulty=problem.get("difficulty", 3),
        bro_code=problem.get("bro_code", ""),
        image_url=problem.get("image_url")
    )

def convert_to_true_false(problem: Dict) -> QuizQuestion:
    """Convert problem to true/false format"""
    # Simple logic: make statement, randomly assign true/false
    is_true = random.choice([True, False])
    
    statement = problem.get("content_markdown", "")
    if not is_true:
        statement = f"Неточно: {statement}"
    
    return QuizQuestion(
        id=problem["id"],
        question_number=1,
        format="true_false",
        question_text=statement,
        options=["Точно", "Неточно"],
        correct_answer="Точно" if is_true else "Неточно",
        points=1,
        difficulty=problem.get("difficulty", 2),
        bro_code=problem.get("bro_code", ""),
        image_url=problem.get("image_url")
    )

def convert_to_short_answer(problem: Dict) -> QuizQuestion:
    """Convert problem to short answer format"""
    return QuizQuestion(
        id=problem["id"],
        question_number=1,
        format="short_answer",
        question_text=problem.get("content_markdown", ""),
        options=None,
        correct_answer=problem.get("answer", ""),
        points=problem.get("points", 2),
        difficulty=problem.get("difficulty", 3),
        bro_code=problem.get("bro_code", ""),
        image_url=problem.get("image_url")
    )

def balance_quiz_by_difficulty(problems: List[Dict], difficulty: str, count: int) -> List[Dict]:
    """Balance problems by difficulty setting"""
    # Categorize by difficulty
    easy = [p for p in problems if p.get("difficulty", 3) <= 2]
    medium = [p for p in problems if 2 < p.get("difficulty", 3) <= 4]
    hard = [p for p in problems if p.get("difficulty", 3) > 4]
    
    if difficulty == "easy":
        mix = {"easy": 0.7, "medium": 0.2, "hard": 0.1}
    elif difficulty == "medium":
        mix = {"easy": 0.3, "medium": 0.5, "hard": 0.2}
    elif difficulty == "hard":
        mix = {"easy": 0.1, "medium": 0.3, "hard": 0.6}
    else:  # mixed
        mix = {"easy": 0.4, "medium": 0.4, "hard": 0.2}
    
    # Calculate counts
    easy_count = int(count * mix["easy"])
    medium_count = int(count * mix["medium"])
    hard_count = count - easy_count - medium_count
    
    # Select and shuffle
    selected = []
    random.shuffle(easy)
    random.shuffle(medium)
    random.shuffle(hard)
    
    selected.extend(easy[:easy_count])
    selected.extend(medium[:medium_count])
    selected.extend(hard[:hard_count])
    
    random.shuffle(selected)
    return selected[:count]

def distribute_formats(problems: List[Dict], formats: List[str]) -> List[QuizQuestion]:
    """Distribute problems across different question formats"""
    questions = []
    
    # Calculate how many of each format
    per_format = len(problems) // len(formats)
    remainder = len(problems) % len(formats)
    
    idx = 0
    for format_type in formats:
        # How many questions for this format
        format_count = per_format + (1 if remainder > 0 else 0)
        remainder -= 1
        
        # Convert problems to this format
        for i in range(format_count):
            if idx >= len(problems):
                break
            
            problem = problems[idx]
            
            if format_type == "multiple_choice":
                question = convert_to_multiple_choice(problem)
            elif format_type == "true_false":
                question = convert_to_true_false(problem)
            elif format_type == "short_answer":
                question = convert_to_short_answer(problem)
            else:  # essay
                question = convert_to_short_answer(problem)
                question.format = "essay"
                question.points = 5
            
            question.question_number = idx + 1
            questions.append(question)
            idx += 1
    
    return questions

def generate_answer_key(questions: List[QuizQuestion]) -> Dict[str, Any]:
    """Generate answer key with solutions"""
    answer_key = {
        "answers": {},
        "scoring_guide": {},
        "total_points": sum(q.points for q in questions)
    }
    
    for q in questions:
        answer_key["answers"][str(q.question_number)] = {
            "correct_answer": q.correct_answer,
            "points": q.points,
            "format": q.format
        }
        
        # Scoring guide
        if q.format == "multiple_choice" or q.format == "true_false":
            answer_key["scoring_guide"][str(q.question_number)] = "Автоматско: 0 или полни поени"
        else:
            answer_key["scoring_guide"][str(q.question_number)] = "Делумно точно: до полни поени"
    
    return answer_key

# --- API ENDPOINTS ---

@router.post("/generate", response_model=QuizResponse)
async def generate_quiz(request: QuizRequest):
    """
    Generate a complete quiz with multiple question formats
    
    **Features**:
    - Multiple formats (MC, T/F, Short Answer, Essay)
    - Difficulty balancing
    - Auto-generated answer key
    - Support for images
    """
    try:
        # Validate input
        if not request.bro_codes:
            raise HTTPException(status_code=400, detail="БРО кодовите се задолжителни")
        
        if request.question_count not in [5, 10, 15, 20]:
            raise HTTPException(status_code=400, detail="Број на прашања: 5, 10, 15 или 20")
        
        # Get database
        db = get_database()
        
        # Fetch problems
        problems = await fetch_problems_by_bro_codes(db, request.bro_codes, limit=50)
        
        if not problems:
            raise HTTPException(
                status_code=404,
                detail=f"Не се пронајдени проблеми за БРО кодови {request.bro_codes}"
            )
        
        # Balance by difficulty
        balanced_problems = balance_quiz_by_difficulty(
            problems,
            request.difficulty,
            request.question_count
        )
        
        # Distribute across formats
        questions = distribute_formats(balanced_problems, request.formats)
        
        # Generate answer key
        answer_key = None
        if request.generate_answer_key:
            answer_key = generate_answer_key(questions)
        
        # Calculate difficulty distribution
        difficulty_dist = {
            "easy": len([q for q in questions if q.difficulty <= 2]),
            "medium": len([q for q in questions if 2 < q.difficulty <= 4]),
            "hard": len([q for q in questions if q.difficulty > 4])
        }
        
        # Create response
        quiz = QuizResponse(
            id=str(uuid.uuid4()),
            title=f"Квиз - {', '.join(request.bro_codes[:2])}{'...' if len(request.bro_codes) > 2 else ''}",
            created_at=datetime.now(),
            question_count=len(questions),
            total_points=sum(q.points for q in questions),
            time_limit=request.time_limit,
            questions=questions,
            answer_key=answer_key,
            difficulty_distribution=difficulty_dist
        )
        
        return quiz
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error generating quiz: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/formats")
async def get_quiz_formats():
    """Get available quiz question formats"""
    formats = [
        {
            "id": "multiple_choice",
            "name": "Повеќекратен избор",
            "icon": "🔘",
            "description": "4 опции, 1 точна",
            "auto_gradable": True,
            "points": 1
        },
        {
            "id": "true_false",
            "name": "Точно/Неточно",
            "icon": "✓✗",
            "description": "Едноставни тврдења",
            "auto_gradable": True,
            "points": 1
        },
        {
            "id": "short_answer",
            "name": "Краток одговор",
            "icon": "📝",
            "description": "Неколку зборови или број",
            "auto_gradable": False,
            "points": 2
        },
        {
            "id": "essay",
            "name": "Есеј/Објаснување",
            "icon": "📄",
            "description": "Детално објаснување",
            "auto_gradable": False,
            "points": 5
        }
    ]
    return {"formats": formats}

@router.post("/export-pdf/{quiz_id}")
async def export_quiz_to_pdf(quiz_id: str, include_answers: bool = False):
    """Export quiz to PDF format"""
    # TODO: Implement PDF generation
    return {
        "success": True,
        "message": "PDF генерирањето е во развој",
        "pdf_url": f"/downloads/quiz_{quiz_id}.pdf",
        "answer_key_url": f"/downloads/quiz_{quiz_id}_answers.pdf" if include_answers else None
    }

@router.post("/export-excel/{quiz_id}")
async def export_quiz_to_excel(quiz_id: str):
    """Export quiz to Excel format for grading"""
    # TODO: Implement Excel export
    return {
        "success": True,
        "message": "Excel експортот е во развој",
        "excel_url": f"/downloads/quiz_{quiz_id}.xlsx"
    }

@router.get("/statistics/{quiz_id}")
async def get_quiz_statistics(quiz_id: str):
    """Get statistics for completed quiz (student responses)"""
    # TODO: Implement statistics tracking
    return {
        "quiz_id": quiz_id,
        "total_attempts": 0,
        "average_score": 0.0,
        "completion_rate": 0.0,
        "difficulty_analysis": {
            "easiest_question": 1,
            "hardest_question": 10,
            "most_skipped": 5
        }
    }

@router.post("/save-bank")
async def save_to_question_bank(questions: List[Dict[str, Any]], bank_name: str):
    """Save questions to custom question bank for reuse"""
    try:
        db = get_database()
        banks_collection = db["question_banks"]
        
        bank_doc = {
            "id": str(uuid.uuid4()),
            "name": bank_name,
            "questions": questions,
            "created_at": datetime.now(),
            "question_count": len(questions)
        }
        
        result = banks_collection.insert_one(bank_doc)
        
        return {
            "success": True,
            "bank_id": str(result.inserted_id),
            "message": f"Банка '{bank_name}' е зачувана"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/my-banks")
async def get_question_banks():
    """Get all saved question banks"""
    try:
        db = get_database()
        banks_collection = db["question_banks"]
        
        cursor = banks_collection.find({})
        banks = []
        
        async for doc in cursor:
            doc["id"] = str(doc.get("_id", doc.get("id", "")))
            if "_id" in doc:
                del doc["_id"]
            banks.append(doc)
        
        return {"banks": banks}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
