import pymongo

# Macedonian Mathematics Curriculum Database Seeder
# Grade IV (4th Grade) - Filling the Foundation Gap

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["olympiad_archive"]
collection = db["curricula"]

grade_4_data = {
    "grade_level": "IV",
    "year_description": "Четврто одделение (Деветгодишно образование)",
    "source": "ЛЕКТУРА-Математика-4.pdf",
    "themes": [
        {
            "id": "броеви_и_броење",
            "title": "БРОЕВИ И БРОЕЊЕ",
            "objectives": [
                "Clothesline number placement with 3-4 digit numbers",
                "Bingo game with 4-digit number reading",
                "Number line positioning for multi-digit numbers",
                "Counting by hundreds, thousands forward and backward",
                "Creating and extending number sequences",
                "Place value understanding (10, 100, 1000 more/less)",
                "Largest/smallest number formation with dice",
                "Place value pattern recognition",
                "Expanded form calculations",
                "Number comparison with symbols",
                "Rounding to nearest ten or hundred",
                "Negative numbers on thermometer scale",
                "Elevator game with positive/negative movement",
                "Fraction equivalence through paper folding",
                "Decimal number ordering on number lines",
                "Fraction of a number activities",
                "Decimal number construction games",
                "Even/odd number identification",
                "Place value acrostic poems",
                "Online quiz reinforcement"
            ]
        },
        {
            "id": "геометрија",
            "title": "ГЕОМЕТРИЈА",
            "objectives": [
                "Angle comparison relative to right angle",
                "Quadrilateral formation and classification",
                "Regular polygon identification",
                "Shape construction with given constraints",
                "Kite construction and analysis",
                "Symmetry line discovery through folding",
                "Angle rotation exploration (180°, 360°)",
                "Directional movement treasure hunt",
                "Clock angle reading and measurement",
                "Symmetry axis counting",
                "Perimeter calculation activities",
                "Shape property matching games",
                "Symmetry line identification",
                "Coordinate system location marking",
                "Coordinate movement problem solving"
            ]
        },
        {
            "id": "операции_со_броеви",
            "title": "ОПЕРАЦИИ СО БРОЕВИ",
            "objectives": [
                "Number pair finding (sums to 10, 20, 100, 1000)",
                "Addition problem solving to 10,000",
                "Addition strategies discussion",
                "Task hunt with addition problems",
                "Word problem creation and peer review",
                "Mental math speed challenges",
                "Story problem solutions",
                "Subtraction analysis and strategies",
                "Inverse operation verification",
                "Doubling and halving explorations",
                "Dice multiplication games",
                "Multiplication table pattern discovery",
                "Scale and map ratio work",
                "Divisor pattern recognition",
                "Multiplication chain questions",
                "Division word problems",
                "Powers of 10 rules",
                "Fraction equivalence matching",
                "Fraction intruder identification",
                "Recipe adjustment problems",
                "Fraction of a number understanding"
            ]
        },
        {
            "id": "мерење",
            "title": "МЕРЕЊЕ",
            "objectives": [
                "Length estimation and measurement",
                "Jump distance measurement activities",
                "Liquid volume measurement",
                "Time duration timing",
                "Calendar date finding",
                "Personal calendar creation",
                "Supermarket role-play with measurements",
                "Mass measurement activities",
                "Time calculation problems",
                "Measurement grouping by type",
                "Wire model perimeter measurement",
                "Equal area different perimeter exploration",
                "Online measurement tools",
                "True/false measurement statements",
                "Unit conversion word problems",
                "Real-world measurement applications",
                "Story adaptation with math context"
            ]
        },
        {
            "id": "работа_со_податоци",
            "title": "РАБОТА СО ПОДАТОЦИ",
            "objectives": [
                "Group research planning and execution",
                "Long jump data collection and graphing",
                "Pictogram creation with scaling",
                "Dart game data analysis",
                "Peer survey and comparison",
                "Diagram interpretation practice",
                "Color pencil graph reading",
                "Weather data collection and analysis",
                "Interactive diagram websites",
                "Error identification in diagrams",
                "Diagram storytelling without labels",
                "Probability experiments with marbles",
                "Event classification (certain, possible, impossible)"
            ]
        }
    ],
    "last_updated": "2026-01-20",
    "data_quality": "clean_manual_import"
}

# Execute database operations
print(f"DELETE: Deleting existing data for grade: {grade_4_data['grade_level']}...")
collection.delete_many({"grade_level": grade_4_data['grade_level']})

print(f"INSERT: Inserting comprehensive data for IV grade...")
result = collection.insert_one(grade_4_data)

total_objectives = sum(len(theme.get('objectives', [])) for theme in grade_4_data['themes'])

print(f"SUCCESS: Successfully imported grade {grade_4_data['grade_level']}!")
print(f"  - {len(grade_4_data['themes'])} themes")
print(f"  - {total_objectives} detailed objectives")
print(f"  - Source: Mathematics Grade 4 Textbook")
print()
print("Now refresh your browser and click on 'IV' to see the curriculum with activities!")

if __name__ == "__main__":
    print("Grade IV curriculum seeding complete!")