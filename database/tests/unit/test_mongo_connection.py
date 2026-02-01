import pytest
from pymongo.errors import ConnectionFailure, OperationFailure
from bson import ObjectId

def test_mongo_connection(mongo_client, mongo_db):
    """Test basic MongoDB connection."""
    assert mongo_client is not None

    # Test basic database operation
    result = mongo_db.command("ping")
    assert result["ok"] == 1.0

def test_mongo_sharding_status(mongo_client):
    """Test MongoDB sharding configuration."""
    # Check if sharding is enabled
    try:
        result = mongo_client.admin.command("listShards")
        assert "shards" in result
        assert len(result["shards"]) > 0
    except OperationFailure:
        pytest.skip("Sharding not configured or not accessible")

def test_collection_operations(mongo_db):
    """Test basic collection operations."""
    # Create a test collection
    collection = mongo_db.test_collection

    # Insert documents
    test_docs = [
        {"_id": ObjectId(), "school_id": 1, "content_type": "problem", "data": "Test problem 1"},
        {"_id": ObjectId(), "school_id": 2, "content_type": "solution", "data": "Test solution 1"},
        {"_id": ObjectId(), "school_id": 1, "content_type": "problem", "data": "Test problem 2"}
    ]

    result = collection.insert_many(test_docs)
    assert len(result.inserted_ids) == 3

    # Query documents
    count = collection.count_documents({"school_id": 1})
    assert count >= 2

    # Update document
    result = collection.update_one(
        {"school_id": 1, "content_type": "problem"},
        {"$set": {"data": "Updated problem"}}
    )
    assert result.modified_count >= 1

    # Delete documents
    result = collection.delete_many({"school_id": 1})
    assert result.deleted_count >= 2

    # Cleanup
    collection.drop()

def test_shard_key_operations(mongo_db):
    """Test operations with shard key."""
    collection = mongo_db.test_sharded

    # Insert with shard key
    doc = {
        "_id": ObjectId(),
        "school_id": 1,
        "content_type": "generated",
        "content": "Test generated content"
    }

    result = collection.insert_one(doc)
    assert result.acknowledged

    # Query by shard key
    found = collection.find_one({"school_id": 1, "content_type": "generated"})
    assert found is not None
    assert found["content"] == "Test generated content"

    # Cleanup
    collection.delete_one({"_id": result.inserted_id})

def test_replica_set_status(mongo_client):
    """Test replica set configuration."""
    try:
        result = mongo_client.admin.command("replSetGetStatus")
        assert "members" in result
        assert len(result["members"]) > 0

        # Check if there's a primary
        primaries = [member for member in result["members"] if member["stateStr"] == "PRIMARY"]
        assert len(primaries) == 1
    except OperationFailure:
        pytest.skip("Replica set not configured or not accessible")

def test_authentication(mongo_client):
    """Test authentication is working."""
    # Try to access admin database
    admin_db = mongo_client.admin

    # This should work if authenticated
    result = admin_db.command("connectionStatus")
    assert result["ok"] == 1.0
    assert result["authInfo"]["authenticatedUsers"] is not None

def test_index_operations(mongo_db):
    """Test index creation and usage."""
    collection = mongo_db.test_indexes

    # Create compound index (matching shard key)
    collection.create_index([("school_id", 1), ("content_type", 1)])

    # Insert test data
    docs = [
        {"school_id": 1, "content_type": "problem", "title": "Math Problem 1"},
        {"school_id": 1, "content_type": "solution", "title": "Math Solution 1"},
        {"school_id": 2, "content_type": "problem", "title": "Math Problem 2"}
    ]

    collection.insert_many(docs)

    # Test index usage
    explain = collection.find({"school_id": 1, "content_type": "problem"}).explain()
    # In MongoDB 4.0+, check if index is used
    if "executionStats" in explain:
        assert explain["executionStats"]["totalDocsExamined"] >= 1

    # Cleanup
    collection.drop()

def test_aggregation_pipeline(mongo_db):
    """Test aggregation operations."""
    collection = mongo_db.test_aggregation

    # Insert test data
    docs = [
        {"school_id": 1, "content_type": "problem", "difficulty": "easy", "views": 100},
        {"school_id": 1, "content_type": "problem", "difficulty": "hard", "views": 50},
        {"school_id": 2, "content_type": "solution", "difficulty": "easy", "views": 75}
    ]

    collection.insert_many(docs)

    # Aggregation pipeline
    pipeline = [
        {"$match": {"school_id": 1}},
        {"$group": {"_id": "$content_type", "total_views": {"$sum": "$views"}}}
    ]

    results = list(collection.aggregate(pipeline))
    assert len(results) > 0

    problem_views = next((r for r in results if r["_id"] == "problem"), None)
    assert problem_views is not None
    assert problem_views["total_views"] == 150

    # Cleanup
    collection.drop()

def test_connection_pooling(mongo_client):
    """Test connection pooling behavior."""
    # Get server info to check connection pool
    server_info = mongo_client.server_info()
    assert server_info is not None

    # Test multiple operations to ensure pooling works
    db = mongo_client.test_pooling

    for i in range(10):
        collection = db[f"test_{i}"]
        collection.insert_one({"test": i})
        count = collection.count_documents({})
        assert count == 1
        collection.drop()

def test_error_handling(mongo_db):
    """Test error handling for invalid operations."""
    collection = mongo_db.test_errors

    # Test invalid operation
    try:
        # This should fail due to invalid field name
        collection.insert_one({"$invalid": "field"})
        pytest.fail("Should have raised an exception")
    except OperationFailure:
        pass  # Expected

    # Connection should still work
    collection.insert_one({"valid": "document"})
    count = collection.count_documents({})
    assert count == 1

    collection.drop()