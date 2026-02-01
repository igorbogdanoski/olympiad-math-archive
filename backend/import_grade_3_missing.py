import pymongo
from datetime import datetime

MONGO_URI = "mongodb://76.13.129.9:27035/"
DB_NAME = "olympiad_db"

problems = [
    {
        "problem_id": "2026_g3_t1_1",
        "title": "Слаткарницата на баба",
        "grade": 3,
        "category": "algebra",
        "difficulty": 1,
        "description": "Баба направила 4 тави со по 5 колачи. Внуците изеле 7 колачи. Колку колачи останале? Ако останатите колачи ги поделиме на 3 деца така што секое да добие ист број, колку колачи ќе останат вишок (остаток)?",
        "solution": "Вкупно колачи: 4 * 5 = 20. Останале: 20 - 7 = 13. Делење: 13 / 3 = 4 и остаток 1. Останува 1 колач вишок.",
        "curriculum_codes": ["MAT-O-G3-T1-S1", "MAT-O-G3-T1-S3", "MAT-O-G3-T1-S7", "MAT-O-G3-T1-S8"],
        "tags": ["множење", "делење со остаток", "текстуални задачи"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g3_t2_1",
        "title": "Трка со броеви до 1000",
        "grade": 3,
        "category": "algebra",
        "difficulty": 1,
        "description": "Подреди ги броевите од најмал до најголем: 405, 450, 504, 45. Кој од овие броеви е најблиску до 500 кога ќе се заокружи на најблиската стотка?",
        "solution": "Редослед: 45, 405, 450, 504. Најблиску до 500 се 450 и 504 (двата се заокружуваат на 500).",
        "curriculum_codes": ["MAT-O-G3-T2-S1", "MAT-O-G3-T2-S2", "MAT-O-G3-T2-S3", "MAT-O-G3-T2-S5"],
        "tags": ["броеви до 1000", "заокружување", "споредување"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g3_t3_1",
        "title": "Геометриска градина",
        "grade": 3,
        "category": "geometry",
        "difficulty": 1,
        "description": "Една фигура има 4 еднакви страни и сите агли ѝ се прави. Која е таа фигура? Нацртај една оска на симетрија на таа фигура. Колку вкупно оски на симетрија има таа?",
        "solution": "Фигурата е квадрат. Квадратот има вкупно 4 оски на симетрија.",
        "curriculum_codes": ["MAT-O-G3-T3-S1", "MAT-O-G3-T3-S3", "MAT-O-G3-T3-S6", "MAT-O-G3-T3-S7"],
        "tags": ["квадрат", "симетрија", "агли", "геометрија"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g3_t4_1",
        "title": "Роденденската торта",
        "grade": 3,
        "category": "logic",
        "difficulty": 1,
        "description": "Една торта е поделена на 8 еднакви парчиња. Марко изел 2 парчиња, а Ана изела 3 парчиња. Кој дел (разломок) од тортата останал? Кој изел повеќе?",
        "solution": "Вкупно изедени: 2 + 3 = 5 парчиња (5/8). Останале: 8/8 - 5/8 = 3/8. Ана изела повеќе (3/8 > 2/8).",
        "curriculum_codes": ["MAT-O-G3-T4-S1", "MAT-O-G3-T4-S2", "MAT-O-G3-T4-S3", "MAT-O-G3-T4-S4", "MAT-O-G3-T4-S5"],
        "tags": ["разломци", "споредување", "логика"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g3_t5_1",
        "title": "Мерење во училницата",
        "grade": 3,
        "category": "measurement",
        "difficulty": 1,
        "description": "Периметарот на еден правоаголник е 20 см. Ако едната страна е 6 см, колку е долга другата страна? Колку милилитри има во 2 литри вода?",
        "solution": "Периметар = 2*(а+б). 20 = 2*(6+б) => 10 = 6+б => б = 4 см. 2 литри = 2000 милилитри.",
        "curriculum_codes": ["MAT-O-G3-T5-S1", "MAT-O-G3-T5-S2", "MAT-O-G3-T5-S3", "MAT-O-G3-T5-S5"],
        "tags": ["периметар", "правоаголник", "мерни единици"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g3_t6_1",
        "title": "Времето на натпреварот",
        "grade": 3,
        "category": "logic",
        "difficulty": 1,
        "description": "Еден натпревар почнал во 10:15 и траел 75 минути. Во колку часот завршил? Колку денови има во 3 седмици и 2 дена?",
        "solution": "75 минути = 1 час и 15 минути. 10:15 + 1:15 = 11:30. Денови: 3 * 7 + 2 = 21 + 2 = 23 дена.",
        "curriculum_codes": ["MAT-O-G3-T6-S1", "MAT-O-G3-T6-S2", "MAT-O-G3-T6-S3", "MAT-O-G3-T6-S4", "MAT-O-G3-T6-S5"],
        "tags": ["време", "календар", "часовник"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g3_t1_2",
        "title": "Магичниот број 100",
        "grade": 3,
        "category": "logic",
        "difficulty": 1,
        "description": "Пресметај: 5 * 10 + 2 * 100. Ако овој број го помножиш со 0, што ќе добиеш? Кое е својството на множење со 0?",
        "solution": "50 + 200 = 250. 250 * 0 = 0. Секој број помножен со 0 е еднаков на 0.",
        "curriculum_codes": ["MAT-O-G3-T1-S4", "MAT-O-G3-T1-S5", "MAT-O-G3-T1-S6"],
        "tags": ["множење со 100", "редослед на операции", "својства на множење"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g3_t2_2",
        "title": "Загатката на градежникот",
        "grade": 3,
        "category": "logic",
        "difficulty": 1,
        "description": "Еден градежник користи 324 тули за еден ѕид. За вториот ѕид му требаат 150 тули повеќе. Колку тули му требаат вкупно за двата ѕида? Заокружи го резултатот на најблиската стотка.",
        "solution": "Втор ѕид: 324 + 150 = 474. Вкупно: 324 + 474 = 798. Заокружено: 800.",
        "curriculum_codes": ["MAT-O-G3-T2-S4", "MAT-O-G3-T2-S6", "MAT-O-G3-T2-S7", "MAT-O-G3-T1-S2"],
        "tags": ["собирање", "броеви до 1000", "заокружување"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g3_t3_final",
        "title": "Геометриски предизвик",
        "grade": 3,
        "category": "geometry",
        "difficulty": 1,
        "description": "Ана користи ленир за да нацрта отсечка долга 7 см. Потоа, од едниот крај црта агол кој е поголем од прав агол. Каков е тој агол (остар, прав или тап)? Ако Ана се сврти за еден цел круг, за колку степени се свртила?",
        "solution": "Агол поголем од 90 степени е тап агол. Цел круг има 360 степени.",
        "curriculum_codes": ["MAT-O-G3-T3-S2", "MAT-O-G3-T3-S4", "MAT-O-G3-T3-S5", "MAT-O-G3-T5-S4"],
        "tags": ["агли", "конструкции", "геометрија"],
        "created_at": datetime.now()
    }
]

def import_problems():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db["problems"]
    
    for p in problems:
        collection.update_one({"problem_id": p["problem_id"]}, {"$set": p}, upsert=True)
    
    print("✅ Успешно ажурирани/внесени задачи за 3-то одделение.")
    client.close()

if __name__ == "__main__":
    import_problems()
