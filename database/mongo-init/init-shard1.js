// Connect to shard1_1 and initialize replica set
db = connect("shard1_1:27018/admin");

rs.initiate({
  _id: "shard1ReplSet",
  members: [
    { _id: 0, host: "shard1_1:27018" },
    { _id: 1, host: "shard1_2:27018" },
    { _id: 2, host: "shard1_3:27018" }
  ]
});

// Wait for primary election
while (!rs.isMaster().ismaster) {
  sleep(1000);
}

print("Shard1 replica set initialized");