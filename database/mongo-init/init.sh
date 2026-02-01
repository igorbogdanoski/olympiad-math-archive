#!/bin/bash

# Wait for all services to be ready
sleep 30

# Initialize config replica set
echo "Initializing config replica set..."
mongosh --host config1:27019 --file /docker-entrypoint-initdb.d/init-config.js

# Initialize shard replica sets
echo "Initializing shard1 replica set..."
mongosh --host shard1_1:27018 --file /docker-entrypoint-initdb.d/init-shard1.js

echo "Initializing shard2 replica set..."
mongosh --host shard2_1:27018 --file /docker-entrypoint-initdb.d/init-shard2.js

echo "Initializing shard3 replica set..."
mongosh --host shard3_1:27018 --file /docker-entrypoint-initdb.d/init-shard3.js

# Wait for replica sets to elect primaries
sleep 15

# Initialize cluster via mongos
echo "Initializing cluster via mongos..."
mongosh --host mongos1:27017 --file /docker-entrypoint-initdb.d/init-cluster.js

echo "MongoDB cluster setup complete!"