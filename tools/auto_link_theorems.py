import os
import re
import frontmatter
from pathlib import Path

def get_theorem_keywords():
    """Dictionary of theorems and their keywords for matching."""
    return {
        'pythagorean_theorem': ['Питагорова теорема', 'питагорова', 'a² + b² = c²'],
        'cevas_theorem': ['Чевината теорема', 'чева', 'ceva'],
        'law_of_sines': ['Теорема за синусите', 'закон за синусите', 'sin A/a = sin B/b'],
        'law_of_cosines': ['Теорема за косинусите', 'закон за косинусите', 'c² = a² + b² - 2ab cos C'],
        'pigeonhole_principle': ['Голупчева теорема', 'пigeonhole', 'голупче'],
        'am_gm_inequality': ['AM-GM', 'ам-гм', 'ариметметичка-геометричка'],
        'cauchy_schwarz_inequality': ['Коши-Шварц', 'cauchy-schwarz', 'коши шварц'],
        'vieta_formulas': ['Виетови формули', 'vieta', 'виета'],
        'similarity': ['Сличност', 'слични триаголници'],
        'menelaus_theorem': ['Менелаова теорема', 'menelaus'],
        'eulers_theorem': ['Ојлерова теорема', 'euler'],
        'fermats_little_theorem': ['Малиот Ферма', 'fermat', 'ферма'],
        'circle_properties': ['Кружни својства', 'тетивен производ'],
        'induction': ['Математска индукција', 'индукција'],
        'modular_arithmetic': ['Модуларна аритметика', 'модуло'],
        'quadratic_equations': ['Квадратни равенки', 'квадратно'],
        'functions': ['Функции', 'домена'],
        'derivatives': ['Деривации', 'изведувања'],
        'integrals': ['Интеграли', 'интегрирање'],
        'vectors': ['Вектори', 'скаларен производ'],
        'complex_numbers': ['Комплексни броеви', 'i² = -1'],
        'combinatorics': ['Комбинаторика', 'пермутации'],
        'probability': ['Веројатност', 'веројатно'],
        'geometry_construction': ['Геометриска конструкција'],
        'trigonometric_identities': ['Тригонометриски идентитети'],
        'polynomial_expansion': ['Полиноми', 'експанзија'],
        'floor_function': ['Подна функција', 'floor'],
        'continued_fractions': ['Верижни дроби'],
        'number_theory': ['Теорија на броевите', 'делители'],
        'graph_theory': ['Теорија на графи', 'графови'],
        'optimization': ['Оптимизација', 'максимум', 'минимум'],
        'invariants': ['Инваријанти', 'непроменливи'],
        'parity': ['Парност', 'парен', 'неparen'],
        'symmetry': ['Симетрија'],
        'case_analysis': ['Анализа на случаи'],
        'working_backwards': ['Работење наназад'],
        'visual_reasoning': ['Визуелно размислување'],
        'pattern_recognition': ['Препознавање на шеми'],
        'structural_thinking': ['Структурно размислување']
    }

def find_related_theorems(content):
    """Find theorems mentioned in problem content."""
    theorems = []
    keywords = get_theorem_keywords()

    content_lower = content.lower()

    for theorem, keys in keywords.items():
        for key in keys:
            if key.lower() in content_lower:
                theorems.append(theorem)
                break

    return list(set(theorems))  # Remove duplicates

def process_problem_file(file_path):
    """Process a single problem file to add related theorems."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        post = frontmatter.loads(content)

        # Get existing related theorems
        existing_theorems = post.metadata.get('related_theorems', [])

        # Find new theorems from content
        found_theorems = find_related_theorems(content)

        # Combine and deduplicate
        all_theorems = list(set(existing_theorems + found_theorems))

        if all_theorems and all_theorems != existing_theorems:
            post.metadata['related_theorems'] = all_theorems
            print(f"Updated {file_path.name}: Added theorems {found_theorems}")

            # Save the file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))

            return True

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

    return False

def main():
    base_dir = Path(__file__).parent.parent
    docs_dir = base_dir / "docs"

    updated_count = 0

    for root, dirs, files in os.walk(docs_dir):
        # Skip non-problem directories
        if any(x in root for x in ["skill_guides", "theorems", "templates", "generated_worksheets", "assets", "public"]):
            continue

        for file in files:
            if file.endswith('.md') and not file.startswith('_'):
                file_path = Path(root) / file
                if process_problem_file(file_path):
                    updated_count += 1

    print(f"Processed {updated_count} files with theorem links.")

if __name__ == "__main__":
    main()