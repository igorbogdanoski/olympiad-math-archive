import pymongo
from datetime import datetime

# Connection to the remote database
# Note: Using the remote IP as established in previous sessions
client = pymongo.MongoClient("mongodb://76.13.129.9:27035/")
db = client["olympiad_db"]
collection = db["problems"]

problems = [
    {
        "problem_id": "2026_g7_t1_s1",
        "title": "Процентна промена на цената",
        "grade": 7,
        "category": "algebra",
        "difficulty": 3,
        "content": "Цената на една книга прво се зголемила за 20%, а потоа новата цена се намалила за 20%. Дали крајната цена е поголема, помала или еднаква на почетната цена? Објасни зошто.",
        "solution": "Нека почетната цена е $x$. По зголемувањето од 20%, новата цена е $x + 0.20x = 1.20x$. Потоа, оваа цена се намалува за 20%: $1.20x - 0.20 \cdot (1.20x) = 1.20x - 0.24x = 0.96x$. Бидејќи $0.96x < x$, крајната цена е помала од почетната за 4%.",
        "curriculum_codes": ["MAT-O-G7-T1-S1"],
        "tags": ["проценти", "алгебра"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g7_t1_s2",
        "title": "Работници и време",
        "grade": 7,
        "category": "algebra",
        "difficulty": 3,
        "content": "Ако 3 работници можат да офарбаат една ограда за 8 часа, колку време ќе им биде потребно на 4 работници за да ја завршат истата работа, под услов сите да работат со исто темпо?",
        "solution": "Ова е проблем со обратнопропорционални големини. Вкупната работа изразена во работни часови е $3 \cdot 8 = 24$ работни часови. Ако работат 4 работници, времето $t$ е: $4 \cdot t = 24$, односно $t = 24 / 4 = 6$ часа.",
        "curriculum_codes": ["MAT-O-G7-T1-S2"],
        "tags": ["пропорција", "обратна пропорција"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g7_t1_s3",
        "title": "Резултат на тест",
        "grade": 7,
        "category": "algebra",
        "difficulty": 2,
        "content": "Еден ученик точно одговорил на 85% од прашањата на еден тест. Ако тој имал 34 точни одговори, колку вкупно прашања имало на тестот?",
        "solution": "Нека вкупниот број прашања е $n$. Имаме равенка: $0.85 \cdot n = 34$. Од тука, $n = 34 / 0.85 = 3400 / 85 = 40$. Значи, на тестот имало 40 прашања.",
        "curriculum_codes": ["MAT-O-G7-T1-S3"],
        "tags": ["проценти", "текстуални задачи"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g7_t1_s4",
        "title": "Растојание на мапа",
        "grade": 7,
        "category": "algebra",
        "difficulty": 3,
        "content": "На географска карта со размер 1:50,000, растојанието меѓу две населени места е 4.5 cm. Колкаво е вистинското растојание меѓу тие места во километри?",
        "solution": "Размерот 1:50,000 значи дека 1 cm на мапата одговара на 50,000 cm во реалноста. Вистинското растојание е $4.5 \cdot 50,000 = 225,000$ cm. Бидејќи $100$ cm = $1$ m и $1,000$ m = $1$ km, имаме $225,000$ cm = $2,250$ m = $2.25$ km.",
        "curriculum_codes": ["MAT-O-G7-T1-S4"],
        "tags": ["размер", "скалирање"],
        "created_at": datetime.now()
    },
    {
        "problem_id": "2026_g7_t1_s5",
        "title": "Едноставна камата",
        "grade": 7,
        "category": "algebra",
        "difficulty": 4,
        "content": "Марко вложил 12,000 денари во банка со годишна каматна стапка од 5%. Колку пари ќе има Марко на својата сметка по 3 години, ако се пресметува едноставна камата?",
        "solution": "Едноставната камата $K$ се пресметува по формулата $K = G \cdot p \cdot t$, каде $G$ е главницата, $p$ е каматната стапка и $t$ е времето во години. $K = 12,000 \cdot 0.05 \cdot 3 = 600 \cdot 3 = 1,800$ денари. Вкупната сума ќе биде $12,000 + 1,800 = 13,800$ денари.",
        "curriculum_codes": ["MAT-O-G7-T1-S5"],
        "tags": ["камата", "проценти"],
        "created_at": datetime.now()
    }
]

print(f"Connecting to remote database at 76.13.129.9...")
try:
    # Delete existing if needed to avoid duplicates during development
    for p in problems:
        collection.delete_many({"problem_id": p["problem_id"]})
    
    result = collection.insert_many(problems)
    print(f"Successfully inserted {len(result.inserted_ids)} problems for Grade 7 Theme 1.")
except Exception as e:
    print(f"Error: {e}")
