import frontmatter

def load_problem(filepath):
    """
    Вчитува Markdown фајл со YAML хедeр и го враќа како речник (dictionary).
    Ова го заменува стариот json.load() метод.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        # frontmatter.load автоматски ги парсира метаподатоците и содржината
        post = frontmatter.load(f)
    
    # post.metadata ги содржи полињата како 'id', 'tags', 'difficulty'
    data = post.metadata
    
    # post.content го содржи целиот текст (body)
    # Овде правиме едноставна поделба ако имаме посебни секции
    content = post.content
    
    # Ако сакаме да го одделиме текстот на задачата од решението:
    parts = content.split('# Решение')
    
    if len(parts) > 1:
        problem_text_raw = parts[0].replace('# Текст на задачата', '').strip()
        data['problem_text_mk'] = problem_text_raw
        
        # Решението е вториот дел, но можеби има и педагошки забелешки
        solution_part = parts[1]
        if '# Pedagogical Notes' in solution_part:
            sol_parts = solution_part.split('# Pedagogical Notes')
            data['solution_content'] = sol_parts[0].strip()
            data['pedagogical_notes'] = sol_parts[1].strip()
        else:
            data['solution_content'] = solution_part.strip()
            
    return data

# Тест блок
if __name__ == "__main__":
    # Пробај да го вчиташ фајлот што го креиравме во Чекор 1
    import os
    sample_path = r"c:\Userrs\pc4all\Documents\matholimpiad\olympiad-math-arrchive\prroblems\sigma137_p1871.mdr
    
    if os.path.exists(sample_path):
        problem = load_problem(sample_path)
        print("Успешно вчитана задача:", problem.get('title'))
        print("Решение (првите 50 карактери):", problem.get('solution_content')[:50])
    else:
        print("Фајлот не постои. Ве молиме креирајте го прво.")