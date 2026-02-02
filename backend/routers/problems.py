"""
Problems Router - API endpoints за работа со задачи
"""
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from database import get_database
from bson import ObjectId

router = APIRouter()


@router.get("/problems")
async def get_problems(
    ids: Optional[str] = Query(None, description="Comma-separated problem IDs"),
    grade: Optional[int] = Query(None, description="Filter by grade (2-9)"),
    subject: Optional[str] = Query(None, description="Filter by subject"),
    difficulty: Optional[str] = Query(None, description="Filter by difficulty"),
    limit: Optional[int] = Query(100, description="Maximum number of problems to return")
):
    """
    Get problems by IDs or filters
    
    Examples:
    - /api/problems?ids=1,2,3
    - /api/problems?grade=5&subject=algebra
    - /api/problems?difficulty=medium&limit=20
    """
    db = get_database()
    if db is None:
        raise HTTPException(status_code=503, detail="Базата не е достапна")
    
    # Build query
    query = {}
    
    # Filter by IDs if provided
    if ids:
        try:
            problem_ids = [int(id.strip()) for id in ids.split(",")]
            query["id"] = {"$in": problem_ids}
        except ValueError:
            raise HTTPException(status_code=400, detail="Invalid problem IDs format")
    
    # Add other filters
    if grade:
        query["grade"] = grade
    if subject:
        query["subject"] = subject
    if difficulty:
        query["difficulty"] = difficulty
    
    # Execute query
    try:
        problems = list(db["problems"].find(query).limit(limit))
        
        # Convert ObjectId to string for JSON serialization
        for problem in problems:
            if "_id" in problem:
                problem["_id"] = str(problem["_id"])
        
        return {
            "count": len(problems),
            "problems": problems
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/problems/{problem_id}")
async def get_problem_by_id(problem_id: int):
    """
    Get a single problem by ID
    
    Example: /api/problems/123
    """
    db = get_database()
    if db is None:
        raise HTTPException(status_code=503, detail="Базата не е достапна")
    
    try:
        problem = db["problems"].find_one({"id": problem_id})
        
        if not problem:
            raise HTTPException(status_code=404, detail=f"Problem {problem_id} not found")
        
        # Convert ObjectId to string
        if "_id" in problem:
            problem["_id"] = str(problem["_id"])
        
        return problem
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/problems/search")
async def search_problems(
    q: str = Query(..., description="Search query"),
    limit: int = Query(50, description="Maximum results")
):
    """
    Search problems by text (title, content, tags)
    
    Example: /api/problems/search?q=геометрија&limit=20
    """
    db = get_database()
    if db is None:
        raise HTTPException(status_code=503, detail="Базата не е достапна")
    
    try:
        # Text search across multiple fields
        query = {
            "$or": [
                {"title": {"$regex": q, "$options": "i"}},
                {"content": {"$regex": q, "$options": "i"}},
                {"primary_skill": {"$regex": q, "$options": "i"}},
                {"subject": {"$regex": q, "$options": "i"}}
            ]
        }
        
        problems = list(db["problems"].find(query).limit(limit))
        
        # Convert ObjectId to string
        for problem in problems:
            if "_id" in problem:
                problem["_id"] = str(problem["_id"])
        
        return {
            "query": q,
            "count": len(problems),
            "problems": problems
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
