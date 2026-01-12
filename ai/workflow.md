# 🚀 Olympiad Archive Workflow (Оперативен Прирачник v2.1)

Овој документ го опишува комплетниот процес на работа: од внес на задача до печатење на професионални материјали.

---

## 1. 📥 Внес на Задачи (Input Phase)

1. **Извор:** Сликај ја задачата или копирај го текстот (од Нумерус, Сигма, Натпревари).
2. **AI Обработка (Google AI Studio):**
   - Користи го **System Prompt** (со Manim инструкциите).
   - Постави ја **JSON Schema** (со `manim_code`).
   - Внеси ја задачата и побарај JSON излез.
3. **Подготовка:**
   - Отвори го фајлот `tools/input.json`.
   - Залепи го JSON кодот внатре (може и листа од повеќе задачи).

---

## 2. ⚙️ Процесирање (Build Phase)

1. Отвори терминал во папката `tools`.
2. Стартувај ја скриптата:
   ```bash
   python build_problem.py
   ```
3. **Што се случува автоматски?**
   - Се креираат `.md` фајлови во соодветните папки (`grade_X` или `pre_olympiad`).
   - Се генерираат логови за визуелизација во `assets/manim_code_log.md`.
   - **Auto-Skeleton:** Ако задачата користи нова вештина (Skill) или теорема што ја немаме, скриптата автоматски креира празен фајл во `tools/skill_guides/` или `tools/theorems/`.
   - Ако веќе постои слика во `assets/images`, таа автоматски се вметнува во задачата.

---

## 3. 🎨 Визуелизација (Geometry Workflow)

Ова е „Хибридниот модел“ за најбрзи и најпрецизни резултати (без локална инсталација на Manim).

1. Отвори го фајлот **`assets/manim_code_log.md`**.
2. Најди го кодот за новата задача (најдолу во фајлот).
3. Копирај го Python кодот.
4. Оди во **Geo-Mentor** (или локален Manim/Google Colab).
5. Залепи го кодот и генерирај слика.
6. **Зачувај ја сликата:**
   - **Име:** Мора да биде исто како ID-то на задачата (пр. `sigma_01.png`).
   - **Локација:** Зачувај ја во папката `assets/images/`.
7. *(Опционално)* Повторно пушти `python build_problem.py` за сликата веднаш да се појави во Markdown фајлот.

---

## 4. 📤 Креирање Материјали (Publishing Phase)

Имаш три моќни алатки за генерирање документи:

### А. SmartTestGenerator - Паметен генератор на тестови (За наставници)
Креира **професионални HTML тестови** со современ дизајн, MathJax и оптимизирано печатење:

#### Командна линија:
```bash
# Пример: Тест за 9-то одделение, Алгебра, 5 средни задачи
python tools/generate_smart_test.py -g 9 -f algebra -c 5 -d medium
```

#### Веб интерфејс (Препорачано):
1. Оди на `http://localhost:4321/teachers` (стартувај `npm run dev` во `web/`)
2. Избери параметри: одделение, област, број на задачи
3. Кликни "Генерирај преглед"
4. Кликни "🖨️ Печати тест" за професионален PDF

#### Карактеристики:
- **Двојни верзии**: Посебни HTML фајлови за ученици и наставници
- **Интелигентна селекција**: Квалитетско рангирање на проблеми
- **Modern Design**: Inter fonts, CSS gradients, responsive layout
- **MathJax 3**: Перфектно математичко рендерирање
- **Print Ready**: Оптимизирано за A4 печатење

### Б. Професионални Документи (Работни листови / Картички)
Генерира HTML/PDF материјали од сите задачи што се моментално во `input.json`:
```bash
python generate_pro_documents.py
```
**Резултат:** Папка `output_documents` со работни листови и картички за сечење.

### В. Единечен Експорт (Брз преглед)
Ако сакаш само една конкретна задача во Word или PDF:
```bash
# За Word
python export.py grade_9/geometry/task_01.md

# За PDF
python export.py grade_9/geometry/task_01.md --pdf
```

---

## 5. 🌐 Веб развој и тестирање

### Стартување на веб апликацијата:
```bash
cd web
npm install
npm run dev  # Отвора на http://localhost:4321
```

### Структура на веб апликацијата:
- **Frontend**: Astro.js + Tailwind CSS
- **API**: Server-side routes за SmartTestGenerator интеграција
- **Teachers Interface**: `/teachers` - модерен генератор на тестови
- **Student Interface**: `/tasks/[id]` - индивидуални задачи
- **Documentation**: MkDocs за статични страници

### Тестирање:
```bash
# E2E тестирање со Playwright
npm run test

# Unit тестови (доколку се додадат)
npm run test:unit
```

---

## 6. 📚 Одржување и надградби (Maintenance)

### Пополнување на системот:
- **Skill Guides**: Проверувај `tools/skill_guides/` за нови методи
- **Problem Validation**: Користи SmartTestGenerator за квалитет проверка
- **Web Updates**: Проверувај API endpoints и UI компоненти

### Напредни алатки:
```bash
# Компајлирање книги од цела област
python tools/compile_book.py grade_9/algebra

# Батч процесирање на проблеми
python tools/process_olympiad.py

# Визуелизации со Manim
python tools/batch_manim.py
```

### Мониторинг и analytics:
- **Problem Quality**: SmartTestGenerator logs за квалитет метрики
- **Usage Statistics**: Web analytics за teacher engagement
- **Performance**: API response times и error rates
