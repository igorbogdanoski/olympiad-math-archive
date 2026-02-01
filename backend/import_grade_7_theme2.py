import pymongo
from datetime import datetime

# Connection to the remote database
client = pymongo.MongoClient("mongodb://76.13.129.9:27035/")
db = client["olympiad_db"]
collection = db["problems"]

problems = [
    {
        "problem_id": "2026_g7_t2_s2",
        "title": "Квадрат и правоаголник",
        "grade": 7,
        "category": "geometry",
        "difficulty": 3,
        "content": "Еден квадрат и еден правоаголник имаат еднакви плоштини. Страните на правоаголникот се 4 cm и 9 cm. Колкава е должината на страната на квадратот?",
        "solution": "Плоштината на правоаголникот е $P = a \cdot b = 4 \cdot 9 = 36$ cm². Бидејќи квадратот има иста плоштина, неговата плоштина е $a_{sq}^2 = 36$. Оттука, страната на квадратот е $a_{sq} = \sqrt{36} = 6$ cm.",
        "curriculum_codes": ["MAT-O-G7-T2-S2"],
        "tags": ["квадрат", "правоаголник", "плоштина"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g7_t2_s3",
        "title": "Периметар на трапез",
        "grade": 7,
        "category": "geometry",
        "difficulty": 2,
        "content": "Кај рамнокрак трапез, основите се 12 cm и 8 cm, а кракот е 5 cm. Пресметај го периметарот на овој трапез.",
        "solution": "Периметарот на трапез е збир од сите негови страни. Бидејќи трапезот е рамнокрак, тој има две основи ($a=12$, $b=8$) и два еднакви крака ($c=5$). Периметарот е $L = a + b + 2c = 12 + 8 + 2 \cdot 5 = 20 + 10 = 30$ cm.",
        "curriculum_codes": ["MAT-O-G7-T2-S3"],
        "tags": ["трапез", "периметар"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g7_t2_s4",
        "title": "Плоштина на паралелограм",
        "grade": 7,
        "category": "geometry",
        "difficulty": 2,
        "content": "Една градина има форма на паралелограм со страна 15 m и соодветна висина спуштена кон таа страна од 8 m. Пресметај ја плоштината на градината.",
        "solution": "Плоштината на паралелограм се пресметува по формулата $P = a \cdot h_a$. Во овој случај, $P = 15 \cdot 8 = 120$ m².",
        "curriculum_codes": ["MAT-O-G7-T2-S4"],
        "tags": ["паралелограм", "плоштина"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g7_t2_s5",
        "title": "Дијагонали на ромб",
        "grade": 7,
        "category": "geometry",
        "difficulty": 3,
        "content": "Дијагоналите на еден ромб се 10 cm и 24 cm. Пресметај ја плоштината на ромбот.",
        "solution": "Плоштината на ромб преку неговите дијагонали се пресметува како половина од нивниот производ: $P = (d_1 \cdot d_2) / 2$. За овој ромб, $P = (10 \cdot 24) / 2 = 240 / 2 = 120$ cm².",
        "curriculum_codes": ["MAT-O-G7-T2-S5"],
        "tags": ["ромб", "дијагонали", "плоштина"],
        "created_at": datetime.now()
    }
]

print(f"Connecting to remote database at 76.13.129.9:27035...")
try:
    for p in problems:
        collection.delete_many({"problem_id": p["problem_id"]})
    result = collection.insert_many(problems)
    print(f"Successfully inserted {len(result.inserted_ids)} problems for Grade 7 Theme 2.")
except Exception as e:
    print(f"Error: {e}")
