import pymongo
from datetime import datetime

# Connection to the remote database
client = pymongo.MongoClient("mongodb://76.13.129.9:27035/")
db = client["olympiad_db"]
collection = db["problems"]

problems = [
    {
        "problem_id": "2026_g9_t3_s1",
        "title": "Пермутации со повторување",
        "grade": 9,
        "category": "combinatorics",
        "difficulty": 3,
        "content": "На колку различни начини можат да се подредат буквите од зборот 'МАТЕМАТИКА'?",
        "solution": "Зборот има 10 букви: М(2), А(3), Т(2), Е(1), И(1), К(1). Бројот на пермутации со повторување е $P = \frac{10!}{2! \cdot 3! \cdot 2!} = \frac{3628800}{2 \cdot 6 \cdot 2} = \frac{3628800}{24} = 151200$.",
        "curriculum_codes": ["MAT-O-G9-T3-S1"],
        "tags": ["комбинаторика", "пермутации"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g9_t3_s3",
        "title": "Биномна веројатност",
        "grade": 9,
        "category": "combinatorics",
        "difficulty": 4,
        "content": "Колкава е веројатноста при 5 фрлања на фер паричка, точно 3 пати да падне 'писмо'?",
        "solution": "Ова е Биномна распределба со $n=5, k=3, p=0.5$. Формулата е $P(X=k) = \binom{n}{k} p^k (1-p)^{n-k}$. Имаме $\binom{5}{3} = 10$. Веројатноста е $10 \cdot (0.5)^3 \cdot (0.5)^2 = 10 \cdot (0.5)^5 = 10 / 32 = 5 / 16 = 0.3125$.",
        "curriculum_codes": ["MAT-O-G9-T3-S3"],
        "tags": ["веројатност", "биномна распределба"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g9_t3_s4",
        "title": "Стандардна девијација",
        "grade": 9,
        "category": "algebra",
        "difficulty": 4,
        "content": "Дадени се податоците: 2, 4, 6, 8, 10. Пресметај ја нивната варијанса и стандардна девијација.",
        "solution": "Аритметичка средина е $\bar{x} = (2+4+6+8+10) / 5 = 6$. Варијансата е $\sigma^2 = \frac{\sum (x_i - \bar{x})^2}{n} = \frac{(2-6)^2 + (4-6)^2 + (6-6)^2 + (8-6)^2 + (10-6)^2}{5} = \frac{16+4+0+4+16}{5} = 40 / 5 = 8$. Стандардна девијација е $\sigma = \sqrt{8} \approx 2.83$.",
        "curriculum_codes": ["MAT-O-G9-T3-S4"],
        "tags": ["статистика", "стандардна девијација"],
        "created_at": datetime.now()
    }
]

print(f"Connecting to remote database at 76.13.129.9:27035...")
try:
    for p in problems:
        collection.delete_many({"problem_id": p["problem_id"]})
    result = collection.insert_many(problems)
    print(f"Successfully inserted {len(result.inserted_ids)} problems for Grade 9 Theme 3.")
except Exception as e:
    print(f"Error: {e}")
