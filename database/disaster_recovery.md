# Disaster Recovery Procedures

This document outlines the procedures for failover and recovery of PostgreSQL Citus cluster and MongoDB sharded cluster in case of disasters.

## Table of Contents

1. [PostgreSQL Cluster Recovery](#postgresql-cluster-recovery)
2. [MongoDB Cluster Recovery](#mongodb-cluster-recovery)
3. [Cross-Region Failover](#cross-region-failover)
4. [Point-in-Time Recovery](#point-in-time-recovery)

## PostgreSQL Cluster Recovery

### Automatic Failover (Patroni)

The PostgreSQL cluster uses Patroni for automatic failover:

1. **Detection**: Patroni detects leader failure via etcd heartbeat
2. **Election**: Remaining nodes elect new leader automatically
3. **Promotion**: New leader promotes standby to primary
4. **Notification**: Alertmanager sends notifications

**Manual intervention only required if:**
- All nodes fail
- Network partition prevents consensus
- Data corruption detected

### Manual Failover Procedure

```bash
# Check cluster status
curl http://localhost:8008/cluster

# Force failover to specific node
curl -X POST http://localhost:8008/failover \
  -d '{"leader": "citus_coordinator", "candidate": "citus_worker1"}'

# Reinitialize failed node
patronictl reinit citus_cluster citus_coordinator
```

### Full Cluster Recovery from Backup

1. **Stop all services**
   ```bash
   docker-compose down
   ```

2. **Restore from S3 backup**
   ```bash
   # Download latest backup
   wal-g backup-fetch /var/lib/postgresql/data LATEST

   # Restore WAL files if needed
   wal-g wal-fetch --restore-target-time="2023-01-01 12:00:00"
   ```

3. **Restart cluster**
   ```bash
   docker-compose up -d
   ```

4. **Verify cluster health**
   ```bash
   SELECT * FROM citus_check_cluster();
   ```

## MongoDB Cluster Recovery

### Automatic Failover (Replica Sets)

Each shard and config server replica set handles failover automatically:

1. **Detection**: Replica set members monitor each other
2. **Election**: Secondary promotes to primary
3. **Notification**: Monitoring alerts sent

### Manual Shard Recovery

```bash
# Connect to mongos
mongosh --host mongos1 --username admin --password securepassword123 --authenticationDatabase admin

# Check cluster status
sh.status()

# If shard is down, check replica set
rs.status()

# Force reconfigure if needed
rs.reconfig({
  _id: "shard1ReplSet",
  members: [
    {_id: 0, host: "mongo_shard1_1:27018"},
    {_id: 1, host: "mongo_shard1_2:27018", priority: 0.5},
    {_id: 2, host: "mongo_shard1_3:27018", arbiterOnly: true}
  ]
})
```

### Full Cluster Restore

1. **Stop cluster**
   ```bash
   docker-compose -f mongo-docker-compose.yml down
   ```

2. **Restore config servers first**
   ```bash
   mongorestore --host config1 --db config /path/to/config-backup
   ```

3. **Restore each shard**
   ```bash
   mongorestore --host shard1_1 --db olympiad_db /path/to/shard-backup
   ```

4. **Restart cluster**
   ```bash
   docker-compose -f mongo-docker-compose.yml up -d
   ```

## Cross-Region Failover

### Prerequisites

- Secondary region infrastructure ready
- Backup replication configured
- DNS failover capability

### Failover Steps

1. **Stop traffic to primary region**
   - Update DNS/load balancer
   - Scale down primary region services

2. **Promote secondary region**
   ```bash
   # For PostgreSQL: Switch patroni to secondary region
   # For MongoDB: Reconfigure mongos to point to secondary shards
   ```

3. **Restore latest data**
   ```bash
   # Apply any missing WAL/transactions from secondary region backups
   wal-g wal-fetch --restore-target-inclusive-promotion
   ```

4. **Verify and resume**
   - Run validation tests
   - Gradually increase traffic

### Failback to Primary

1. **Ensure primary region is healthy**
2. **Set up replication from secondary to primary**
3. **Switch traffic back**
4. **Demote secondary region**

## Point-in-Time Recovery

### PostgreSQL PITR

```bash
# Stop the cluster
docker-compose down

# Create recovery.conf
cat > /var/lib/postgresql/data/recovery.conf << EOF
restore_command = 'wal-g wal-fetch %f %p'
recovery_target_time = '2023-01-01 12:00:00'
recovery_target_action = 'promote'
EOF

# Start recovery
docker-compose up -d citus_coordinator

# Monitor recovery
tail -f /var/lib/postgresql/data/log/postgresql-*.log

# Once recovered, clean up
rm /var/lib/postgresql/data/recovery.conf
```

### MongoDB PITR

```bash
# Restore base snapshot
mongorestore --oplogReplay --oplogLimit "2023-01-01 12:00:00" /path/to/snapshot

# Apply oplog up to target time
mongosh --eval "
  db.getSiblingDB('local').oplog.rs.find({
    ts: {\$gte: Timestamp(1672531200, 0)}  // Target timestamp
  }).sort({ts: 1}).forEach(function(op) {
    // Apply operation
  })
"
```

## Testing Recovery Procedures

### Regular Testing Schedule

- **Weekly**: Test backup restoration
- **Monthly**: Full disaster recovery simulation
- **Quarterly**: Cross-region failover test

### Validation Checklists

- [ ] Backup files are accessible
- [ ] Data integrity verified
- [ ] Applications can connect
- [ ] Performance meets requirements
- [ ] All services functional

## Emergency Contacts

- **Database Administrator**: [contact]
- **Infrastructure Team**: [contact]
- **Application Owners**: [contact]

## RTO/RPO Targets

- **Recovery Time Objective (RTO)**: 4 hours for full service, 1 hour for critical functions
- **Recovery Point Objective (RPO)**: 15 minutes data loss maximum
- **Cross-region RTO**: 8 hours
- **Cross-region RPO**: 1 hour