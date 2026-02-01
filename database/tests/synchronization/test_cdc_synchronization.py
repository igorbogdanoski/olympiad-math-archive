#!/usr/bin/env python3
"""
CDC Synchronization Testing

Tests Change Data Capture (CDC) pipeline using Kafka and Debezium,
validating data synchronization between PostgreSQL and MongoDB.
"""

import pytest
import time
import psycopg2
from pymongo import MongoClient
import json
import requests
import os
from typing import Dict, List, Any

class CDCTester:
    def __init__(self):
        self.kafka_connect_url = os.getenv('KAFKA_CONNECT_URL', 'http://localhost:8083')
        self.kafka_broker_url = os.getenv('KAFKA_BROKER_URL', 'localhost:9092')

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

        # Test table setup
        self.setup_test_table()

    def setup_test_table(self):
        """Create test table for CDC testing."""
        with self.pg_conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS cdc_test_problems (
                    problem_id SERIAL PRIMARY KEY,
                    school_id INTEGER NOT NULL,
                    title VARCHAR(200),
                    content TEXT,
                    difficulty VARCHAR(20),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)

            # Add trigger for updated_at (simplified, real implementation would use a proper trigger)
            cursor.execute("""
                CREATE OR REPLACE FUNCTION update_updated_at_column()
                RETURNS TRIGGER AS $$
                BEGIN
                    NEW.updated_at = CURRENT_TIMESTAMP;
                    RETURN NEW;
                END;
                $$ language 'plpgsql';
            """)

            cursor.execute("""
                DROP TRIGGER IF EXISTS update_cdc_test_problems_updated_at ON cdc_test_problems;
                CREATE TRIGGER update_cdc_test_problems_updated_at
                    BEFORE UPDATE ON cdc_test_problems
                    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
            """)

            self.pg_conn.commit()

    def insert_test_data(self) -> Dict[str, Any]:
        """Insert test data into PostgreSQL."""
        test_data = {
            'school_id': 1001,
            'title': f'CDC Test Problem {int(time.time())}',
            'content': 'This is a test problem for CDC synchronization.',
            'difficulty': 'medium'
        }

        with self.pg_conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO cdc_test_problems (school_id, title, content, difficulty)
                VALUES (%s, %s, %s, %s)
                RETURNING problem_id, created_at, updated_at
            """, (test_data['school_id'], test_data['title'], test_data['content'], test_data['difficulty']))

            result = cursor.fetchone()
            test_data['problem_id'] = result[0]
            test_data['created_at'] = result[1]
            test_data['updated_at'] = result[2]

        self.pg_conn.commit()
        return test_data

    def update_test_data(self, problem_id: int) -> Dict[str, Any]:
        """Update test data in PostgreSQL."""
        new_content = f'Updated content at {int(time.time())}'
        new_difficulty = 'hard'

        with self.pg_conn.cursor() as cursor:
            cursor.execute("""
                UPDATE cdc_test_problems
                SET content = %s, difficulty = %s
                WHERE problem_id = %s
                RETURNING updated_at
            """, (new_content, new_difficulty, problem_id))

            result = cursor.fetchone()
            updated_at = result[0] if result else None

        self.pg_conn.commit()

        return {
            'problem_id': problem_id,
            'content': new_content,
            'difficulty': new_difficulty,
            'updated_at': updated_at
        }

    def delete_test_data(self, problem_id: int):
        """Delete test data from PostgreSQL."""
        with self.pg_conn.cursor() as cursor:
            cursor.execute("DELETE FROM cdc_test_problems WHERE problem_id = %s", (problem_id,))
        self.pg_conn.commit()

    def wait_for_sync(self, timeout: int = 30) -> bool:
        """Wait for CDC synchronization to complete."""
        time.sleep(timeout)  # Simple wait, in production you'd poll Kafka topics
        return True

    def check_mongo_sync(self, expected_data: Dict[str, Any], operation: str) -> bool:
        """Check if data was synchronized to MongoDB."""
        collection = self.mongo_db.cdc_problems  # Assuming sink connector maps to this collection

        if operation == 'insert':
            doc = collection.find_one({'problem_id': expected_data['problem_id']})
            if not doc:
                return False

            # Verify key fields
            assert doc['school_id'] == expected_data['school_id']
            assert doc['title'] == expected_data['title']
            assert doc['content'] == expected_data['content']
            assert doc['difficulty'] == expected_data['difficulty']
            return True

        elif operation == 'update':
            doc = collection.find_one({'problem_id': expected_data['problem_id']})
            if not doc:
                return False

            assert doc['content'] == expected_data['content']
            assert doc['difficulty'] == expected_data['difficulty']
            return True

        elif operation == 'delete':
            doc = collection.find_one({'problem_id': expected_data['problem_id']})
            return doc is None  # Should not exist after delete

        return False

    def check_debezium_connector_status(self) -> Dict[str, Any]:
        """Check Debezium PostgreSQL connector status."""
        try:
            response = requests.get(f"{self.kafka_connect_url}/connectors/postgres-connector/status")
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"HTTP {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}

    def check_mongodb_sink_status(self) -> Dict[str, Any]:
        """Check MongoDB sink connector status."""
        try:
            response = requests.get(f"{self.kafka_connect_url}/connectors/mongodb-sink-connector/status")
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"HTTP {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}

    def test_cdc_pipeline_health(self):
        """Test that CDC pipeline components are healthy."""
        # Check Debezium connector
        debezium_status = self.check_debezium_connector_status()
        assert "error" not in debezium_status, f"Debezium connector error: {debezium_status}"
        assert debezium_status.get('connector', {}).get('state') == 'RUNNING'

        # Check MongoDB sink connector
        sink_status = self.check_mongodb_sink_status()
        assert "error" not in sink_status, f"MongoDB sink connector error: {sink_status}"
        assert sink_status.get('connector', {}).get('state') == 'RUNNING'

    def test_insert_synchronization(self):
        """Test INSERT operation synchronization."""
        # Insert data
        test_data = self.insert_test_data()
        print(f"Inserted test data: {test_data}")

        # Wait for sync
        self.wait_for_sync()

        # Check MongoDB
        synced = self.check_mongo_sync(test_data, 'insert')
        assert synced, "INSERT operation not synchronized to MongoDB"

    def test_update_synchronization(self):
        """Test UPDATE operation synchronization."""
        # Insert initial data
        test_data = self.insert_test_data()
        self.wait_for_sync()

        # Update data
        updated_data = self.update_test_data(test_data['problem_id'])
        print(f"Updated test data: {updated_data}")

        # Wait for sync
        self.wait_for_sync()

        # Check MongoDB
        synced = self.check_mongo_sync(updated_data, 'update')
        assert synced, "UPDATE operation not synchronized to MongoDB"

        # Cleanup
        self.delete_test_data(test_data['problem_id'])

    def test_delete_synchronization(self):
        """Test DELETE operation synchronization."""
        # Insert data
        test_data = self.insert_test_data()
        self.wait_for_sync()

        # Verify it exists in MongoDB
        assert self.check_mongo_sync(test_data, 'insert')

        # Delete data
        self.delete_test_data(test_data['problem_id'])
        print(f"Deleted test data: {test_data['problem_id']}")

        # Wait for sync
        self.wait_for_sync()

        # Check MongoDB (should not exist)
        synced = self.check_mongo_sync(test_data, 'delete')
        assert synced, "DELETE operation not synchronized to MongoDB"

    def test_data_consistency(self):
        """Test data consistency across multiple operations."""
        # Perform multiple operations
        operations = []

        # Insert 3 records
        for i in range(3):
            data = self.insert_test_data()
            operations.append(('insert', data))

        self.wait_for_sync()

        # Update each record
        for op_type, data in operations:
            if op_type == 'insert':
                updated = self.update_test_data(data['problem_id'])
                operations.append(('update', updated))

        self.wait_for_sync()

        # Verify all updates in MongoDB
        for op_type, data in operations:
            if op_type == 'update':
                assert self.check_mongo_sync(data, 'update'), f"Update not synced for problem_id {data['problem_id']}"

        # Delete all records
        for op_type, data in operations:
            if op_type == 'insert':
                self.delete_test_data(data['problem_id'])

        self.wait_for_sync()

        # Verify deletions in MongoDB
        for op_type, data in operations:
            if op_type == 'insert':
                assert self.check_mongo_sync(data, 'delete'), f"Delete not synced for problem_id {data['problem_id']}"

    def test_bulk_operations(self):
        """Test synchronization of bulk operations."""
        # Bulk insert
        bulk_data = []
        for i in range(10):
            data = self.insert_test_data()
            bulk_data.append(data)

        self.wait_for_sync(60)  # Longer wait for bulk operations

        # Verify all inserts
        synced_count = 0
        for data in bulk_data:
            if self.check_mongo_sync(data, 'insert'):
                synced_count += 1

        assert synced_count >= 8, f"Only {synced_count}/10 bulk inserts synchronized"  # Allow some tolerance

        # Bulk delete
        for data in bulk_data:
            self.delete_test_data(data['problem_id'])

        self.wait_for_sync()

        # Verify deletions
        deleted_count = 0
        for data in bulk_data:
            if self.check_mongo_sync(data, 'delete'):
                deleted_count += 1

        assert deleted_count >= 8, f"Only {deleted_count}/10 bulk deletes synchronized"

    def cleanup(self):
        """Clean up test data."""
        try:
            with self.pg_conn.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS cdc_test_problems")
                cursor.execute("DROP FUNCTION IF EXISTS update_updated_at_column()")
            self.pg_conn.commit()
        except:
            pass

        try:
            self.mongo_db.cdc_problems.drop()
        except:
            pass

        self.pg_conn.close()
        self.mongo_client.close()

@pytest.fixture
def cdc_tester():
    tester = CDCTester()
    yield tester
    tester.cleanup()

def test_cdc_pipeline_health(cdc_tester):
    """Test CDC pipeline component health."""
    cdc_tester.test_cdc_pipeline_health()

def test_insert_operation_sync(cdc_tester):
    """Test INSERT synchronization."""
    cdc_tester.test_insert_synchronization()

def test_update_operation_sync(cdc_tester):
    """Test UPDATE synchronization."""
    cdc_tester.test_update_synchronization()

def test_delete_operation_sync(cdc_tester):
    """Test DELETE synchronization."""
    cdc_tester.test_delete_synchronization()

def test_data_consistency_across_operations(cdc_tester):
    """Test data consistency across multiple operations."""
    cdc_tester.test_data_consistency()

def test_bulk_operation_sync(cdc_tester):
    """Test bulk operation synchronization."""
    cdc_tester.test_bulk_operations()