import pymongo
from datetime import datetime

MONGO_URI = "mongodb://76.13.129.9:27035/"
DB_NAME = "olympiad_db"

problems = [
    {
        "problem_id": "2026_g4_t1_1",
        "title": "Библиотеката на училиштето",
        "grade": 4,
        "category": "algebra",
        "difficulty": 2,
        "description": "Во една библиотека има 845 книги. Ако се купат уште 155 книги, колку вкупно книги ќе има? Заокружи го резултатот на најблиската илјада. Колку десетици има во овој број?",
        "solution": "845 + 155 = 1000. Заокружено на илјада е 1000. Во 1000 има 100 десетици.",
        "curriculum_codes": ["MAT-O-G4-T1-S1", "MAT-O-G4-T1-S2", "MAT-O-G4-T1-S3", "MAT-O-G4-T1-S7"],
        "tags": ["броеви до 1000", "собирање", "заокружување"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g4_t2_1",
        "title": "Оградата на дворот",
        "grade": 4,
        "category": "geometry",
        "difficulty": 2,
        "description": "Еден правоаголен двор има должина 12 метри и ширина 8 метри. Колкав е периметарот на дворот? Ако сакаме да го покриеме дворот со плочки, колкава површина (плоштина) треба да покриеме?",
        "solution": "Периметар = 2*(12 + 8) = 40 метри. Плоштина = 12 * 8 = 96 метри квадратни.",
        "curriculum_codes": ["MAT-O-G4-T2-S3", "MAT-O-G4-T2-S4", "MAT-O-G4-T2-S7"],
        "tags": ["периметар", "плоштина", "правоаголник"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g4_t3_1",
        "title": "Поделба на бонбони",
        "grade": 4,
        "category": "algebra",
        "difficulty": 2,
        "description": "Имаме 96 бонбони кои треба да ги поделиме на 12 деца. Колку бонбони ќе добие секое дете? Провери го резултатот со множење.",
        "solution": "96 / 12 = 8 бонбони. Проверка: 8 * 12 = 96.",
        "curriculum_codes": ["MAT-O-G4-T3-S2", "MAT-O-G4-T3-S3", "MAT-O-G4-T3-S4", "MAT-O-G4-T3-S5"],
        "tags": ["делење", "проверка", "текстуални задачи"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g4_t4_1",
        "title": "Пица за пријателите",
        "grade": 4,
        "category": "algebra",
        "difficulty": 2,
        "description": "Јован изел 1/2 од една пица, а Марко изел 2/4 од истата пица. Кој изел повеќе? Објасни зошто.",
        "solution": "И двајцата изеле исто. 1/2 и 2/4 се еквивалентни (еднакви) разломци бидејќи 2/4 може да се скрати со 2 и да се добие 1/2.",
        "curriculum_codes": ["MAT-O-G4-T4-S1", "MAT-O-G4-T4-S2", "MAT-O-G4-T4-S3"],
        "tags": ["разломци", "еквивалентни разломци", "споредување"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g4_t4_2",
        "title": "Мерење со разломци",
        "grade": 4,
        "category": "measurement",
        "difficulty": 2,
        "description": "Во едно шише има 3/4 литри сок. Ако испиеме 1/4 литри, колку сок ќе остане? Ако имаме 1 цел литар и 1/2 литар, колку вкупно четвртини (1/4) литри имаме?",
        "solution": "3/4 - 1/4 = 2/4 = 1/2 литри. 1 и 1/2 литри = 3/2 литри = 6/4 литри. Имаме вкупно 6 четвртини.",
        "curriculum_codes": ["MAT-O-G4-T4-S4", "MAT-O-G4-T4-S5", "MAT-O-G4-T1-S4"],
        "tags": ["разломци", "собирање", "одземање", "мерење"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g4_t1_2",
        "title": "Проценка на пазарот",
        "grade": 4,
        "category": "logic",
        "difficulty": 2,
        "description": "Мајка му на Петар купила 3 производи кои чинат 195, 298 и 405 денари. Процени го вкупниот износ со заокружување на секој број на најблиската стотка. Дали вистинскиот износ е поголем или помал од проценката?",
        "solution": "Проценка: 200 + 300 + 400 = 900 денари. Вистински износ: 195 + 298 + 405 = 898 денари. Вистинскиот износ е помал од проценката.",
        "curriculum_codes": ["MAT-O-G4-T1-S5", "MAT-O-G4-T1-S6"],
        "tags": ["проценка", "заокружување", "собирање"],
        "created_at": datetime.now()
    }
]

def import_problems():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db["problems"]
    
    for p in problems:
        collection.update_one({"problem_id": p["problem_id"]}, {"$set": p}, upsert=True)
    
    print("✅ Успешно ажурирани/внесени задачи за 4-то одделение.")
    client.close()

if __name__ == "__main__":
    import_problems()
