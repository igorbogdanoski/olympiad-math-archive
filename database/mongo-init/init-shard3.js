// Connect to shard3_1 and initialize replica set
db = connect("shard3_1:27018/admin");

rs.initiate({
  _id: "shard3ReplSet",
  members: [
    { _id: 0, host: "shard3_1:27018" },
    { _id: 1, host: "shard3_2:27018" },
    { _id: 2, host: "shard3_3:27018" }
  ]
});

// Wait for primary election
while (!rs.isMaster().ismaster) {
  sleep(1000);
}

print("Shard3 replica set initialized");