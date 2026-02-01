import pytest
import psycopg2
from psycopg2 import sql

def test_postgres_connection(postgres_connection):
    """Test basic PostgreSQL connection."""
    assert postgres_connection is not None
    assert not postgres_connection.closed

    # Test simple query
    with postgres_connection.cursor() as cursor:
        cursor.execute("SELECT 1 as test_value")
        result = cursor.fetchone()
        assert result[0] == 1

def test_citus_version(postgres_connection):
    """Test Citus extension is available and working."""
    with postgres_connection.cursor() as cursor:
        cursor.execute("SELECT * FROM citus_version()")
        result = cursor.fetchone()
        assert result is not None
        assert "Citus" in result[0]

def test_sharding_operations(postgres_connection):
    """Test basic sharding operations."""
    with postgres_connection.cursor() as cursor:
        # Create a test table distributed by school_id
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_students (
                student_id SERIAL PRIMARY KEY,
                school_id INTEGER NOT NULL,
                name VARCHAR(100)
            )
        """)

        # Distribute the table
        cursor.execute("SELECT create_distributed_table('test_students', 'school_id')")

        # Insert test data
        cursor.execute("""
            INSERT INTO test_students (school_id, name) VALUES
            (1, 'Alice'),
            (2, 'Bob'),
            (1, 'Charlie')
        """)

        # Test query on distributed table
        cursor.execute("SELECT COUNT(*) FROM test_students")
        count = cursor.fetchone()[0]
        assert count >= 3

        # Test shard count
        cursor.execute("""
            SELECT COUNT(*) FROM pg_dist_shard
            WHERE logicalrelid = 'test_students'::regclass
        """)
        shard_count = cursor.fetchone()[0]
        assert shard_count > 0

        postgres_connection.commit()

def test_connection_pooling():
    """Test PgBouncer connection pooling."""
    # Connect through PgBouncer (port 6432)
    config = {
        'host': 'localhost',
        'port': 6432,
        'user': 'postgres',
        'password': 'postgres',
        'database': 'olympiad_core'
    }

    conn = None
    try:
        conn = psycopg2.connect(**config)
        assert not conn.closed

        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            assert result[0] == 1
    finally:
        if conn:
            conn.close()

def test_transaction_isolation(postgres_connection):
    """Test transaction isolation and rollback."""
    with postgres_connection.cursor() as cursor:
        # Create a test table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS test_transactions (
                id SERIAL PRIMARY KEY,
                value INTEGER
            )
        """)
        postgres_connection.commit()

        # Start transaction
        cursor.execute("INSERT INTO test_transactions (value) VALUES (100)")
        cursor.execute("SELECT COUNT(*) FROM test_transactions WHERE value = 100")
        count = cursor.fetchone()[0]
        assert count == 1

        # Rollback
        postgres_connection.rollback()

        cursor.execute("SELECT COUNT(*) FROM test_transactions WHERE value = 100")
        count = cursor.fetchone()[0]
        assert count == 0

def test_prepared_statements(postgres_connection):
    """Test prepared statements for performance."""
    with postgres_connection.cursor() as cursor:
        # Prepare statement
        cursor.execute("""
            PREPARE test_insert (INTEGER, TEXT) AS
            INSERT INTO test_students (school_id, name) VALUES ($1, $2)
        """)

        # Execute prepared statement
        cursor.execute("EXECUTE test_insert (3, 'Prepared Alice')")
        cursor.execute("EXECUTE test_insert (3, 'Prepared Bob')")

        # Verify
        cursor.execute("SELECT COUNT(*) FROM test_students WHERE school_id = 3")
        count = cursor.fetchone()[0]
        assert count >= 2

        postgres_connection.commit()

def test_error_handling(postgres_connection):
    """Test error handling for invalid operations."""
    with postgres_connection.cursor() as cursor:
        with pytest.raises(psycopg2.Error):
            cursor.execute("SELECT * FROM nonexistent_table")

        # Connection should still be usable
        cursor.execute("SELECT 1")
        result = cursor.fetchone()
        assert result[0] == 1