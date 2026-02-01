import pymongo
from datetime import datetime

# Connection to the remote database
client = pymongo.MongoClient("mongodb://76.13.129.9:27035/")
db = client["olympiad_db"]
collection = db["problems"]

problems = [
    {
        "problem_id": "2026_g7_t3_s1",
        "title": "Табела на фреквенција",
        "grade": 7,
        "category": "algebra",
        "difficulty": 2,
        "content": "Во една група од 20 ученици е спроведена анкета за омилен спорт. Добиени се следниве резултати: Фудбал (8), Кошарка (5), Ракомет (4) и Тенис (3). Организирај ги овие податоци во табела на фреквенција и одреди го процентот на ученици кои избрале Фудбал.",
        "solution": "Табела на фреквенција:\n- Фудбал: 8\n- Кошарка: 5\n- Ракомет: 4\n- Тенис: 3\nВкупно: 20. Процентот за Фудбал е $(8 / 20) \cdot 100\% = 0.4 \cdot 100\% = 40\%$.",
        "curriculum_codes": ["MAT-O-G7-T3-S1"],
        "tags": ["статистика", "податоци", "проценти"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g7_t3_s2",
        "title": "Кружен дијаграм",
        "grade": 7,
        "category": "algebra",
        "difficulty": 3,
        "content": "Ако сакаме да ги претставиме податоците за омилен спорт (Фудбал: 8, Кошарка: 5, Ракомет: 4, Тенис: 3) со кружен дијаграм, колкав централен агол ќе одговара на секторот 'Кошарка'?",
        "solution": "Вкупниот број на ученици е 20. Целиот круг има $360^\circ$. Аголот за Кошарка се пресметува како пропорционален дел од вкупниот агол: $\alpha = (5 / 20) \cdot 360^\circ = (1 / 4) \cdot 360^\circ = 90^\circ$.",
        "curriculum_codes": ["MAT-O-G7-T3-S2"],
        "tags": ["статистика", "кружен дијаграм", "агли"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g7_t3_s3",
        "title": "Средни вредности на поени",
        "grade": 7,
        "category": "algebra",
        "difficulty": 3,
        "content": "Дадена е низа од освоени поени на еден квиз: 12, 15, 12, 18, 20, 15, 12. Одреди ги аритметичката средина, медијаната и модата на овие податоци.",
        "solution": "Прво ги подредуваме податоците: 12, 12, 12, 15, 15, 18, 20.\n1. Аритметичка средина: $(12+12+12+15+15+18+20) / 7 = 104 / 7 \approx 14.86$.\n2. Медијана: Средишниот член во подредената низа е 15.\n3. Мода: Бројот кој најчесто се повторува е 12.",
        "curriculum_codes": ["MAT-O-G7-T3-S3"],
        "tags": ["статистика", "аритметичка средина", "медијана", "мода"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g7_t3_s4",
        "title": "Веројатност со топчиња",
        "grade": 7,
        "category": "combinatorics",
        "difficulty": 3,
        "content": "Во една торба има 4 црвени, 3 сини и 5 зелени топчиња. Ако по случаен избор се извлече едно топче, колкава е веројатноста тоа да НЕ биде зелено?",
        "solution": "Вкупниот број на топчиња е $4 + 3 + 5 = 12$. Бројот на топчиња кои не се зелени (црвени или сини) е $4 + 3 = 7$. Веројатноста е $P = 7 / 12$.",
        "curriculum_codes": ["MAT-O-G7-T3-S4"],
        "tags": ["веројатност"],
        "created_at": datetime.now()
    }
]

print(f"Connecting to remote database at 76.13.129.9:27035...")
try:
    for p in problems:
        collection.delete_many({"problem_id": p["problem_id"]})
    result = collection.insert_many(problems)
    print(f"Successfully inserted {len(result.inserted_ids)} problems for Grade 7 Theme 3.")
except Exception as e:
    print(f"Error: {e}")
