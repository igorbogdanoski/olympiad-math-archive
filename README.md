# 🏆 Olympiad Math Archive (Production)

Интегрирана платформа за управување, решавање и архивирање на математички олимписки задачи, автоматизирана со AI и поддржана од модерна облак инфраструктура.

## 🚀 Преглед на системот
Овој проект е структуриран да овозможи брз пристап до образовни материјали (БРО стандарди) и над **1100+ математички задачи**, со фокус на автоматизирано генерирање на решенија, интерактивна визуелизација и AI-асистирана настава.

### 🏗️ Структура на репозиториумот
* **`/web`**: Frontend портал изграден со Astro (Teachers Portal, Students Portal, AI Grader)
* **`/backend`**: FastAPI backend со MongoDB интеграција
* **`/infrastructure`**: IaC (Infrastructure as Code) користејќи Terraform за AWS deployment
* **`/tools`**: Python автоматизација за обработка на податоци и генерирање LaTeX/PDF
* **`/problems`**: JSON база на 1100+ олимписки задачи
* **`/database`**: MongoDB seed скрипти и schema дефиниции
* **`/docs`**: Комплетна документација на системот (SYSTEM_IMPLEMENTATION_RECORD)

## 🛠️ Технолошки стак
* **Frontend:** Astro v4.16, Svelte, TailwindCSS
* **Backend:** FastAPI (Python 3.11+), MongoDB, Uvicorn
* **AI:** Google Gemini 1.5 Pro (Vision AI Grading, LaTeX OCR, Problem Generation)
* **Visualization:** Manim CE, GeoGebra
* **Infrastructure:** Terraform, AWS (в.п. production deployment)
* **CI/CD:** GitHub Actions (автоматски syntax проверки)

## 🔧 Како да започнете (Local Setup)

### 1. Web Портал
```bash
cd web
npm install
npm run build  # Генерира 1315+ статични страници (трае ~5 мин)
npm run preview -- --host 0.0.0.0 --port 4321
```
Пристап: http://localhost:4321

### 2. Backend API
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
API документација: http://localhost:8000/docs

### 3. Infrastructure (Terraform)
*Напомена: Провајдерите се исклучени од Git за оптимизација (787MB спасени).*
```bash
cd infrastructure/prod
terraform init
terraform plan
```

## 🎓 Клучни Features
* ✅ **1100+ Олимписки задачи** (БРО усогласени)
* ✅ **391 Наставни стандарди** (I-XII одделение, 100% покриеност)
* ✅ **Vision AI Grading** - Скенирање и оценување на ракописни решенија
* ✅ **Teachers Co-pilot** - AI генератор на тестови, планови за час, и работни листови
* ✅ **Knowledge Graph** - Семантичко мапирање на математички концепти
* ✅ **GeoGebra интеграција** - Интерактивна геометрија
* ✅ **Manim анимации** - Визуелизација на математички докази

## 🧹 Git Хигиена и Стандарди

Овој репозиториум одржува **чиста историја** (orphan branch стратегија).

### 🚫 Забрането да се комитира:
* `.terraform/` (провајдери, state)
* `web/dist/` (build artifacts)
* `web/node_modules/` (dependencies)
* `backend/.env` (secrets)
* `*.log` (runtime logs)

### ✅ Пред секој commit:
1. Провери `.gitignore` (сите горенаведени се веќе исклучени)
2. Никогаш фајлови > 10MB (GitHub limit = 100MB)
3. Користи `git status` пред `git add .`

## 📊 Статус на проектот (Februari 2026)

| Метрика | Вредност | Статус |
|---------|----------|--------|
| Математички задачи | 1100+ | ✅ Complete |
| БРО Стандарди | 391/391 | ✅ 100% |
| AI Верификација | 1100/1100 | ✅ Done |
| Knowledge Graph | 391 nodes | ✅ Active |
| GeoGebra мапирање | 220+ tasks | 🚧 Ongoing |
| Production Branch | `production-clean-v2` | ✅ Live |

## 🔐 Git Криза Резолуција (2026-02-02)
Репозиториумот помина низ критична orphan branch миграција за отстранување на 787MB Terraform binary од историјата. Детали: [SYSTEM_IMPLEMENTATION_RECORD.md](./SYSTEM_IMPLEMENTATION_RECORD.md#-2026-02-02-git-infrastructure-crisis---resolved)

## 🚦 Следни чекори
- [ ] PWA mobile testing (Add to Home Screen)
- [ ] Vision AI stress test (3+ sequential uploads)
- [ ] Knowledge Graph → Vision AI интеграција
- [ ] Default branch промена на GitHub (`main` → `production-clean-v2`)

---

**Лиценца:** Educational Use Only  
**Контакт:** Igor Bogdanoski  
**Верзија:** v1.0.0 (Production Clean)

---
*"Connecting national curriculum with Olympiad excellence through AI"* 🚀
