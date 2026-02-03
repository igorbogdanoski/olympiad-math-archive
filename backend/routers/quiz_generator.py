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

# ====================
# LIVE QUIZ ENDPOINTS
# ====================

class LiveQuizCreate(BaseModel):
    """Create a live quiz session"""
    teacher_id: str
    quiz_title: str
    bro_codes: List[str]
    question_count: int = 10
    time_limit: int = 45
    formats: List[str] = ["multiple_choice", "true_false"]

class JoinRequest(BaseModel):
    """Student joins quiz lobby"""
    access_code: str
    student_name: str

class StudentAnswer(BaseModel):
    """Single answer from student"""
    problem_id: str
    selected_option: str
    time_spent: int = 0

class SubmissionRequest(BaseModel):
    """Complete quiz submission"""
    access_code: str
    student_name: str
    answers: List[StudentAnswer]

def generate_access_code(length: int = 6) -> str:
    """Generate random 6-character code"""
    import string
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

@router.post("/live/create")
async def create_live_quiz(quiz_data: LiveQuizCreate):
    """Create live quiz and generate access code"""
    try:
        db = get_database()
        
        # Generate unique access code
        access_code = generate_access_code()
        quizzes_collection = db["live_quizzes"]
        
        # Check for collision (unlikely but possible)
        while await quizzes_collection.find_one({"access_code": access_code}):
            access_code = generate_access_code()
        
        # Fetch problems
        problems = await fetch_problems_by_bro_codes(db, quiz_data.bro_codes, quiz_data.question_count * 2)
        
        if not problems:
            raise HTTPException(status_code=404, detail="Нема пронајдено задачи за избраните БРО кодови")
        
        # Balance and format questions
        balanced = balance_quiz_by_difficulty(problems, "mixed", quiz_data.question_count)
        formatted_questions = []
        
        for idx, prob in enumerate(balanced, 1):
            # Convert to multiple choice by default
            format_type = random.choice(quiz_data.formats)
            
            if format_type == "multiple_choice":
                question = convert_to_multiple_choice(prob)
            elif format_type == "true_false":
                question = convert_to_true_false(prob)
            else:
                question = convert_to_short_answer(prob)
            
            question.question_number = idx
            formatted_questions.append(question.dict())
        
        # Create quiz document
        quiz_doc = {
            "access_code": access_code,
            "teacher_id": quiz_data.teacher_id,
            "title": quiz_data.quiz_title,
            "time_limit": quiz_data.time_limit,
            "questions": formatted_questions,
            "participants": [],  # Students who joined
            "status": "active",
            "created_at": datetime.now()
        }
        
        result = await quizzes_collection.insert_one(quiz_doc)
        
        return {
            "quiz_id": str(result.inserted_id),
            "access_code": access_code,
            "question_count": len(formatted_questions),
            "message": f"Live квиз креиран! Код: {access_code}"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/live/join")
async def join_live_quiz(data: JoinRequest):
    """Student joins quiz lobby"""
    try:
        db = get_database()
        quizzes_collection = db["live_quizzes"]
        
        # Find quiz
        quiz = await quizzes_collection.find_one({"access_code": data.access_code.upper()})
        
        if not quiz:
            raise HTTPException(status_code=404, detail="Невалиден код за квиз")
        
        if quiz.get("status") != "active":
            raise HTTPException(status_code=403, detail="Квизот е затворен")
        
        # Add student to participants
        await quizzes_collection.update_one(
            {"_id": quiz["_id"]},
            {"$addToSet": {"participants": data.student_name}}
        )
        
        return {"status": "joined", "message": f"{data.student_name} се приклучи"}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/live/access/{access_code}")
async def get_quiz_for_student(access_code: str):
    """Get quiz questions for student (NO ANSWERS!)"""
    try:
        db = get_database()
        quizzes_collection = db["live_quizzes"]
        
        quiz = await quizzes_collection.find_one({"access_code": access_code.upper()})
        
        if not quiz:
            raise HTTPException(status_code=404, detail="Невалиден код")
        
        if quiz.get("status") != "active":
            raise HTTPException(status_code=403, detail="Квизот е затворен")
        
        # SECURITY: Remove correct answers from response
        sanitized_questions = []
        for q in quiz["questions"]:
            safe_q = {
                "id": q["id"],
                "question_number": q["question_number"],
                "format": q["format"],
                "question_text": q["question_text"],
                "options": q.get("options"),
                "points": q["points"],
                "bro_code": q["bro_code"],
                "image_url": q.get("image_url")
            }
            # NEVER include correct_answer here!
            sanitized_questions.append(safe_q)
        
        return {
            "title": quiz["title"],
            "time_limit": quiz["time_limit"],
            "question_count": len(sanitized_questions),
            "questions": sanitized_questions
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/live/submit")
async def submit_live_quiz(submission: SubmissionRequest):
    """Auto-grade and save submission"""
    try:
        db = get_database()
        quizzes_collection = db["live_quizzes"]
        submissions_collection = db["quiz_submissions"]
        
        # Get quiz with answers
        quiz = await quizzes_collection.find_one({"access_code": submission.access_code.upper()})
        
        if not quiz:
            raise HTTPException(status_code=404, detail="Квиз не е пронајден")
        
        # Create answer key
        answer_key = {q["id"]: q["correct_answer"] for q in quiz["questions"]}
        points_map = {q["id"]: q["points"] for q in quiz["questions"]}
        
        # ⚡ GAMIFICATION: Speed Bonus Scoring (Kahoot-style)
        total_score = 0
        max_possible_score = 0  # Dynamic max based on perfect speed
        correct_count = 0
        current_streak = 0
        max_streak = 0
        graded = []
        
        for ans in submission.answers:
            is_correct = False
            base_points = points_map.get(ans.problem_id, 0)
            
            # Max possible = base points × 2 (if answered instantly)
            max_possible_score += (base_points * 2)
            
            correct_val = answer_key.get(ans.problem_id, "")
            student_val = ans.selected_option.strip()
            
            # Simple comparison (case-insensitive)
            if correct_val and str(correct_val).strip().lower() == student_val.lower():
                is_correct = True
                correct_count += 1
                current_streak += 1
                if current_streak > max_streak:
                    max_streak = current_streak
                
                # ⚡ SPEED BONUS FORMULA
                # Time Factor: 1.0 (instant) to 0.5 (slow)
                time_limit_per_q = 30  # 30 seconds is "slow" threshold
                time_taken = min(ans.time_spent, time_limit_per_q)
                
                # Formula: factor = 1 - (time / (2 * limit))
                # 0 sec -> factor 1.0 -> 200% points
                # 15 sec -> factor 0.75 -> 150% points  
                # 30 sec -> factor 0.5 -> 100% points
                time_factor = 1 - (time_taken / (2 * time_limit_per_q))
                
                earned_points = int(base_points * 2 * time_factor)
                total_score += earned_points
                
            else:
                current_streak = 0  # Reset streak
                earned_points = 0
            
            graded.append({
                "problem_id": ans.problem_id,
                "student_answer": student_val,
                "correct_answer": correct_val,
                "is_correct": is_correct,
                "points_earned": earned_points,
                "time_spent": ans.time_spent
            })
        
        # Save submission
        submission_doc = {
            "quiz_id": str(quiz["_id"]),
            "access_code": submission.access_code.upper(),
            "student_name": submission.student_name,
            "answers": graded,
            "total_score": total_score,
            "max_score": max_possible_score,
            "correct_count": correct_count,
            "streak": max_streak,
            "submitted_at": datetime.now()
        }
        
        await submissions_collection.insert_one(submission_doc)
        
        percentage = (total_score / max_possible_score * 100) if max_possible_score > 0 else 0
        
        # 🔥 Dynamic feedback with streak info
        feedback = f"Браво {submission.student_name}!"
        if max_streak >= 5:
            feedback += f" 🔥 Невероватен Streak: {max_streak}!"
        elif max_streak >= 3:
            feedback += f" ⚡ Одличен Streak: {max_streak}!"
        feedback += f" Освои {total_score}/{max_possible_score} поени ({percentage:.1f}%)"
        
        return {
            "score": total_score,
            "max_score": max_possible_score,
            "correct_count": correct_count,
            "total_questions": len(quiz["questions"]),
            "percentage": round(percentage, 1),
            "streak": max_streak,
            "feedback": feedback
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/live/{quiz_id}/stats")
async def get_live_stats(quiz_id: str):
    """Real-time stats for teacher dashboard"""
    try:
        from bson import ObjectId
        
        db = get_database()
        quizzes_collection = db["live_quizzes"]
        submissions_collection = db["quiz_submissions"]
        
        # Get quiz
        quiz = await quizzes_collection.find_one({"_id": ObjectId(quiz_id)})
        
        if not quiz:
            raise HTTPException(status_code=404, detail="Квиз не е пронајден")
        
        # Get submissions
        cursor = submissions_collection.find({"quiz_id": quiz_id})
        submissions = []
        async for doc in cursor:
            submissions.append(doc)
        
        # Build student list
        participants = quiz.get("participants", [])
        finished_names = {s["student_name"] for s in submissions}
        
        students = []
        for name in participants:
            sub = next((s for s in submissions if s["student_name"] == name), None)
            
            students.append({
                "name": name,
                "status": "finished" if sub else "working",
                "score": sub["total_score"] if sub else 0,
                "max_score": sub["max_score"] if sub else 0,
                "percentage": round(sub["total_score"] / sub["max_score"] * 100, 1) if sub else 0
            })
        
        # Sort by score (finished first)
        students.sort(key=lambda x: (x["status"] == "finished", x["score"]), reverse=True)
        
        return {
            "access_code": quiz["access_code"],
            "title": quiz["title"],
            "total_participants": len(participants),
            "finished_count": len(submissions),
            "students": students,
            "avg_score": sum(s["score"] for s in students if s["status"] == "finished") / len(submissions) if submissions else 0
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
