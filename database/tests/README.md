# Database Testing Suite

This directory contains comprehensive testing procedures for the PostgreSQL Citus cluster, MongoDB sharded cluster, CDC synchronization, backup/recovery systems, and multi-AZ failover scenarios.

## Test Categories

### 1. Unit Tests (`unit/`)
- **PostgreSQL Connection Tests**: Basic connectivity, Citus extension validation, sharding operations, transaction isolation
- **MongoDB Connection Tests**: Connection pooling, authentication, replica set status, sharding validation
- **Database Operations**: CRUD operations, indexing, aggregation pipelines

### 2. Integration Tests (`integration/`)
- **Microservice Integration**: Test localization-handler interactions with databases
- **API Endpoint Testing**: Health checks, data flow validation
- **Concurrent Operations**: Multiple service interactions

### 3. Scalability Tests (`scalability/`)
- **Load Testing**: Using Locust for distributed load simulation
- **Data Generation**: Automated generation of test data with configurable scale factors
- **Performance Scaling**: Testing with increasing data volumes (1x, 10x, 100x scale)

### 4. Failover Tests (`failover/`)
- **PostgreSQL Patroni Failover**: Automatic leader election and recovery
- **MongoDB Replica Set Failover**: Primary election and data consistency
- **Connection Pooling**: PgBouncer failover behavior
- **Data Consistency**: Verification during failover events

### 5. Synchronization Tests (`synchronization/`)
- **CDC Pipeline Testing**: Debezium PostgreSQL connector validation
- **Kafka Connect**: MongoDB sink connector testing
- **Data Consistency**: INSERT/UPDATE/DELETE synchronization validation
- **Cross-Database Sync**: PostgreSQL → Kafka → MongoDB pipeline

### 6. Backup/Recovery Tests (`backup_recovery/`)
- **PostgreSQL Backups**: Full, incremental, and WAL archiving
- **MongoDB Backups**: Oplog backup and point-in-time recovery
- **Backup Validation**: Integrity checks and restoration testing
- **Disaster Recovery**: Complete recovery scenario simulation

### 7. Multi-AZ Tests (`multi_az/`)
- **Geographic Redundancy**: Cross-region data replication
- **Load Balancing**: Traffic distribution and routing
- **AZ Failover**: Automatic failover between availability zones
- **Network Latency**: Performance under simulated network conditions

### 8. Performance & Monitoring (`performance/`)
- **Benchmarking**: Query performance, throughput, latency measurements
- **Prometheus Metrics**: Monitoring validation and alerting
- **Grafana Dashboards**: Visualization system testing
- **Concurrent Load**: Multi-user performance testing

## Prerequisites

### System Requirements
- Python 3.8+
- Docker and Docker Compose
- PostgreSQL Citus cluster running
- MongoDB sharded cluster running
- Kafka with Debezium and Kafka Connect
- Prometheus and Grafana (optional for monitoring tests)

### Python Dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- pytest>=7.0.0
- psycopg2-binary>=2.9.0
- pymongo>=4.0.0
- locust>=2.15.0
- requests>=2.28.0
- prometheus-client>=0.17.0
- docker>=6.1.0

## Environment Variables

Set the following environment variables for your test environment:

```bash
# PostgreSQL
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
export POSTGRES_USER=postgres
export POSTGRES_PASSWORD=postgres
export POSTGRES_DB=olympiad_core

# MongoDB
export MONGO_HOST=localhost
export MONGO_PORT=27017
export MONGO_USER=admin
export MONGO_PASSWORD=securepassword123
export MONGO_DB=olympiad_db
export MONGO_AUTH_SOURCE=admin

# Kafka/CDC
export KAFKA_CONNECT_URL=http://localhost:8083
export KAFKA_BROKER_URL=localhost:9092

# Monitoring (optional)
export PROMETHEUS_URL=http://localhost:9090
export GRAFANA_URL=http://localhost:3000
export ALERTMANAGER_URL=http://localhost:9093

# Multi-AZ (optional)
export POSTGRES_LB_HOST=localhost
export POSTGRES_LB_PORT=6432
export MONGO_LB_HOST=localhost
export MONGO_LB_PORT=27017
```

## Running Tests

### Setup Test Environment
```bash
# Install dependencies
python run_tests.py --setup

# Or manually
pip install -r requirements.txt
```

### Run All Tests
```bash
python run_tests.py --all
```

### Run Specific Test Categories
```bash
# Unit tests only
python run_tests.py --unit

# Integration tests
python run_tests.py --integration

# Scalability tests
python run_tests.py --scalability

# Failover tests
python run_tests.py --failover

# Synchronization tests
python run_tests.py --synchronization

# Backup/recovery tests
python run_tests.py --backup-recovery

# Multi-AZ tests
python run_tests.py --multi-az

# Performance tests
python run_tests.py --performance
```

### Run Individual Test Files
```bash
# Using pytest directly
pytest unit/test_postgres_connection.py -v
pytest integration/test_localization_integration.py -v
pytest scalability/load_test.py  # Locust load test
pytest failover/test_failover.py -v
pytest synchronization/test_cdc_synchronization.py -v
pytest backup_recovery/test_backup_recovery.py -v
pytest multi_az/test_multi_az.py -v
pytest performance/test_performance_monitoring.py -v
```

## Scalability Testing

### Data Generation
Generate test data with different scale factors:

```bash
# Generate small dataset (default)
python scalability/data_generator.py

# Generate 10x scale dataset
python scalability/data_generator.py --scale-factor 10

# Generate 100x scale dataset
python scalability/data_generator.py --scale-factor 100 --students 10000 --problems 5000 --contents 20000
```

### Load Testing
Run Locust load tests:

```bash
# Web UI mode
locust -f scalability/load_test.py

# Headless mode
locust -f scalability/load_test.py --headless -u 100 -r 10 --run-time 5m
```

## Test Data Management

### Setup Test Tables
The tests automatically create necessary test tables, but you can pre-setup:

```sql
-- PostgreSQL test tables
CREATE TABLE test_students (
    student_id SERIAL PRIMARY KEY,
    school_id INTEGER NOT NULL,
    name VARCHAR(100)
);

CREATE TABLE curriculum_problems (
    problem_id VARCHAR(50) PRIMARY KEY,
    school_id INTEGER NOT NULL,
    title VARCHAR(200),
    content TEXT
);

-- Distribute tables
SELECT create_distributed_table('test_students', 'school_id');
SELECT create_distributed_table('curriculum_problems', 'school_id');
```

### MongoDB Collections
Test collections are created automatically:
- `generated_content`: Sharded content collection
- `localization`: Localization data
- Various test collections for specific tests

## Monitoring and Reporting

### Performance Reports
Generate performance benchmark reports:

```python
from performance.test_performance_monitoring import PerformanceMonitorTester

tester = PerformanceMonitorTester()
report = tester.generate_performance_report()
print(report)
```

### Test Results
- Pytest generates JUnit XML reports
- Locust generates HTML reports
- Performance benchmarks output JSON metrics
- Failed tests provide detailed error information

## Troubleshooting

### Common Issues

1. **Database Connection Failures**
   - Ensure databases are running and accessible
   - Check environment variables
   - Verify network connectivity

2. **Docker Container Issues**
   - Ensure containers are started: `docker-compose up -d`
   - Check container logs: `docker-compose logs`
   - Verify port mappings

3. **CDC Pipeline Issues**
   - Check Kafka broker connectivity
   - Verify Debezium and Kafka Connect status
   - Review Kafka topic creation

4. **Load Testing Issues**
   - Ensure sufficient system resources
   - Monitor system metrics during tests
   - Adjust user counts based on system capacity

5. **Multi-AZ Testing**
   - Requires multiple database instances
   - May need load balancer configuration
   - Network simulation tools for latency tests

### Test Isolation
- Each test category is isolated
- Test data is cleaned up after execution
- Use `--tb=short` for concise error reporting

## CI/CD Integration

### GitHub Actions Example
```yaml
- name: Run Database Tests
  run: |
    cd database/tests
    python run_tests.py --unit --integration

- name: Run Scalability Tests
  run: |
    cd database/tests
    python scalability/data_generator.py --scale-factor 5
    python run_tests.py --scalability

- name: Performance Benchmarks
  run: |
    cd database/tests
    python run_tests.py --performance
```

### Docker Test Environment
```bash
# Start test environment
docker-compose -f database/docker-compose.test.yml up -d

# Run tests
docker run --network database_test_network database-tests

# Cleanup
docker-compose -f database/docker-compose.test.yml down
```

## Contributing

### Adding New Tests
1. Create test file in appropriate directory
2. Follow pytest conventions
3. Add fixtures for setup/teardown
4. Update this README
5. Add to `run_tests.py` if needed

### Test Best Practices
- Use descriptive test names
- Include docstrings
- Handle exceptions appropriately
- Clean up test data
- Parameterize tests when possible
- Use fixtures for common setup

## Security Considerations

- Test databases should be separate from production
- Use secure passwords in environment variables
- Clean up test data after execution
- Monitor resource usage during load tests
- Implement timeouts to prevent runaway tests

## Support

For issues or questions:
1. Check test logs and error messages
2. Review database logs
3. Verify environment configuration
4. Consult individual test documentation
5. Check system resource availability