#!/usr/bin/env python3
"""
Data Generator for Scalability Testing

Generates increasing volumes of test data for PostgreSQL and MongoDB
to test database performance under different data scales.
"""

import argparse
import psycopg2
import random
import string
from pymongo import MongoClient
from pymongo.errors import BulkWriteError
import time
import os
from typing import List, Dict, Any

class DataGenerator:
    def __init__(self, scale_factor: int = 1):
        self.scale_factor = scale_factor

        # Database connections
        self.pg_conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            port=int(os.getenv('POSTGRES_PORT', 5432)),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'postgres'),
            database=os.getenv('POSTGRES_DB', 'olympiad_core')
        )

        mongo_uri = f"mongodb://{os.getenv('MONGO_USER', 'admin')}:{os.getenv('MONGO_PASSWORD', 'securepassword123')}@{os.getenv('MONGO_HOST', 'localhost')}:{os.getenv('MONGO_PORT', 27017)}/{os.getenv('MONGO_DB', 'olympiad_db')}?authSource=admin"
        self.mongo_client = MongoClient(mongo_uri)
        self.mongo_db = self.mongo_client[os.getenv('MONGO_DB', 'olympiad_db')]

    def generate_students(self, count: int) -> List[Dict[str, Any]]:
        """Generate student data for PostgreSQL."""
        students = []
        for i in range(count):
            student = {
                'school_id': random.randint(1, 100 * self.scale_factor),
                'name': f"Student_{i}_{random.choice(['Smith', 'Johnson', 'Williams', 'Brown', 'Jones'])}",
                'grade': random.randint(1, 12),
                'performance_score': random.uniform(0, 100)
            }
            students.append(student)
        return students

    def generate_curriculum_problems(self, count: int) -> List[Dict[str, Any]]:
        """Generate curriculum problem data."""
        problems = []
        subjects = ['algebra', 'geometry', 'combinatorics', 'number_theory', 'calculus']
        difficulties = ['easy', 'medium', 'hard', 'expert']

        for i in range(count):
            problem = {
                'problem_id': f"prob_{i}_{self.scale_factor}",
                'school_id': random.randint(1, 100 * self.scale_factor),
                'title': f"Problem {i}: {random.choice(['Solve for x', 'Find the area', 'Prove that', 'Calculate'])}",
                'subject': random.choice(subjects),
                'difficulty': random.choice(difficulties),
                'grade_level': random.randint(1, 12),
                'content': self.generate_problem_content(),
                'solution': self.generate_solution_content(),
                'tags': random.sample(['olympiad', 'contest', 'practice', 'theory', 'application'], k=random.randint(1, 3))
            }
            problems.append(problem)
        return problems

    def generate_problem_content(self) -> str:
        """Generate random problem content."""
        templates = [
            "Find all solutions to the equation {equation}.",
            "Prove that in triangle ABC, {property}.",
            "Determine the number of ways to {action}.",
            "Calculate the value of {expression}."
        ]
        return random.choice(templates).format(
            equation=f"x^2 + {random.randint(1,10)}x + {random.randint(1,10)} = 0",
            property="the sum of angles equals 180 degrees",
            action=f"arrange {random.randint(1,10)} distinct objects",
            expression=f"∫_{random.randint(0,5)}^{random.randint(6,10)} x dx"
        )

    def generate_solution_content(self) -> str:
        """Generate random solution content."""
        return f"Solution: Using {random.choice(['algebraic manipulation', 'geometric properties', 'combinatorial counting', 'integration by parts'])}, we can show that the answer is {random.randint(1,100)}."

    def generate_mongo_content(self, count: int) -> List[Dict[str, Any]]:
        """Generate content data for MongoDB."""
        contents = []
        content_types = ['generated', 'rendered', 'localization']
        languages = ['en', 'es', 'fr', 'de', 'zh']

        for i in range(count):
            content = {
                'school_id': random.randint(1, 100 * self.scale_factor),
                'content_type': random.choice(content_types),
                'content_id': f"content_{i}_{self.scale_factor}",
                'title': f"Content Title {i}",
                'body': self.generate_large_text(random.randint(500, 2000)),
                'metadata': {
                    'language': random.choice(languages),
                    'difficulty': random.choice(['easy', 'medium', 'hard']),
                    'subject': random.choice(['math', 'physics', 'chemistry']),
                    'grade_level': random.randint(1, 12),
                    'tags': random.sample(['interactive', 'video', 'text', 'diagram'], k=random.randint(1, 3))
                },
                'created_at': time.time() - random.randint(0, 365*24*3600),  # Random time in last year
                'version': random.randint(1, 5),
                'access_count': random.randint(0, 1000)
            }
            contents.append(content)
        return contents

    def generate_large_text(self, length: int) -> str:
        """Generate large text content."""
        words = ['mathematics', 'problem', 'solution', 'equation', 'theorem', 'proof', 'calculate', 'determine', 'prove', 'find']
        text = []
        while len(' '.join(text)) < length:
            sentence = ' '.join(random.choices(words, k=random.randint(5, 15))) + '.'
            text.append(sentence.capitalize())
        return ' '.join(text)[:length]

    def insert_postgres_data(self, students: List[Dict], problems: List[Dict]):
        """Insert data into PostgreSQL."""
        print(f"Inserting {len(students)} students and {len(problems)} problems into PostgreSQL...")

        with self.pg_conn.cursor() as cursor:
            # Insert students
            for student in students:
                cursor.execute("""
                    INSERT INTO test_students (school_id, name)
                    VALUES (%s, %s)
                    ON CONFLICT DO NOTHING
                """, (student['school_id'], student['name']))

            # Insert problems
            for problem in problems:
                cursor.execute("""
                    INSERT INTO curriculum_problems (problem_id, school_id, title, subject, difficulty, grade_level, content, solution, tags)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (problem_id) DO NOTHING
                """, (
                    problem['problem_id'], problem['school_id'], problem['title'],
                    problem['subject'], problem['difficulty'], problem['grade_level'],
                    problem['content'], problem['solution'], problem['tags']
                ))

            self.pg_conn.commit()

        print("PostgreSQL data insertion complete.")

    def insert_mongo_data(self, contents: List[Dict]):
        """Insert data into MongoDB."""
        print(f"Inserting {len(contents)} content documents into MongoDB...")

        try:
            collection = self.mongo_db.generated_content
            result = collection.insert_many(contents, ordered=False)
            print(f"Inserted {len(result.inserted_ids)} documents into MongoDB.")
        except BulkWriteError as e:
            print(f"Bulk write error: {e.details}")
            # Some documents might have failed due to duplicates, but that's okay for testing

    def setup_tables(self):
        """Create necessary tables if they don't exist."""
        print("Setting up database tables...")

        with self.pg_conn.cursor() as cursor:
            # Create test_students table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS test_students (
                    student_id SERIAL PRIMARY KEY,
                    school_id INTEGER NOT NULL,
                    name VARCHAR(100),
                    grade INTEGER,
                    performance_score FLOAT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Create curriculum_problems table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS curriculum_problems (
                    problem_id VARCHAR(50) PRIMARY KEY,
                    school_id INTEGER NOT NULL,
                    title VARCHAR(200),
                    subject VARCHAR(50),
                    difficulty VARCHAR(20),
                    grade_level INTEGER,
                    content TEXT,
                    solution TEXT,
                    tags TEXT[],
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Distribute tables (ignore errors if already distributed)
            try:
                cursor.execute("SELECT create_distributed_table('test_students', 'school_id')")
            except:
                pass

            try:
                cursor.execute("SELECT create_distributed_table('curriculum_problems', 'school_id')")
            except:
                pass

            self.pg_conn.commit()

        print("Table setup complete.")

    def generate_and_insert(self, student_count: int, problem_count: int, content_count: int):
        """Generate and insert all test data."""
        print(f"Generating data with scale factor {self.scale_factor}...")

        # Setup tables
        self.setup_tables()

        # Generate data
        students = self.generate_students(student_count)
        problems = self.generate_curriculum_problems(problem_count)
        contents = self.generate_mongo_content(content_count)

        # Insert data
        start_time = time.time()
        self.insert_postgres_data(students, problems)
        self.insert_mongo_data(contents)
        end_time = time.time()

        print(".2f")
        print(f"Data generation complete. Scale factor: {self.scale_factor}")

    def cleanup(self):
        """Clean up database connections."""
        if hasattr(self, 'pg_conn'):
            self.pg_conn.close()
        if hasattr(self, 'mongo_client'):
            self.mongo_client.close()

def main():
    parser = argparse.ArgumentParser(description='Generate test data for scalability testing')
    parser.add_argument('--scale-factor', type=int, default=1,
                       help='Scale factor for data generation (default: 1)')
    parser.add_argument('--students', type=int, default=1000,
                       help='Number of students to generate (default: 1000)')
    parser.add_argument('--problems', type=int, default=500,
                       help='Number of problems to generate (default: 500)')
    parser.add_argument('--contents', type=int, default=2000,
                       help='Number of content documents to generate (default: 2000)')

    args = parser.parse_args()

    # Scale the counts by scale factor
    student_count = args.students * args.scale_factor
    problem_count = args.problems * args.scale_factor
    content_count = args.contents * args.scale_factor

    generator = DataGenerator(args.scale_factor)

    try:
        generator.generate_and_insert(student_count, problem_count, content_count)
    finally:
        generator.cleanup()

if __name__ == '__main__':
    main()