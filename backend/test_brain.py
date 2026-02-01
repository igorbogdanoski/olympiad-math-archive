# backend/test_brain.py
from prompt_builder import build_system_prompt

# Тест 1: Прваче
lesson_data_kids = {"grade": "I", "title": "Собирање до 10"}
activity_kids = "Игра со собирање јаболка во корпа."
print("--- TEST I ODD ---")
print(build_system_prompt(lesson_data_kids, activity_kids))

# Тест 2: Гимназијалец
lesson_data_hs = {"grade": "HighSchool_IV", "title": "Извод на функција"}
activity_hs = "Анализа на брзина на промена преку тангента."
print("\n--- TEST IV GODINA ---")
print(build_system_prompt(lesson_data_hs, activity_hs))
