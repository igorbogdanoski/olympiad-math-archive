import pytest
import psycopg2
from pymongo import MongoClient
import os
from typing import Generator

# Database connection configurations
POSTGRES_CONFIG = {
    'host': os.getenv('POSTGRES_HOST', 'localhost'),
    'port': int(os.getenv('POSTGRES_PORT', 5432)),
    'user': os.getenv('POSTGRES_USER', 'postgres'),
    'password': os.getenv('POSTGRES_PASSWORD', 'postgres'),
    'database': os.getenv('POSTGRES_DB', 'olympiad_core')
}

MONGO_CONFIG = {
    'host': os.getenv('MONGO_HOST', 'localhost'),
    'port': int(os.getenv('MONGO_PORT', 27017)),
    'username': os.getenv('MONGO_USER', 'admin'),
    'password': os.getenv('MONGO_PASSWORD', 'securepassword123'),
    'database': os.getenv('MONGO_DB', 'olympiad_db'),
    'authSource': os.getenv('MONGO_AUTH_SOURCE', 'admin')
}

@pytest.fixture(scope="session")
def postgres_connection() -> Generator[psycopg2.extensions.connection, None, None]:
    """PostgreSQL database connection fixture."""
    conn = None
    try:
        conn = psycopg2.connect(**POSTGRES_CONFIG)
        yield conn
    finally:
        if conn:
            conn.close()

@pytest.fixture(scope="session")
def mongo_client() -> Generator[MongoClient, None, None]:
    """MongoDB client fixture."""
    client = None
    try:
        mongo_uri = f"mongodb://{MONGO_CONFIG['username']}:{MONGO_CONFIG['password']}@{MONGO_CONFIG['host']}:{MONGO_CONFIG['port']}/{MONGO_CONFIG['database']}?authSource={MONGO_CONFIG['authSource']}"
        client = MongoClient(mongo_uri)
        yield client
    finally:
        if client:
            client.close()

@pytest.fixture(scope="session")
def mongo_db(mongo_client: MongoClient):
    """MongoDB database fixture."""
    return mongo_client[MONGO_CONFIG['database']]

@pytest.fixture(autouse=True)
def setup_test_data(postgres_connection, mongo_db):
    """Setup test data before each test."""
    # This can be overridden in specific test files
    pass