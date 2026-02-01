import pymongo
from datetime import datetime

# Connection to the remote database
client = pymongo.MongoClient("mongodb://76.13.129.9:27035/")
db = client["olympiad_db"]
collection = db["problems"]

problems = [
    {
        "problem_id": "2026_g9_t1_s1",
        "title": "Линеарна функција и нула",
        "grade": 9,
        "category": "algebra",
        "difficulty": 2,
        "content": "Одреди ја нулата на линеарната функција $f(x) = 3x - 12$. Што претставува таа точка на графикот?",
        "solution": "Нулата на функцијата се наоѓа кога $f(x) = 0$. Имаме $3x - 12 = 0$, односно $3x = 12$, па $x = 4$. Точката $(4, 0)$ е пресекот на графикот со x-оската.",
        "curriculum_codes": ["MAT-O-G9-T1-S1"],
        "tags": ["функции", "линеарна функција", "нула"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g9_t1_s2",
        "title": "Теме на квадратна функција",
        "grade": 9,
        "category": "algebra",
        "difficulty": 4,
        "content": "Одреди ги координатите на темето на параболата $f(x) = x^2 - 4x + 5$. Дали таа точка е минимум или максимум на функцијата?",
        "solution": "Координатите на темето $(h, k)$ се $h = -b / (2a) = 4 / 2 = 2$. Тогаш $k = f(2) = 2^2 - 4(2) + 5 = 4 - 8 + 5 = 1$. Темето е во точката $(2, 1)$. Бидејќи $a=1 > 0$, параболата е свртена нагоре, па темето е точка на минимум.",
        "curriculum_codes": ["MAT-O-G9-T1-S2"],
        "tags": ["функции", "квадратна функција", "теме"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g9_t1_s3",
        "title": "Пресек на парабола и права",
        "grade": 9,
        "category": "algebra",
        "difficulty": 5,
        "content": "Одреди ги пресечните точки на графикот на функцијата $f(x) = x^2$ и правата $y = x + 2$.",
        "solution": "Ги изедначуваме изразите: $x^2 = x + 2$, т.е. $x^2 - x - 2 = 0$. Користиме квадратна формула: $x = (1 \pm \sqrt{1 + 8}) / 2 = (1 \pm 3) / 2$. Решенијата се $x_1 = 2$ и $x_2 = -1$. Соодветните y-координати се $y_1 = 2^2 = 4$ и $y_2 = (-1)^2 = 1$. Пресечните точки се $(2, 4)$ и $(-1, 1)$.",
        "curriculum_codes": ["MAT-O-G9-T1-S3"],
        "tags": ["функции", "график", "пресек"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g9_t1_s4",
        "title": "Домен на рационална функција",
        "grade": 9,
        "category": "algebra",
        "difficulty": 3,
        "content": "Одреди го дефиниционото подрачје (доменот) на функцијата $f(x) = \frac{x-1}{x^2 - 9}$.",
        "solution": "Именителот не смее да биде нула: $x^2 - 9 \neq 0$, што значи $x^2 \neq 9$, па $x \neq 3$ и $x \neq -3$. Доменот е $D = \mathbb{R} \setminus \{-3, 3\}$.",
        "curriculum_codes": ["MAT-O-G9-T1-S4"],
        "tags": ["функции", "домен"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g9_t1_s5",
        "title": "Транслација на функција",
        "grade": 9,
        "category": "algebra",
        "difficulty": 4,
        "content": "Ако графикот на функцијата $f(x) = x^2$ се транслатира за 3 единици надесно и 2 единици нагоре, која е равенката на новата функција $g(x)$?",
        "solution": "Транслација за $h$ единици надесно ја менува променливата во $(x-h)$, а транслација за $k$ единици нагоре додава $k$ на функцијата. Новата равенка е $g(x) = (x - 3)^2 + 2$.",
        "curriculum_codes": ["MAT-O-G9-T1-S5"],
        "tags": ["функции", "трансформации"],
        "created_at": datetime.now()
    }
]

print(f"Connecting to remote database at 76.13.129.9:27035...")
try:
    for p in problems:
        collection.delete_many({"problem_id": p["problem_id"]})
    result = collection.insert_many(problems)
    print(f"Successfully inserted {len(result.inserted_ids)} problems for Grade 9 Theme 1.")
except Exception as e:
    print(f"Error: {e}")
