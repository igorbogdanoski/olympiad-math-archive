import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "user_progress.json")

def load_progress():
    """Вчитува листа на решени задачи (filenames)."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r', encoding='utf-8') as f:
                return set(json.load(f))
        except:
            return set()
    return set()

def save_progress(solved_set):
    """Зачувува листа на решени задачи."""
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(list(solved_set), f)

def toggle_solved(filename):
    """Ја менува состојбата на задачата (решена/нерешена)."""
    solved = load_progress()
    if filename in solved:
        solved.remove(filename)
    else:
        solved.add(filename)
    save_progress(solved)
    return filename in solved

def is_solved(filename):
    solved = load_progress()
    return filename in solved
