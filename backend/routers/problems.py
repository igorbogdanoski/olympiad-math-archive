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
    grade: Optional[str] = Query(None, description="Filter by grade (4-9, or 10-12)"),
    topic: Optional[str] = Query(None, description="Filter by topic (algebra, geometry, etc.)"),
    min_difficulty: Optional[int] = Query(None, description="Minimum difficulty (1-10)"),
    max_difficulty: Optional[int] = Query(None, description="Maximum difficulty (1-10)"),
    limit: Optional[int] = Query(100, description="Maximum number of problems to return")
):
    """
    Get problems by IDs or filters
    
    Examples:
    - /api/problems?ids=sigma_138_1874,sigma_137_1871
    - /api/problems?grade=5&topic=algebra
    - /api/problems?topic=geometry&min_difficulty=1&max_difficulty=5&limit=50
    """
    db = get_database()
    if db is None:
        raise HTTPException(status_code=503, detail="Базата не е достапна")
    
    # Build query
    query = {}
    
    # Filter by IDs if provided
    if ids:
        # IDs are strings like 'sigma_138_1874'
        problem_ids = [id.strip() for id in ids.split(",")]
        query["problem_id"] = {"$in": problem_ids}
    
    # Add other filters
    if grade:
        query["grade"] = grade
    if topic:
        query["topic"] = topic
    if min_difficulty is not None or max_difficulty is not None:
        query["difficulty"] = {}
        if min_difficulty is not None:
            query["difficulty"]["$gte"] = min_difficulty
        if max_difficulty is not None:
            query["difficulty"]["$lte"] = max_difficulty
    
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
async def get_problem_by_id(problem_id: str):
    """
    Get a single problem by ID
    
    Example: /api/problems/sigma_138_1874
    """
    db = get_database()
    if db is None:
        raise HTTPException(status_code=503, detail="Базата не е достапна")
    
    try:
        problem = db["problems"].find_one({"problem_id": problem_id})
        
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
