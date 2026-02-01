// Connect to shard2_1 and initialize replica set
db = connect("shard2_1:27018/admin");

rs.initiate({
  _id: "shard2ReplSet",
  members: [
    { _id: 0, host: "shard2_1:27018" },
    { _id: 1, host: "shard2_2:27018" },
    { _id: 2, host: "shard2_3:27018" }
  ]
});

// Wait for primary election
while (!rs.isMaster().ismaster) {
  sleep(1000);
}

print("Shard2 replica set initialized");