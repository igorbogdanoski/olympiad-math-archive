import pytest
import requests
import time
import subprocess
import os
from pymongo import MongoClient
import psycopg2

# Service configuration
LOCALIZATION_SERVICE_URL = os.getenv('LOCALIZATION_SERVICE_URL', 'http://localhost:3004')

@pytest.fixture(scope="session")
def start_localization_service():
    """Start the localization service for testing."""
    # This assumes the service can be started from the test
    # In a real scenario, you might use Docker Compose or Kubernetes
    service_dir = "microservices/localization-handler"

    # Set environment variables for test database
    env = os.environ.copy()
    env.update({
        'POSTGRES_HOST': 'localhost',
        'POSTGRES_PORT': '5432',
        'POSTGRES_USER': 'postgres',
        'POSTGRES_PASSWORD': 'postgres',
        'POSTGRES_DB': 'olympiad_core',
        'MONGO_HOST': 'localhost',
        'MONGO_PORT': '27017',
        'MONGO_USER': 'admin',
        'MONGO_PASSWORD': 'securepassword123',
        'MONGO_DB': 'olympiad_db',
        'PORT': '3004'
    })

    process = subprocess.Popen(
        ['node', 'server.js'],
        cwd=service_dir,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Wait for service to start
    time.sleep(5)

    yield process

    # Cleanup
    process.terminate()
    process.wait()

def test_localization_service_health(start_localization_service):
    """Test localization service health endpoint."""
    response = requests.get(f"{LOCALIZATION_SERVICE_URL}/health")
    assert response.status_code == 200
    assert response.text == "Localization Handler is healthy"

def test_localization_service_db_health(start_localization_service, mongo_client, postgres_connection):
    """Test localization service database health check."""
    response = requests.get(f"{LOCALIZATION_SERVICE_URL}/health/db")
    assert response.status_code == 200

    health_data = response.json()
    assert isinstance(health_data, list)

    # Should have health status for both databases
    db_names = [h.get('database') for h in health_data]
    assert 'PostgreSQL' in db_names
    assert 'MongoDB' in db_names

    # All should be healthy
    for health in health_data:
        assert health['status'] == 'healthy'

def test_localization_workflow(start_localization_service, mongo_db):
    """Test complete localization workflow."""
    # First, insert test data into MongoDB
    test_content = {
        "problemId": "test_problem_123",
        "schoolId": 1,
        "content": "This is a test math problem",
        "createdAt": "2024-01-01T00:00:00Z"
    }

    mongo_db.generated_content.insert_one(test_content)

    # Now test the localization endpoint
    payload = {
        "problemId": "test_problem_123",
        "schoolId": 1,
        "targetLanguage": "es"
    }

    response = requests.post(f"{LOCALIZATION_SERVICE_URL}/localize", json=payload)
    assert response.status_code == 200

    result = response.json()
    assert "message" in result
    assert "localizationId" in result
    assert "localizedContent" in result
    assert "Localized version of" in result["localizedContent"]
    assert "es" in result["localizedContent"]

    # Verify data was stored in MongoDB
    localization_doc = mongo_db.localization.find_one({"problemId": "test_problem_123"})
    assert localization_doc is not None
    assert localization_doc["language"] == "es"
    assert localization_doc["schoolId"] == 1

    # Cleanup
    mongo_db.generated_content.delete_one({"problemId": "test_problem_123"})
    mongo_db.localization.delete_one({"problemId": "test_problem_123"})

def test_localization_error_handling(start_localization_service):
    """Test localization error handling."""
    # Test with non-existent content
    payload = {
        "problemId": "nonexistent_problem",
        "schoolId": 999,
        "targetLanguage": "fr"
    }

    response = requests.post(f"{LOCALIZATION_SERVICE_URL}/localize", json=payload)
    assert response.status_code == 404

    error_data = response.json()
    assert "error" in error_data
    assert "not found" in error_data["error"].lower()

def test_localization_invalid_payload(start_localization_service):
    """Test localization with invalid payload."""
    # Missing required fields
    payload = {
        "problemId": "test_problem_123"
        # Missing schoolId and targetLanguage
    }

    response = requests.post(f"{LOCALIZATION_SERVICE_URL}/localize", json=payload)
    # Should return 400 or 500 depending on validation
    assert response.status_code >= 400

def test_concurrent_localization_requests(start_localization_service, mongo_db):
    """Test handling multiple concurrent localization requests."""
    import threading

    # Insert multiple test contents
    test_contents = []
    for i in range(5):
        content = {
            "problemId": f"concurrent_problem_{i}",
            "schoolId": 1,
            "content": f"Test content {i}",
            "createdAt": "2024-01-01T00:00:00Z"
        }
        mongo_db.generated_content.insert_one(content)
        test_contents.append(content)

    results = []
    errors = []

    def make_request(problem_id):
        try:
            payload = {
                "problemId": problem_id,
                "schoolId": 1,
                "targetLanguage": "de"
            }
            response = requests.post(f"{LOCALIZATION_SERVICE_URL}/localize", json=payload, timeout=10)
            results.append((problem_id, response.status_code, response.json() if response.status_code == 200 else None))
        except Exception as e:
            errors.append((problem_id, str(e)))

    # Start concurrent requests
    threads = []
    for content in test_contents:
        thread = threading.Thread(target=make_request, args=(content["problemId"],))
        threads.append(thread)
        thread.start()

    # Wait for all threads
    for thread in threads:
        thread.join()

    # Verify results
    assert len(results) == 5
    assert len(errors) == 0

    for problem_id, status_code, data in results:
        assert status_code == 200
        assert data["localizedContent"] is not None

    # Verify all localizations were stored
    localization_count = mongo_db.localization.count_documents({"schoolId": 1, "language": "de"})
    assert localization_count == 5

    # Cleanup
    for content in test_contents:
        mongo_db.generated_content.delete_one({"problemId": content["problemId"]})
    mongo_db.localization.delete_many({"schoolId": 1, "language": "de"})

def test_database_connection_failures(mongo_db):
    """Test service behavior when database connections fail."""
    # This would require mocking database failures
    # For now, test with invalid connection (service should handle gracefully)

    # Temporarily disconnect MongoDB client to simulate failure
    # Note: This is a simplified test - real implementation would need proper mocking

    # Test that service can recover from database issues
    response = requests.get(f"{LOCALIZATION_SERVICE_URL}/health/db")
    assert response.status_code in [200, 503]  # Either healthy or indicating service unavailable