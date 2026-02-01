# PostgreSQL Citus Cluster Setup

This directory contains the setup for a scalable PostgreSQL cluster with Citus extension for sharding, Patroni for high availability, and PgBouncer for connection pooling.

## Architecture

- **Coordinator Node**: Handles queries and coordinates sharding
- **Worker Nodes**: Store sharded data (3 initial workers)
- **PgBouncer**: Connection pooling
- **Patroni**: Automatic failover using etcd as DCS
- **Sharding**: By `school_id` for most tables

## Docker Compose Setup

### Prerequisites
- Docker and Docker Compose installed

### Starting the Cluster
```bash
cd database
docker-compose up -d
```

Wait for Patroni to initialize and elect a leader (coordinator should be the leader).

### Check Cluster Status
```bash
# Check Patroni status
curl http://localhost:8008/cluster

# Connect to database
psql -h localhost -p 5432 -U postgres -d olympiad_core

# Verify Citus
SELECT * FROM citus_version();
```

### Run Schema Migration
```sql
psql -h localhost -p 5432 -U postgres -d olympiad_core -f migrations/001_initial_schema.sql
```

### Add Worker Nodes to Citus
After workers are running:
```sql
SELECT * FROM citus_add_node('citus_worker1', 5433);
SELECT * FROM citus_add_node('citus_worker2', 5434);
SELECT * FROM citus_add_node('citus_worker3', 5435);
```

### Test Connection Pooling
```bash
psql -h localhost -p 6432 -U postgres -d olympiad_core
```

## Kubernetes Setup

### Prerequisites
- Kubernetes cluster
- kubectl configured

### Deploy
```bash
kubectl apply -f k8s/
```

### Check Status
```bash
kubectl get pods
kubectl get svc
```

### Run Migration Job
Create a job to run the migration (not included, but can be added).

## MongoDB Sharded Cluster Setup

This directory contains the setup for a production-ready MongoDB sharded cluster with replica sets, suitable for document-based data collections.

### Architecture

- **Config Servers**: 3-member replica set for cluster metadata
- **Shard Servers**: 3 shards, each with 3-member replica set
- **Mongos Routers**: 2 routers for query distribution
- **Sharding**: Enabled on collections with shard key `{school_id: 1, content_type: 1}`
- **Collections**: `generated_content`, `rendered_content`, `localization`, `accessibility_metadata`
- **Authentication**: Enabled with admin user
- **Indexes**: Created for optimal query performance

### Docker Compose Setup

#### Prerequisites
- Docker and Docker Compose installed

#### Starting the Cluster
```bash
cd database
docker-compose -f mongo-docker-compose.yml up -d
```

Wait for initialization (may take a few minutes). The `init-mongo` service will set up the cluster automatically.

#### Check Cluster Status
```bash
# Connect to mongos
mongosh --host localhost:27017 --username admin --password securepassword123 --authenticationDatabase admin

# Check sharding status
sh.status()

# Check replica sets
rs.status()
```

#### Stop the Cluster
```bash
docker-compose -f mongo-docker-compose.yml down -v  # -v to remove volumes
```

### Kubernetes Setup

#### Prerequisites
- Kubernetes cluster
- kubectl configured

#### Deploy
```bash
kubectl apply -f k8s-mongo/
```

#### Check Status
```bash
kubectl get pods -n mongodb-cluster
kubectl get svc -n mongodb-cluster
```

#### Run Initialization Job
The init job runs automatically, but to check:
```bash
kubectl logs -n mongodb-cluster job/mongo-init
```

### Environment Configuration

Microservices use the following connections:
- PostgreSQL via PgBouncer: `pgbouncer:6432`
- MongoDB: `mongodb://admin:securepassword123@mongos1:27017/olympiad_db?authSource=admin` (Docker Compose)
- MongoDB: `mongodb://admin:securepassword123@mongo-mongos.mongodb-cluster.svc.cluster.local:27017/olympiad_db?authSource=admin` (Kubernetes)

See `.env` files in each microservice directory.

## Backup and Recovery

The database clusters include comprehensive backup and recovery systems:

### PostgreSQL Backup Features

- **WAL Archiving**: Continuous archiving to S3-compatible storage using wal-g
- **Point-in-Time Recovery (PITR)**: Restore to any point in time
- **Automated Full Backups**: Daily full backups with retention policies
- **Monitoring**: Backup success/failure alerts via Prometheus/Alertmanager

### MongoDB Backup Features

- **Oplog Backup**: Continuous oplog capture for PITR
- **Automated Snapshots**: Regular snapshot backups with oplog
- **Sharded Cluster Support**: Backup across all shards and config servers

### Backup Management

```bash
# Run PostgreSQL backup
./postgres_backup.sh full

# Run MongoDB backup
./mongo_backup.sh snapshot

# Validate backups
./backup_validation.sh

# Cleanup old backups
./postgres_backup.sh cleanup
./mongo_backup.sh cleanup
```

### Monitoring and Alerting

- Backup job success/failure
- Backup validation results
- WAL archiving status
- Cross-region replication lag
- Backup age monitoring

### Disaster Recovery

See `disaster_recovery.md` for detailed failover and recovery procedures.

## Notes

- Patroni configuration uses environment variables for simplicity.
- For production, secure passwords and use secrets.
- MongoDB cluster is now fully implemented with sharding and authentication.
- Comprehensive backup and recovery systems are configured.
- Geographic redundancy and CDC to PostgreSQL are fully set up.