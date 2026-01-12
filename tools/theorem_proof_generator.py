#!/usr/bin/env python3
"""
Theorem Proof Generator System

Овој систем овозможува автоматско генерирање на докази за теореми користејќи AI,
со вграден систем за валидација и интеграција во постоечката архива.
"""

import os
import json
import re
from pathlib import Path
from typing import Dict, List, Optional

class TheoremProofGenerator:
    def __init__(self, base_dir: str = "../"):
        self.base_dir = Path(base_dir).resolve()
        self.theorems_dir = self.base_dir / "web" / "src" / "data" / "theorems"
        self.templates_dir = self.base_dir / "tools" / "proof_templates"
        self.output_dir = self.base_dir / "tools" / "generated_proofs"

        # Креирај потребни папки
        for dir_path in [self.templates_dir, self.output_dir]:
            dir_path.mkdir(parents=True, exist_ok=True)

    def get_theorems_list(self) -> List[Dict]:
        """Ги собира сите теореми и нивниот статус."""
        theorems = []

        for file in sorted(os.listdir(self.theorems_dir)):
            if file.endswith('.md') and not file.startswith('_'):
                theorem_data = self._parse_theorem_file(file)
                theorems.append(theorem_data)

        return theorems

    def _parse_theorem_file(self, filename: str) -> Dict:
        """Парсира теорема фајл за основни информации."""
        filepath = self.theorems_dir / filename

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Извади frontmatter
        frontmatter = {}
        if content.startswith('---'):
            end_pos = content.find('---', 3)
            if end_pos > 0:
                fm_text = content[3:end_pos]
                for line in fm_text.split('\n'):
                    if ':' in line:
                        key, value = line.split(':', 1)
                        frontmatter[key.strip()] = value.strip().strip('"\'').strip()

        theorem_name = filename[:-3]  # без .md
        title = frontmatter.get('title', theorem_name.replace('_', ' '))
        category = frontmatter.get('category', 'General')
        difficulty = frontmatter.get('difficulty', 'Intermediate')
        has_proof = '## 📝 Доказ' in content

        return {
            'filename': theorem_name,
            'title': title,
            'category': category,
            'difficulty': difficulty,
            'has_proof': has_proof,
            'filepath': filepath,
            'content': content
        }

    def generate_ai_prompt_for_theorem(self, theorem: Dict) -> str:
        """Генерира детален AI prompt за доказ на теорема."""

        template = f"""
ТИ СИ ЕКСПЕРТ ПО МАТЕМАТИКА - ОЛИМПИСКИ ТРЕНЕР

Теорема: {theorem['title']}
Категорија: {theorem['category']}
Тежина: {theorem['difficulty']}

ГЕНЕРИРАЈ ДОКАЗ ЗА ОВАА ТЕОРЕМА СПОРЕД СЛЕДНИТЕ СТРОГИ ПРАВИЛА:

## ФОРМАТ НА ДОКАЗОТ:
```
## 📝 Доказ ([метод])
[Кратко објаснување на методот на доказ - 1-2 реченици]

### Чекор 1: [Име на чекорот]
[Детално објаснување со математички симболи]
$$ [формула или равенка] $$

### Чекор 2: [Име на чекорот]
[Детално објаснување со математички симболи]
$$ [формула или равенка] $$

[... дополнителни чекори ...]

### Заклучок:
[Финално резонирање]
```

## ПРАВИЛА ЗА ДОКАЗОТ:

### 1. ИЗБОР НА МЕТОД:
- **Геометриски теореми**: Доказ со плоштини, слични триаголници, координати, вектори
- **Алгебарски теореми**: Доказ со манипулација на равенки, индукција, контрадикција
- **Комбинаторни теореми**: Доказ со броење, биекција, рекурзија
- **Аналитички теореми**: Доказ со граници, деривации, интеграли

### 2. НИВО НА ДЕТАЛИ:
- **Basic**: Елементарен доказ, основни концепти
- **Intermediate**: Стандарден олимписки доказ, средно ниво
- **Advanced**: Напреден/елегантен доказ, универзитетско ниво

### 3. СТРУКТУРА:
- Максимум 5 чекори (за да биде разбирлив)
- Секој чекор треба да има текст + формула
- Користи LaTeX за математички изрази
- Објасни секој симбол и концепт

### 4. ВАЛИДАЦИЈА:
- Доказот мора да биде математички точен
- Сите претпоставки треба да се наведат
- Заклучокот треба да следи логично
- Избегни круг во доказувањето

### 5. ПЕДАГОШКИ ЕЛЕМЕНТИ:
- Додај интуитивни објаснувања
- Спомни алтернативни пристапи ако постојат
- Поврзи со поврзани концепти

## ПРИМЕР ЗА Ceva's теорема:
```
## 📝 Доказ (Преку плоштини)
Овој доказ користи својството дека плоштината на триаголник е пропорционална на основата.

### Чекор 1: Однос на плоштини
Во триаголниците со иста висина, плоштината е пропорционална на основата.
$ \frac{P_{ABD}}{P_{ACD}} = \frac{BD}{DC} $

### Чекор 2: Својство на пропорции
Користејќи својство на пропорции за мали триаголници:
$$ \\frac{P_{ABP}}{P_{ACP}} = \\frac{BD}{DC} $$

### Чекор 3: Комбинирање на односи
$$ \\frac{P_{ABP}}{P_{ACP}} \\cdot \\frac{P_{BCP}}{P_{BAP}} \\cdot \\frac{P_{CAP}}{P_{CBP}} = \\frac{BD}{DC} \\cdot \\frac{CE}{EA} \\cdot \\frac{AF}{FB} $$

### Заклучок:
Левата страна е 1, па производот на десната мора да биде 1.
$$ \\frac{AF}{FB} \\cdot \\frac{BD}{DC} \\cdot \\frac{CE}{EA} = 1 $$
```

ТЕОРЕМАТА МОРДА ДА СЕ ДОКАЖЕ: {theorem['title']}

ГЕНЕРИРАЈ САМО ДОКАЗОТ ВО ГОРЕНАВЕДЕНИОТ ФОРМАТ!
"""

        return template

    def generate_manim_prompt_for_theorem(self, theorem: Dict, proof_text: str) -> str:
        """Генерира Manim код за визуелизација на доказот."""

        template = f"""
ТИ СИ ЕКСПЕРТ ПО MANIM ЗА МАТЕМАТИЧКИ ВИЗУЕЛИЗАЦИИ

Теорема: {theorem['title']}
Категорија: {theorem['category']}

ГЕНЕРИРАЈ MANIM КОД ЗА ВИЗУЕЛИЗАЦИЈА НА ДОКАЗОТ:

## ПРАВИЛА ЗА MANIM КОД:

### 1. СТРУКТУРА НА СЦЕНАТА:
```python
class {theorem['filename'].title().replace('_', '')}ProofScene(Scene):
    def construct(self):
        # 1. Креирај основни елементи
        # 2. Анимирај чекори од доказот
        # 3. Покажи заклучок
        # 4. Додај текст објаснувања
```

### 2. ОСНОВНИ ЕЛЕМЕНТИ:
- **Геометриски**: Triangle, Circle, Line, Dot со labels
- **Текст**: Tex/MathTex за формули, Text за објаснувања
- **Анимации**: Write, FadeIn, Transform, Indicate
- **Бои**: BLUE, RED, GREEN за различни елементи

### 3. ЕКСПЕРТСКИ СОВЕТИ ЗА MANIM:
- Користи `self.play()` за анимации
- Групирај елементи во VGroup за едновремено манипулирање
- Користи `always_redraw` за динамични елементи
- Додај `self.wait()` помеѓу чекори
- Користи `TransformMatchingTex` за трансформација на равенки
- Означи точки со `Dot().add_updater(lambda d: d.next_to(point, UP))`

### 4. ПЕДАГОШКИ ПРАВИЛА:
- Почни со едноставен цртеж
- Постепено додавај елементи
- Користи стрелки за да укажеш на односи
- Додај бројки/формули до елементи
- Заврши со визуелен заклучок

### 5. ТЕХНИЧКИ ПРАВИЛА:
- Користи релативни координати (ORIGIN, UP, DOWN, LEFT, RIGHT)
- Додели имиња на променливи за лесно ажурирање
- Користи `self.add()` за постојани елементи
- Додај коментари за секој чекор

ПРИМЕР ЗА PYTHAGOREAN THEOREM:
```python
class PythagoreanProofScene(Scene):
    def construct(self):
        # Креирај правоаголен триаголник
        triangle = Polygon(ORIGIN, 3*RIGHT, 3*RIGHT + 2*UP, color=BLUE)
        self.play(Create(triangle))

        # Додај квадрати на страните
        # ... анимации за доказ

        # Додај текст: a² + b² = c²
        conclusion = MathTex("a^2 + b^2 = c^2").scale(1.5)
        self.play(Write(conclusion))
```

ГЕНЕРИРАЈ КОМПЛЕТЕН MANIM КОД ЗА ВИЗУЕЛИЗАЦИЈА НА ДОКАЗОТ НА ТЕОРЕМАТА: {theorem['title']}

ДОКАЗ ТЕКСТ: {proof_text[:500]}...

ГЕНЕРИРАЈ САМО MANIM КОД ВО ФОРМАТО НАДВОРЕ!
"""

        return template

    def validate_proof_content(self, proof_text: str, theorem: Dict) -> Dict:
        """Валидира дали доказот ги задоволува сите барања."""

        validation_results = {
            'is_valid': True,
            'errors': [],
            'warnings': []
        }

        # Проверка за основни елементи
        if not proof_text.strip():
            validation_results['errors'].append("Доказот е празен")

        if '## 📝 Доказ' not in proof_text:
            validation_results['errors'].append("Недостасува заглавие '## 📝 Доказ'")

        if '### Чекор 1:' not in proof_text:
            validation_results['errors'].append("Недостасува барем еден чекор")

        if '### Заклучок:' not in proof_text:
            validation_results['errors'].append("Недостасува заклучок")

        # Проверка за LaTeX формули
        latex_count = len(re.findall(r'\$\$[^$]+\$\$', proof_text))
        if latex_count < 2:
            validation_results['warnings'].append("Мал број на LaTeX формули")

        # Проверка за математичка точност (основна)
        theorem_name = theorem['title'].lower()
        proof_lower = proof_text.lower()

        # Основни проверки за некои теореми
        if 'ceva' in theorem_name and 'пл' not in proof_lower and 'плошт' not in proof_lower:
            validation_results['warnings'].append("Ceva's доказ обично користи плоштини")

        if 'pythagoras' in theorem_name or 'pitagora' in theorem_name:
            if 'квадрат' not in proof_lower and 'square' not in proof_lower:
                validation_results['warnings'].append("Pythagorean доказ обично вклучува квадрати")

        # Финална валидација
        if validation_results['errors']:
            validation_results['is_valid'] = False

        return validation_results

    def integrate_proof_into_theorem(self, theorem: Dict, proof_text: str, manim_code: str = None) -> bool:
        """Интегрира доказот во теоремата фајл."""

        try:
            content = theorem['content']

            # Ако веќе има доказ, замени го
            if '## 📝 Доказ' in content:
                # Најди почеток и крај на постоечкиот доказ
                start = content.find('## 📝 Доказ')
                # Најди следната секција или крај
                next_section = re.search(r'\n## [^\n]+', content[start+1:])
                if next_section:
                    end = start + next_section.start()
                else:
                    end = len(content)

                # Замени го доказот
                new_content = content[:start] + proof_text + content[end:]
            else:
                # Додај доказ пред првата ## секција после frontmatter
                # Најди каде да го вметнеш (после ## 🛠 Каде се користи?)
                insert_pos = content.find('## 🛠 Каде се користи?')
                if insert_pos == -1:
                    insert_pos = content.find('---', content.find('---') + 1) + 3

                # Најди крај на секцијата
                next_section_match = re.search(r'\n## [^\n]+', content[insert_pos:])
                if next_section_match:
                    insert_end = insert_pos + next_section_match.start()
                    new_content = content[:insert_end] + '\n\n' + proof_text + '\n\n' + content[insert_end:]
                else:
                    new_content = content + '\n\n' + proof_text

            # Сними ја новата содржина
            with open(theorem['filepath'], 'w', encoding='utf-8') as f:
                f.write(new_content)

            # Ако има Manim код, создај датотека
            if manim_code:
                manim_filename = f"manim_{theorem['filename']}_proof.py"
                manim_filepath = self.output_dir / manim_filename

                with open(manim_filepath, 'w', encoding='utf-8') as f:
                    f.write(manim_code)

                print(f"Manim код зачуван во: {manim_filepath}")

            return True

        except Exception as e:
            print(f"Грешка при интеграција: {e}")
            return False

    def process_theorem_batch(self, theorem_list: List[str] = None) -> Dict:
        """Процесира множество теореми - генерира prompts за AI."""

        theorems = self.get_theorems_list()

        if theorem_list:
            theorems = [t for t in theorems if t['filename'] in theorem_list]

        results = {}

        for theorem in theorems:
            if not theorem['has_proof']:
                prompt = self.generate_ai_prompt_for_theorem(theorem)
                results[theorem['filename']] = {
                    'title': theorem['title'],
                    'prompt': prompt,
                    'category': theorem['category'],
                    'difficulty': theorem['difficulty']
                }

        return results

    def create_workflow_summary(self) -> str:
        """Креира резиме на workflow за корисникот."""

        theorems = self.get_theorems_list()
        total = len(theorems)
        with_proofs = len([t for t in theorems if t['has_proof']])
        without_proofs = total - with_proofs

        summary = f"""
# СИСТЕМ ЗА ГЕНЕРИРАЊЕ ДОКАЗИ ЗА ТЕОРЕМИ

## СТАТУС:
- Вкупно теореми: {total}
- Со докази: {with_proofs} ({with_proofs/total*100:.1f}%)
- Без докази: {without_proofs} ({without_proofs/total*100:.1f}%)

## ПРОЦЕДУРА ЗА ДОБИВАЊЕ ДОКАЗ:

### 1. Избери теорема
```python
generator = TheoremProofGenerator()
theorems = generator.get_theorems_list()
# Филтрирај само оние без докази
missing_proofs = [t for t in theorems if not t['has_proof']]
```

### 2. Генерирај AI Prompt
```python
for theorem in missing_proofs:
    prompt = generator.generate_ai_prompt_for_theorem(theorem)
    # Копирај го prompt-от во AI алатка (ChatGPT, Claude, итн.)
```

### 3. Добиј доказ од AI
- Користи prompt-от за да добиеш доказ во бараниот формат
- Провери дали доказот ги задоволува сите правила

### 4. Генерирај Manim визуелизација (опционално)
```python
manim_prompt = generator.generate_manim_prompt_for_theorem(theorem, proof_text)
# Копирај во AI за Manim код
```

### 5. Валидирај и интеграцирај
```python
validation = generator.validate_proof_content(proof_text, theorem)
if validation['is_valid']:
    success = generator.integrate_proof_into_theorem(theorem, proof_text, manim_code)
```

## ПРАВИЛА ЗА КВАЛИТЕТ:

### Обавезни елементи:
- ✅ Тачно заглавие "## 📝 Доказ ([метод])"
- ✅ Барем 2 чекори со објаснувања
- ✅ LaTeX формули во $$ блокови
- ✅ Заклучок со финалниот резултат

### Препорачани елементи:
- 📝 Интуитивни објаснувања
- 🔗 Поврзување со други концепти
- 🎨 Визуелни елементи (Manim)
- 📚 Литературни референци

### Чести грешки:
- ❌ Премногу технички детали
- ❌ Недостасувачки чекори
- ❌ Неточни математички симболи
- ❌ Неконзистентна нотација

## АВТОМАТИЗАЦИЈА:

За автоматска обработка, користи:
```bash
python tools/theorem_proof_generator.py --batch --validate --integrate
```

Ова ќе ги процесира сите теореми без докази и ќе ги интеграцира во системот.
"""

        return summary

def main():
    generator = TheoremProofGenerator()

    # Прикажи статус
    print(generator.create_workflow_summary())

    # Генерирај prompts за сите теореми без докази
    batch_results = generator.process_theorem_batch()

    if batch_results:
        print("\n" + "="*50)
        print("AI PROMPTS ЗА ГЕНЕРИРАЊЕ НА ДОКАЗИ:")
        print("="*50)

        for theorem_id, data in batch_results.items():
            print(f"\n## {data['title']} ({theorem_id})")
            print(f"**Категорија:** {data['category']} | **Тежина:** {data['difficulty']}")
            print("\n**PROMPT ЗА AI:**")
            print(data['prompt'])
            print("\n" + "-"*50)

if __name__ == "__main__":
    main()