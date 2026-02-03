"""
Worksheet Templates Configuration
Created: February 3, 2026
Purpose: Pre-defined worksheet templates for teachers
"""

TEMPLATES = {
    "standard_test": {
        "name": "Стандарден Тест",
        "name_en": "Standard Test",
        "problems": 20,
        "difficulty": {"easy": 0.3, "medium": 0.5, "hard": 0.2},
        "include_solutions": True,
        "time_limit": 45,
        "description": "Класичен тест со 20 задачи и одговори",
        "icon": "📝",
        "use_cases": ["Тестирање", "Оценување", "Месечна проверка"]
    },
    "quick_quiz": {
        "name": "Брза Проверка",
        "name_en": "Quick Quiz",
        "problems": 5,
        "difficulty": {"easy": 0.6, "medium": 0.4, "hard": 0.0},
        "include_solutions": False,
        "time_limit": 15,
        "description": "5 задачи за брза проверка на знаењето",
        "icon": "⚡",
        "use_cases": ["Воведен тест", "Брза проверка", "Загревање"]
    },
    "homework": {
        "name": "Домашна Задача",
        "name_en": "Homework Assignment",
        "problems": 10,
        "difficulty": {"easy": 0.4, "medium": 0.4, "hard": 0.2},
        "include_solutions": True,
        "time_limit": None,
        "description": "10 задачи за вежбање дома",
        "icon": "🏠",
        "use_cases": ["Домашна", "Вежбање", "Ревизија"]
    },
    "practice_sheet": {
        "name": "Вежба Лист",
        "name_en": "Practice Sheet",
        "problems": 30,
        "difficulty": {"easy": 0.4, "medium": 0.5, "hard": 0.1},
        "include_solutions": True,
        "time_limit": None,
        "description": "30 задачи групирани по тема за интензивна вежба",
        "icon": "💪",
        "use_cases": ["Интензивна вежба", "Подготовка за тест", "Групна работа"]
    },
    "mixed_review": {
        "name": "Мешана Ревизија",
        "name_en": "Mixed Review",
        "problems": 15,
        "difficulty": {"easy": 0.3, "medium": 0.5, "hard": 0.2},
        "include_solutions": True,
        "time_limit": 30,
        "description": "15 задачи од различни теми за ревизија",
        "icon": "🔄",
        "use_cases": ["Ревизија", "Крај на тема", "Подготовка за испит"]
    }
}


def get_template(template_id: str):
    """Get template by ID"""
    return TEMPLATES.get(template_id)


def get_all_templates():
    """Get all available templates"""
    return TEMPLATES


def calculate_problem_counts(template_id: str, total_problems: int = None):
    """
    Calculate how many problems of each difficulty level
    
    Args:
        template_id: Template identifier
        total_problems: Override default problem count
    
    Returns:
        dict: {easy: int, medium: int, hard: int}
    """
    template = get_template(template_id)
    if not template:
        return None
    
    count = total_problems or template["problems"]
    difficulty = template["difficulty"]
    
    easy_count = int(count * difficulty["easy"])
    medium_count = int(count * difficulty["medium"])
    hard_count = count - easy_count - medium_count  # Ensure total is exact
    
    return {
        "easy": easy_count,
        "medium": medium_count,
        "hard": hard_count,
        "total": count
    }
