import pymongo
from datetime import datetime

MONGO_URI = "mongodb://76.13.129.9:27035/"
DB_NAME = "olympiad_db"

problems = [
    {
        "problem_id": "2026_g11_t1_1",
        "title": "Тригонометриски идентитети",
        "grade": 11,
        "category": "trigonometry",
        "difficulty": 4,
        "description": "Докажи го идентитетот: sin(α+β) * sin(α-β) = sin²α - sin²β користејќи ги адионите теореми.",
        "solution": "sin(α+β) = sinα cosβ + cosα sinβ; sin(α-β) = sinα cosβ - cosα sinβ. Нивниот производ е (sinα cosβ)² - (cosα sinβ)² = sin²α cos²β - cos²α sin²β = sin²α(1-sin²β) - (1-sin²α)sin²β = sin²α - sin²α sin²β - sin²β + sin²α sin²β = sin²α - sin²β.",
        "curriculum_codes": ["MAT-S-G11-T1-S2"],
        "tags": ["тригонометрија", "идентитети", "адициони теореми"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g11_t2_1",
        "title": "Логаритамски равенки и модели",
        "grade": 11,
        "category": "algebra",
        "difficulty": 4,
        "description": "Реши ја равенката: log₂(x+2) + log₂(x-1) = 2. Како може логаритамската функција да се користи за моделирање на јачина на звук (dB)?",
        "solution": "log₂((x+2)(x-1)) = 2 => (x+2)(x-1) = 2² = 4 => x² + x - 2 = 4 => x² + x - 6 = 0. (x+3)(x-2) = 0. x = 2 (бидејќи x мора да биде > 1). Јачината на звук L се моделира со L = 10 * log₁₀(I/I₀).",
        "curriculum_codes": ["MAT-S-G11-T2-S3", "MAT-S-G11-T2-S6"],
        "tags": ["логаритми", "моделирање", "равенки"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g11_t3_1",
        "title": "Граници и бесконечни редови",
        "grade": 11,
        "category": "calculus",
        "difficulty": 4,
        "description": "Најди ја збирот на бесконечниот геометриски ред: 1 + 1/3 + 1/9 + ... + (1/3)^n + ... Пресметај ја границата lim (n→∞) (2n+1)/(3n-2).",
        "solution": "За редот a=1, q=1/3. S = a/(1-q) = 1/(1 - 1/3) = 1/(2/3) = 3/2. За границата: делење со n => lim (2 + 1/n) / (3 - 2/n) = 2/3.",
        "curriculum_codes": ["MAT-S-G11-T3-S3", "MAT-S-G11-T3-S4"],
        "tags": ["низи", "граница", "геометриски ред"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g11_t4_1",
        "title": "Векторски и мешан производ",
        "grade": 11,
        "category": "vectors",
        "difficulty": 4,
        "description": "Дадени се векторите a = (1, 2, 0) и b = (0, 1, 3). Пресметај го нивниот векторски производ a x b. Која е геометриската смисла на мешаниот производ (a x b) · c?",
        "solution": "a x b = (2*3-0*1, 0*0-1*3, 1*1-2*0) = (6, -3, 1). Мешаниот производ претставува волумен на паралелопипедот конструиран над трите вектори.",
        "curriculum_codes": ["MAT-S-G11-T4-S1", "MAT-S-G11-T4-S3", "MAT-S-G11-T4-S4", "MAT-S-G11-T4-S5"],
        "tags": ["вектори", "векторски производ", "волумен"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g11_t5_1",
        "title": "Комплексни броеви во поларна форма",
        "grade": 11,
        "category": "algebra",
        "difficulty": 4,
        "description": "Претстави го комплексниот број z = 1 + i во поларна (тригонометриска) форма.",
        "solution": "Модул r = √(1² + 1²) = √2. Аргумент φ: tanφ = 1/1 = 1 => φ = π/4. z = √2(cos(π/4) + i sin(π/4)).",
        "curriculum_codes": ["MAT-S-G11-T5-S5"],
        "tags": ["комплексни броеви", "поларна форма"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g11_t6_1",
        "title": "Системи и матрици",
        "grade": 11,
        "category": "algebra",
        "difficulty": 4,
        "description": "Реши го системот равенки користејќи го Крамеровото правило: x + y = 3, 2x - y = 0. Објасни кога една матрица има инверзна матрица.",
        "solution": "D = |1 1; 2 -1| = -1 - 2 = -3. Dx = |3 1; 0 -1| = -3. Dy = |1 3; 2 0| = -6. x = -3/-3 = 1, y = -6/-3 = 2. Матрицата има инверзна ако е квадратна и нејзината детерминанта е различна од нула (несингуларна).",
        "curriculum_codes": ["MAT-S-G11-T6-S1", "MAT-S-G11-T6-S2", "MAT-S-G11-T6-S3", "MAT-S-G11-T6-S4", "MAT-S-G11-T6-S5", "MAT-S-G11-T3-S5", "MAT-S-G11-T3-S6"],
        "tags": ["матрици", "детерминанти", "Крамерово правило"],
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
