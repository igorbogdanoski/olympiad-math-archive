import pymongo
from datetime import datetime

MONGO_URI = "mongodb://76.13.129.9:27035/"
DB_NAME = "olympiad_db"

problems = [
    {
        "problem_id": "2026_g1_t3_1",
        "title": "Магичните стапки на зајачето",
        "grade": 1,
        "category": "measurement",
        "difficulty": 1,
        "description": "Едно зајаче ја мери должината на патеката со своите скокови. Ако еден скок на зајачето е колку две стапки на ежот, колку стапки на ежот се 5 скокови на зајачето?",
        "solution": "Ако 1 скок = 2 стапки, тогаш 5 скокови = 5 * 2 = 10 стапки на ежот.",
        "curriculum_codes": ["MAT-O-G1-T3-S6", "MAT-O-G1-T3-S7"],
        "tags": ["мерење", "логика", "споредување"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g1_t4_1",
        "title": "Времето на Марко",
        "grade": 1,
        "category": "logic",
        "difficulty": 1,
        "description": "Ако вчера беше понеделник, кој ден ќе биде задутре?",
        "solution": "Ако вчера беше понеделник, денес е вторник. Утре е среда, а задутре е четврток.",
        "curriculum_codes": ["MAT-O-G1-T4-S1", "MAT-O-G1-T4-S2", "MAT-O-G1-T4-S5"],
        "tags": ["време", "денови во неделата", "логика"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g1_t4_2",
        "title": "Дневниот распоред на Ана",
        "grade": 1,
        "category": "logic",
        "difficulty": 1,
        "description": "Ана оди на училиште во 8 часот наутро. Таа си доаѓа дома по 4 часа. Во колку часот Ана се враќа дома?",
        "solution": "8 часот + 4 часа = 12 часот.",
        "curriculum_codes": ["MAT-O-G1-T4-S4", "MAT-O-G1-T4-S7"],
        "tags": ["часовник", "собирање", "време"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g1_t5_1",
        "title": "Овошната градина",
        "grade": 1,
        "category": "data",
        "difficulty": 1,
        "description": "Во една кошница има 3 јаболка, 5 круши и 2 банани. Нацртај со цртички колку овошја има од секој вид. Кое овошје го има најмногу?",
        "solution": "Јаболка: |||, Круши: |||||, Банани: ||. Најмногу има круши.",
        "curriculum_codes": ["MAT-O-G1-T5-S1", "MAT-O-G1-T5-S2", "MAT-O-G1-T5-S3"],
        "tags": ["податоци", "бројање", "графикони"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g1_t5_2",
        "title": "Шарените коцки",
        "grade": 1,
        "category": "logic",
        "difficulty": 1,
        "description": "Петар има црвени и сини коцки. Некои се големи, а некои се мали. На колку начини може да ги подреди коцките во групи ако сака да бидат исти по боја И по големина?",
        "solution": "Може да ги подреди во 4 групи: големи црвени, мали црвени, големи сини и мали сини.",
        "curriculum_codes": ["MAT-O-G1-T5-S4", "MAT-O-G1-T5-S5"],
        "tags": ["групирање", "класификација", "множества"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g1_t6_1",
        "title": "Математика во прошетка",
        "grade": 1,
        "category": "logic",
        "difficulty": 1,
        "description": "На една патека има наредено камења во боја: црвен, син, црвен, син... Која боја ќе биде 10-тиот камен?",
        "solution": "Бидејќи боите се менуваат наизменично (непарен број = црвен, парен број = син), 10-тиот камен е парен, па затоа ќе биде син.",
        "curriculum_codes": ["MAT-O-G1-T6-S1", "MAT-O-G1-T6-S4", "MAT-O-G1-T6-S5"],
        "tags": ["шаблони", "низи", "секојдневна математика"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g1_t4_3",
        "title": "Роденденот на Дамјан",
        "grade": 1,
        "category": "logic",
        "difficulty": 1,
        "description": "Дамјан е роден во месецот што доаѓа веднаш по мај. Кој е тој месец? Ако денес е 1-ви јуни, а неговиот роденден е по точно една недела, на кој датум е неговиот роденден?",
        "solution": "Месецот по мај е јуни. Ако денес е 1-ви јуни, по една недела (7 дена) ќе биде 8-ми јуни.",
        "curriculum_codes": ["MAT-O-G1-T4-S3", "MAT-O-G1-T4-S6"],
        "tags": ["месеци", "календар", "датуми"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g1_t6_2",
        "title": "Математички натпревар",
        "grade": 1,
        "category": "logic",
        "difficulty": 1,
        "description": "Во еден фудбалски натпревар, тимот 'Лавови' постигна 3 гола во првото полувреме и 2 гола во второто. Колку вкупно голови постигна тимот? Ако за секоја торта што ја прават во кујната им требаат 2 јајца, колку јајца им требаат за 3 такви торти?",
        "solution": "3 + 2 = 5 гола вкупно. За 3 торти им требаат 2 + 2 + 2 = 6 јајца.",
        "curriculum_codes": ["MAT-O-G1-T6-S2", "MAT-O-G1-T6-S3"],
        "tags": ["бројање", "спорт", "кујна"],
        "created_at": datetime.now()
    }
]

def import_problems():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db["problems"]
    
    # Avoid duplicates if script is re-run
    for p in problems:
        collection.update_one({"problem_id": p["problem_id"]}, {"$set": p}, upsert=True)
    
    print(f"✅ Успешно ажурирани/внесени задачи за 1-во одделение.")
    client.close()

if __name__ == "__main__":
    import_problems()
