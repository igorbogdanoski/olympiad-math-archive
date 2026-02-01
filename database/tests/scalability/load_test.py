from locust import HttpUser, task, between
from pymongo import MongoClient
import psycopg2
import random
import string
import time
import os

class DatabaseLoadTest(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        """Setup database connections for each user."""
        # PostgreSQL connection
        self.pg_conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            port=int(os.getenv('POSTGRES_PORT', 5432)),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'postgres'),
            database=os.getenv('POSTGRES_DB', 'olympiad_core')
        )

        # MongoDB connection
        mongo_uri = f"mongodb://{os.getenv('MONGO_USER', 'admin')}:{os.getenv('MONGO_PASSWORD', 'securepassword123')}@{os.getenv('MONGO_HOST', 'localhost')}:{os.getenv('MONGO_PORT', 27017)}/{os.getenv('MONGO_DB', 'olympiad_db')}?authSource=admin"
        self.mongo_client = MongoClient(mongo_uri)
        self.mongo_db = self.mongo_client[os.getenv('MONGO_DB', 'olympiad_db')]

    def on_stop(self):
        """Close database connections."""
        if hasattr(self, 'pg_conn'):
            self.pg_conn.close()
        if hasattr(self, 'mongo_client'):
            self.mongo_client.close()

    @task(3)
    def postgres_read_operation(self):
        """Simulate read operations on PostgreSQL."""
        with self.pg_conn.cursor() as cursor:
            try:
                # Random school_id for distributed queries
                school_id = random.randint(1, 100)

                # Simulate reading student data
                cursor.execute("""
                    SELECT COUNT(*) FROM test_students
                    WHERE school_id = %s
                """, (school_id,))

                count = cursor.fetchone()[0]

                # Simulate reading curriculum data
                cursor.execute("""
                    SELECT problem_id, title FROM curriculum_problems
                    WHERE school_id = %s
                    LIMIT 10
                """, (school_id,))

                problems = cursor.fetchall()

            except Exception as e:
                self.environment.events.request.fire(
                    request_type="POSTGRES_READ",
                    name="postgres_read",
                    response_time=0,
                    response_length=0,
                    exception=e
                )
                return

        self.environment.events.request.fire(
            request_type="POSTGRES_READ",
            name="postgres_read",
            response_time=time.time() * 1000,  # Convert to milliseconds
            response_length=len(problems) if 'problems' in locals() else 0,
        )

    @task(2)
    def postgres_write_operation(self):
        """Simulate write operations on PostgreSQL."""
        with self.pg_conn.cursor() as cursor:
            try:
                school_id = random.randint(1, 100)
                student_name = ''.join(random.choices(string.ascii_letters, k=10))

                # Insert new student
                cursor.execute("""
                    INSERT INTO test_students (school_id, name)
                    VALUES (%s, %s)
                """, (school_id, student_name))

                self.pg_conn.commit()

            except Exception as e:
                self.pg_conn.rollback()
                self.environment.events.request.fire(
                    request_type="POSTGRES_WRITE",
                    name="postgres_write",
                    response_time=0,
                    response_length=0,
                    exception=e
                )
                return

        self.environment.events.request.fire(
            request_type="POSTGRES_WRITE",
            name="postgres_write",
            response_time=time.time() * 1000,
            response_length=1,
        )

    @task(3)
    def mongo_read_operation(self):
        """Simulate read operations on MongoDB."""
        try:
            school_id = random.randint(1, 100)
            content_type = random.choice(['problem', 'solution', 'generated'])

            # Query sharded collection
            collection = self.mongo_db.generated_content
            documents = list(collection.find(
                {"school_id": school_id, "content_type": content_type}
            ).limit(5))

            response_length = len(documents)

        except Exception as e:
            self.environment.events.request.fire(
                request_type="MONGO_READ",
                name="mongo_read",
                response_time=0,
                response_length=0,
                exception=e
            )
            return

        self.environment.events.request.fire(
            request_type="MONGO_READ",
            name="mongo_read",
            response_time=time.time() * 1000,
            response_length=response_length,
        )

    @task(2)
    def mongo_write_operation(self):
        """Simulate write operations on MongoDB."""
        try:
            school_id = random.randint(1, 100)
            content_type = random.choice(['problem', 'solution', 'generated'])
            content_data = ''.join(random.choices(string.ascii_letters + string.digits, k=100))

            # Insert into sharded collection
            collection = self.mongo_db.generated_content
            document = {
                "school_id": school_id,
                "content_type": content_type,
                "content": content_data,
                "created_at": time.time(),
                "metadata": {
                    "difficulty": random.choice(['easy', 'medium', 'hard']),
                    "subject": random.choice(['algebra', 'geometry', 'combinatorics'])
                }
            }

            result = collection.insert_one(document)

        except Exception as e:
            self.environment.events.request.fire(
                request_type="MONGO_WRITE",
                name="mongo_write",
                response_time=0,
                response_length=0,
                exception=e
            )
            return

        self.environment.events.request.fire(
            request_type="MONGO_WRITE",
            name="mongo_write",
            response_time=time.time() * 1000,
            response_length=1,
        )

    @task(1)
    def complex_query_operation(self):
        """Simulate complex queries spanning both databases."""
        try:
            school_id = random.randint(1, 100)

            # PostgreSQL query
            with self.pg_conn.cursor() as cursor:
                cursor.execute("""
                    SELECT COUNT(*) as student_count
                    FROM test_students
                    WHERE school_id = %s
                """, (school_id,))
                pg_result = cursor.fetchone()

            # MongoDB query
            collection = self.mongo_db.generated_content
            mongo_result = collection.aggregate([
                {"$match": {"school_id": school_id}},
                {"$group": {"_id": "$content_type", "count": {"$sum": 1}}}
            ])

            mongo_counts = list(mongo_result)

            # Combine results (simulating business logic)
            combined_data = {
                "school_id": school_id,
                "student_count": pg_result[0] if pg_result else 0,
                "content_counts": {item["_id"]: item["count"] for item in mongo_counts}
            }

        except Exception as e:
            self.environment.events.request.fire(
                request_type="COMPLEX_QUERY",
                name="complex_query",
                response_time=0,
                response_length=0,
                exception=e
            )
            return

        self.environment.events.request.fire(
            request_type="COMPLEX_QUERY",
            name="complex_query",
            response_time=time.time() * 1000,
            response_length=len(str(combined_data)),
        )