import os
import json
import re
import uuid
import google.generativeai as genai
from fastapi import APIRouter, HTTPException
from datetime import datetime
from database import get_database

router = APIRouter()

GENAI_API_KEY = os.getenv("GENAI_API_KEY")
if GENAI_API_KEY:
    genai.configure(api_key=GENAI_API_KEY)

@router.get("/dashboard/stats")
async def get_dashboard_stats():
    db = get_database()
    if db is None:
        return {"error": "Базата не е достапна"}
    
    # 1. Основна статистика
    total_problems = db["problems"].count_documents({})
    total_tests = db["test_instances"].count_documents({})
    
    # 2. Пресметка на покриеност
    covered_standards = len(db["problems"].distinct("primary_skill"))
    total_possible_standards = 391 
    coverage_percent = round((covered_standards / total_possible_standards) * 100, 1) if total_possible_standards > 0 else 0

    # 3. Последни активности (Тестови)
    recent_tests_cursor = db["test_instances"].find().sort("created_at", -1).limit(5)
    recent_tests = []
    for test in recent_tests_cursor:
        recent_tests.append({
            "id": test["_id"],
            "topic": test.get("topic", "Без наслов"),
            "grade": test.get("grade", "?"),
            "date": test["created_at"].strftime("%d.%m.%Y")
        })

    return {
        "stats": {
            "problems_count": total_problems,
            "tests_created": total_tests,
            "coverage_percent": coverage_percent
        },
        "recent_activity": recent_tests
    }

@router.get("/dashboard/recommendation")
async def get_ai_recommendation():
    db = get_database()
    if db is None: return {"error": "DB error"}
    
    # 1. Најди ги сите стандарди (кодови)
    # Земаме примерок од курикулумот
    curriculum_sample = db["curriculum"].find_one({}, {"themes": 1})
    if not curriculum_sample or "themes" not in curriculum_sample:
        return {"status": "complete", "message": "Нема податоци за курикулумот"}
    
    all_standards = []
    for theme in curriculum_sample["themes"]:
        if "standards_with_codes" in theme:
            for s in theme["standards_with_codes"]:
                all_standards.append({
                    "code": s["code"],
                    "description": s["description"],
                    "topic": theme["title"]
                })
    
    # 2. Најди ги покриените стандарди
    covered_codes = db["problems"].distinct("primary_skill")
    
    # 3. Најди ја првата "дупка"
    missing = [s for s in all_standards if s["code"] not in covered_codes]
    
    if not missing:
        return {"status": "complete", "message": "Програмата е 100% покриена!"}
    
    # Врати ја првата препорака
    recommended = missing[0]
    return {
        "status": "pending",
        "standard": recommended
    }

@router.post("/dashboard/fix-gap")
async def fix_gap(payload: dict):
    """
    Uses Gemini AI to generate new problems for a missing curriculum standard.
    """
    if not GENAI_API_KEY:
        raise HTTPException(status_code=500, detail="Gemini API Key not configured")

    db = get_database()
    code = payload.get("code")
    description = payload.get("description")
    topic = payload.get("topic")

    prompt = f"""
    You are an expert mathematics teacher. Generate 3 unique math problems for the following curriculum standard:
    Standard Code: {code}
    Topic: {topic}
    Description: {description}

    The problems must:
    1. Be written in Macedonian (Cyrillic).
    2. Include a clear 'title', 'content_markdown', and 'solution'.
    3. Be appropriate for the difficulty of this standard.
    4. Return the result as a JSON list of objects.

    Output ONLY valid JSON.
    """

    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(prompt)
        text = response.text
        
        # Extract JSON
        json_match = re.search(r'\[.*\]', text, re.DOTALL)
        if not json_match:
            return {"status": "error", "message": "AI failed to return valid JSON"}

        new_problems = json.loads(json_match.group(0))
        
        mongo_docs = []
        for p in new_problems:
            prob_id = f"ai-{uuid.uuid4().hex[:8]}"
            doc = {
                "problem_id": prob_id,
                "title": p.get("title", f"Проблем за {code}"),
                "content_markdown": p.get("content_markdown", ""),
                "topic": topic,
                "difficulty": 3,
                "grade": "unknown", # Could be inferred from code
                "primary_skill": code,
                "tags": ["ai-generated", code],
                "curriculum_codes": [code],
                "solution": p.get("solution", ""),
                "created_at": datetime.utcnow()
            }
            mongo_docs.append(doc)

        if mongo_docs:
            db["problems"].insert_many(mongo_docs)
            return {"status": "success", "message": f"Successfully generated and stored {len(mongo_docs)} problems for {code}"}
        
        return {"status": "error", "message": "No problems were generated"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
