// Connect to mongos
db = connect("mongos1:27017/admin");

// Add shards to the cluster
sh.addShard("shard1ReplSet/shard1_1:27018,shard1_2:27018,shard1_3:27018");
sh.addShard("shard2ReplSet/shard2_1:27018,shard2_2:27018,shard2_3:27018");
sh.addShard("shard3ReplSet/shard3_1:27018,shard3_2:27018,shard3_3:27018");

// Enable sharding on the database
sh.enableSharding("olympiad_db");

// Shard collections with the specified key
db.adminCommand({shardCollection: "olympiad_db.generated_content", key: {school_id: 1, content_type: 1}});
db.adminCommand({shardCollection: "olympiad_db.rendered_content", key: {school_id: 1, content_type: 1}});
db.adminCommand({shardCollection: "olympiad_db.localization", key: {school_id: 1, content_type: 1}});
db.adminCommand({shardCollection: "olympiad_db.accessibility_metadata", key: {school_id: 1, content_type: 1}});

// Switch to the database
db = db.getSiblingDB("olympiad_db");

// Create indexes for optimal query performance
db.generated_content.createIndex({school_id: 1, content_type: 1});
db.rendered_content.createIndex({school_id: 1, content_type: 1});
db.localization.createIndex({school_id: 1, content_type: 1});
db.accessibility_metadata.createIndex({school_id: 1, content_type: 1});

// Create admin user for authentication
db.getSiblingDB("admin").createUser({
  user: "admin",
  pwd: "securepassword123",  // Change this in production
  roles: ["root"]
});

print("MongoDB sharded cluster initialized with collections, indexes, and authentication");