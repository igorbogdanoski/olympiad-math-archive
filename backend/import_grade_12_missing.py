import pymongo
from datetime import datetime

MONGO_URI = "mongodb://76.13.129.9:27035/"
DB_NAME = "olympiad_db"

problems = [
    {
        "problem_id": "2026_g12_t1_1",
        "title": "Оптимизација и изводи",
        "grade": 12,
        "category": "calculus",
        "difficulty": 5,
        "description": "Најди ги димензиите на цилиндар со најголем волумен кој може да се впише во сфера со радиус R. Користи ги правилата за диференцирање.",
        "solution": "V = πr²h. r² + (h/2)² = R² => r² = R² - h²/4. V(h) = π(R² - h²/4)h = πR²h - πh³/4. V'(h) = πR² - 3πh²/4 = 0 => h = 2R/√3. r = R√(2/3).",
        "curriculum_codes": ["MAT-S-G12-T1-S3", "MAT-S-G12-T1-S6"],
        "tags": ["изводи", "оптимизација", "геометрија"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g12_t2_1",
        "title": "Интегрално сметање и физика",
        "grade": 12,
        "category": "calculus",
        "difficulty": 5,
        "description": "Пресметај го интегралот ∫ x² sin(x) dx користејќи парцијална интеграција. Објасни како определениот интеграл се користи за пресметување работа во физиката.",
        "solution": "∫ u dv = uv - ∫ v du. u = x², dv = sin(x)dx => du = 2xdx, v = -cos(x). ∫ x² sin(x) dx = -x²cos(x) + ∫ 2x cos(x) dx. Повторно парцијална: u=2x, dv=cos(x)dx => du=2dx, v=sin(x). Резултат: -x²cos(x) + 2xsin(x) + 2cos(x) + C. Работа W = ∫ F dx.",
        "curriculum_codes": ["MAT-S-G12-T2-S1", "MAT-S-G12-T2-S2", "MAT-S-G12-T2-S3", "MAT-S-G12-T2-S6"],
        "tags": ["интеграли", "парцијална интеграција", "физика"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g12_t3_1",
        "title": "Сопствени вредности и вектори",
        "grade": 12,
        "category": "algebra",
        "difficulty": 5,
        "description": "Најди ги сопствените вредности на матрицата A = [[1, 2], [2, 1]]. Објасни го концептот на линеарна трансформација.",
        "solution": "det(A - λI) = |1-λ 2; 2 1-λ| = (1-λ)² - 4 = λ² - 2λ - 3 = 0. (λ-3)(λ+1) = 0. Сопствени вредности се λ=3 и λ=-1. Линеарна трансформација е пресликување меѓу векторски простори кое ги зачувува собирањето и множењето со скалар.",
        "curriculum_codes": ["MAT-S-G12-T3-S1", "MAT-S-G12-T3-S2", "MAT-S-G12-T3-S3", "MAT-S-G12-T3-S5", "MAT-S-G12-T3-S6", "MAT-S-G12-T3-S7"],
        "tags": ["матрици", "сопствени вредности", "линеарна алгебра"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g12_t4_1",
        "title": "Статистичка анализа и регресија",
        "grade": 12,
        "category": "data",
        "difficulty": 4,
        "description": "Што е нормална распределба и која е нејзината улога во статистичкото тестирање на хипотези? Како се толкува коефициентот на корелација r?",
        "solution": "Нормалната распределба (Гаусова) е симетрична распределба во форма на ѕвоно. Се користи за дефинирање на критични региони и p-вредности. r е меѓу -1 и 1; 1 значи совршена позитивна линеарна поврзаност, -1 совршена негативна, 0 нема поврзаност.",
        "curriculum_codes": ["MAT-S-G12-T4-S1", "MAT-S-G12-T4-S3", "MAT-S-G12-T4-S4", "MAT-S-G12-T4-S5", "MAT-S-G12-T4-S6", "MAT-S-G12-T4-S7"],
        "tags": ["статистика", "регресија", "хипотези"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g12_t5_1",
        "title": "Комплексна анализа и интеграли",
        "grade": 12,
        "category": "algebra",
        "difficulty": 5,
        "description": "Што е аналитичка функција во комплексната рамнина? Објасни ја основната идеја на контурните интеграли.",
        "solution": "Функција е аналитичка ако има извод во секоја точка од некоја околина (ги задоволува Коши-Римановите услови). Контурен интеграл е интеграл на функција по должина на крива во комплексната рамнина.",
        "curriculum_codes": ["MAT-S-G12-T5-S1", "MAT-S-G12-T5-S2", "MAT-S-G12-T5-S3", "MAT-S-G12-T5-S4", "MAT-S-G12-T5-S5"],
        "tags": ["комплексна анализа", "интеграли"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g12_t6_1",
        "title": "Графови и криптографија",
        "grade": 12,
        "category": "logic",
        "difficulty": 4,
        "description": "Наведи пример за Ојлеров пат во граф. Како се користи Буловата алгебра во дизајнирање на логички кола?",
        "solution": "Ојлеров пат минува низ секој раб на графот точно еднаш. Буловата алгебра (AND, OR, NOT операции) се користи за минимизирање и имплементација на дигитални функции во хардверот.",
        "curriculum_codes": ["MAT-S-G12-T6-S1", "MAT-S-G12-T6-S3", "MAT-S-G12-T6-S5"],
        "tags": ["графови", "булова алгебра", "криптографија"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g12_t1_2",
        "title": "Диференцијални равенки",
        "grade": 12,
        "category": "calculus",
        "difficulty": 5,
        "description": "Реши ја диференцијалната равенка: dy/dx = 2xy.",
        "solution": "dy/y = 2x dx => ln|y| = x² + C => y = Ce^(x²).",
        "curriculum_codes": ["MAT-S-G12-T1-S5", "MAT-S-G12-T2-S5"],
        "tags": ["диференцијални равенки"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g12_t4_2",
        "title": "Биномна распределба",
        "grade": 12,
        "category": "data",
        "difficulty": 4,
        "description": "Фрламе паричка 10 пати. Колкава е веројатноста точно 5 пати да падне глава?",
        "solution": "P(X=5) = (10 над 5) * (0.5)^5 * (0.5)^5 = 252 * (1/1024) ≈ 0.246.",
        "curriculum_codes": ["MAT-S-G12-T4-S2"],
        "tags": ["биномна распределба", "веројатност"],
        "created_at": datetime.now()
    }
]

def import_problems():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db["problems"]
    for p in problems:
        collection.update_one({"problem_id": p["problem_id"]}, {"$set": p}, upsert=True)
    client.close()

if __name__ == "__main__":
    import_problems()
