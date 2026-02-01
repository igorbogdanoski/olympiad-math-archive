# backend/prompt_builder.py

def get_pedagogical_strategy(grade):
    """
    Ја одредува стратегијата според возраста на детето.
    """
    # Листа на помали одделенија
    young_grades = ["I", "II", "III", "IV", "V"]
    
    # Листа на поголеми одделенија (предметна настава)
    middle_grades = ["VI", "VII", "VIII", "IX"]
    
    if grade in young_grades:
        return """
        - **TONE:** Playful, enthusiastic, storytelling style. Like a friendly TV presenter for kids.
        - **VISUALS:** Use bright colors, simple geometric shapes (Star, Circle, Square).
        - **SPEED:** Slow and clear animations. Use self.wait(2) often.
        - **CONTEXT:** Treat the math problem as a magical adventure or a game.
        - **KEYWORD:** Simplification and Joy.
        """
    elif grade in middle_grades:
        return """
        - **TONE:** Exploratory and encouraging. Connect concepts to real life.
        - **VISUALS:** Clean, modern diagrams. Use coordinate systems and graphs where needed.
        - **SPEED:** Moderate pace. Focus on "Why" something works.
        - **CONTEXT:** Real-world applications and logical discovery.
        - **KEYWORD:** Intuition and Logic.
        """
    else: # Средно образование (I, II, III, IV година)
        return """
        - **TONE:** Academic, rigorous, but engaging. Like a top-tier YouTube educator (e.g., 3Blue1Brown).
        - **VISUALS:** Precise mathematical plots, functions, and proofs.
        - **SPEED:** Efficient. Focus on abstraction and logic.
        - **CONTEXT:** Rigorous proofs and high-level abstract thinking.
        - **KEYWORD:** Rigor and Elegance.
        """

def build_system_prompt(lesson_data, selected_activity):
    """
    Го креира финалниот промпт за Gemini со Chain of Thought (CoT).
    """
    grade = lesson_data.get("grade", "Unknown")
    topic = lesson_data.get("title", "Math Topic")
    
    strategy = get_pedagogical_strategy(grade)
    
    system_prompt = f"""
### ROLE
You are a World-Class Educational Content Creator and Senior Manim (Python) Developer.
Your goal is to transform a mathematical activity into a stunning, pedagogically sound animation.

### TARGET AUDIENCE
- **Grade Level:** {grade}
- **Topic:** {topic}

### PEDAGOGICAL STRATEGY
{strategy}

### THE CORE ACTIVITY
"{selected_activity}"

### THINKING PROCESS (Chain of Thought - REQUIRED)
Before writing any code, you MUST:
1. **Analyze:** Break down the activity into 3 key mathematical concepts.
2. **Visualize:** Describe the visual metaphor or scene layout (Background, Objects, Colors).
3. **Plan:** Outline the animation sequence (Step-by-step).

### TECHNICAL EXPERT CONSTRAINTS (MANIM CE)
1. **Cyrillic Support:**
   ```python
   from manim.utils.tex import TexTemplate
   cyrillic_template = TexTemplate()
   cyrillic_template.add_to_preamble(r"\\usepackage[utf8]{{inputenc}}")
   cyrillic_template.add_to_preamble(r"\\usepackage[T2A]{{fontenc}}")
   cyrillic_template.add_to_preamble(r"\\usepackage[macedonian]{{babel}}")
   # Use: Tex(r"Текст", tex_template=cyrillic_template) or Text("Текст", font="Arial")
   ```
2. **Dynamic Elements:** Use `ValueTracker` for variable parameters and `always_redraw` for labels/objects that depend on them.
3. **Transformations:** Use `TransformMatchingTex` with `transform_mismatches=True` for smooth equation transitions.
4. **Style:** 
   - Background: `self.camera.background_color = WHITE` (if requested by local renderer).
   - Class Name: `LessonScene`.
5. **Output:** Provide the thinking process first, followed by the Python code block.

Let's begin.
"""
    return system_prompt

def build_lesson_plan_prompt(lesson_data, selected_activity):
    """
    Креира промпт за целосно сценарио за час (Lesson Plan).
    """
    grade = lesson_data.get("grade", "Unknown")
    topic = lesson_data.get("title", "Math Topic")
    objectives = "\n".join([f"- {obj}" for obj in lesson_data.get("objectives", [])])
    standards = "\n".join([f"- {std}" for std in lesson_data.get("standards", [])])
    
    strategy = get_pedagogical_strategy(grade)
    
    prompt = f"""
### ROLE
You are a Master Teacher and Educational Strategist specializing in the Macedonian National Curriculum.
Your goal is to create a comprehensive, highly engaging Lesson Plan (Сценарио за час).

### CONTEXT
- **Grade Level:** {grade}
- **Topic:** {topic}
- **BRO Objectives:**
{objectives}
- **BRO Standards:**
{standards}
- **Core Activity:** "{selected_activity}"

### PEDAGOGICAL STRATEGY
{strategy}

### INSTRUCTIONS
Generate a structured Lesson Plan in **Macedonian language**. The response must be a valid JSON object with the following structure:

{{
  "title": "Наслов на лекцијата",
  "intro": {{
    "duration": "5-10 мин",
    "hook": "Интересен вовед или прашање за поттикнување љубопитност",
    "context": "Како ова се поврзува со претходно знаење"
  }},
  "core_activity": {{
    "duration": "20 мин",
    "description": "Чекор-по-чекор инструкции за наставникот",
    "visual_focus": "Што треба наставникот да нагласи додека ја покажува анимацијата",
    "key_questions": ["Прашање 1", "Прашање 2"]
  }},
  "olympiad_bridge": {{
    "duration": "10 мин",
    "connection": "Како овој концепт се користи во олимписки задачи",
    "example_problem_brief": "Краток опис на еден потежок предизвик поврзан со темата"
  }},
  "assessment": {{
    "duration": "5 мин",
    "method": "Брз начин за проверка на разбирањето",
    "homework_suggestion": "Предлог за домашна работа"
  }}
}}

### LANGUAGE & FORMATTING REQUIREMENT
- All text content must be in **Macedonian Cyrillic**.
- **Mathematical Formulas:** Use LaTeX for ALL mathematical formulas and variables. 
  - Use `\\( ... \\)` for inline math (e.g., \\( x^2 \\)).
  - Use `\\[ ... \\]` for display math on a new line.
  - DO NOT use single $ signs.
- Be specific to the Grade Level and Topic.
- Use professional yet accessible language for a teacher.

Return ONLY the JSON object.
"""
    return prompt
