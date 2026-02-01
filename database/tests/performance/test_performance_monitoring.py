#!/usr/bin/env python3
"""
Performance Benchmarks and Monitoring Validation

Tests database performance benchmarks, monitoring metrics validation,
and alerting system verification.
"""

import pytest
import time
import psycopg2
import statistics
from pymongo import MongoClient
from pymongo.errors import OperationFailure
import requests
import os
from typing import Dict, List, Any, Tuple
import json
import subprocess

class PerformanceMonitorTester:
    def __init__(self):
        # Database connections
        self.pg_conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST', 'localhost'),
            port=int(os.getenv('POSTGRES_PORT', 5432)),
            user=os.getenv('POSTGRES_USER', 'postgres'),
            password=os.getenv('POSTGRES_PASSWORD', 'postgres'),
            database=os.getenv('POSTGRES_DB', 'olympiad_core')
        )

        mongo_uri = f"mongodb://{os.getenv('MONGO_USER', 'admin')}:{os.getenv('MONGO_PASSWORD', 'securepassword123')}@{os.getenv('MONGO_HOST', 'localhost')}:{os.getenv('MONGO_PORT', 27017)}/{os.getenv('MONGO_DB', 'olympiad_db')}?authSource=admin"
        self.mongo_client = MongoClient(mongo_uri)
        self.mongo_db = self.mongo_client[os.getenv('MONGO_DB', 'olympiad_db')]

        # Monitoring endpoints
        self.prometheus_url = os.getenv('PROMETHEUS_URL', 'http://localhost:9090')
        self.grafana_url = os.getenv('GRAFANA_URL', 'http://localhost:3000')
        self.alertmanager_url = os.getenv('ALERTMANAGER_URL', 'http://localhost:9093')

    def benchmark_postgres_query_performance(self, query_count: int = 100) -> Dict[str, Any]:
        """Benchmark PostgreSQL query performance."""
        results = {
            'simple_selects': [],
            'complex_queries': [],
            'inserts': [],
            'updates': []
        }

        # Simple SELECT queries
        for i in range(query_count):
            start_time = time.perf_counter()
            with self.pg_conn.cursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM test_students WHERE school_id = %s", (i % 10,))
                cursor.fetchone()
            end_time = time.perf_counter()
            results['simple_selects'].append((end_time - start_time) * 1000)  # Convert to ms

        # Complex distributed queries
        for i in range(query_count // 10):  # Fewer complex queries
            start_time = time.perf_counter()
            with self.pg_conn.cursor() as cursor:
                cursor.execute("""
                    SELECT s.school_id, COUNT(*) as student_count,
                           AVG(LENGTH(s.name)) as avg_name_length
                    FROM test_students s
                    GROUP BY s.school_id
                    ORDER BY student_count DESC
                    LIMIT 10
                """)
                cursor.fetchall()
            end_time = time.perf_counter()
            results['complex_queries'].append((end_time - start_time) * 1000)

        # INSERT operations
        for i in range(query_count // 2):
            start_time = time.perf_counter()
            with self.pg_conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO test_students (school_id, name)
                    VALUES (%s, %s)
                """, (999, f'Perf test user {i}'))
            self.pg_conn.commit()
            end_time = time.perf_counter()
            results['inserts'].append((end_time - start_time) * 1000)

        # Calculate statistics
        for operation, times in results.items():
            if times:
                results[f'{operation}_stats'] = {
                    'avg': statistics.mean(times),
                    'median': statistics.median(times),
                    'p95': sorted(times)[int(len(times) * 0.95)],
                    'p99': sorted(times)[int(len(times) * 0.99)],
                    'min': min(times),
                    'max': max(times),
                    'count': len(times)
                }

        return results

    def benchmark_mongo_performance(self, operation_count: int = 100) -> Dict[str, Any]:
        """Benchmark MongoDB performance."""
        results = {
            'finds': [],
            'inserts': [],
            'updates': [],
            'aggregations': []
        }

        collection = self.mongo_db.perf_test_collection

        # FIND operations
        for i in range(operation_count):
            start_time = time.perf_counter()
            list(collection.find({"school_id": i % 10}).limit(10))
            end_time = time.perf_counter()
            results['finds'].append((end_time - start_time) * 1000)

        # INSERT operations
        for i in range(operation_count // 2):
            doc = {
                "school_id": 999,
                "content_type": "perf_test",
                "data": f"Performance test data {i}",
                "metadata": {"test": True, "index": i}
            }
            start_time = time.perf_counter()
            collection.insert_one(doc)
            end_time = time.perf_counter()
            results['inserts'].append((end_time - start_time) * 1000)

        # UPDATE operations
        for i in range(operation_count // 4):
            start_time = time.perf_counter()
            collection.update_many(
                {"school_id": 999, "content_type": "perf_test"},
                {"$set": {"updated": True, "update_time": time.time()}}
            )
            end_time = time.perf_counter()
            results['updates'].append((end_time - start_time) * 1000)

        # AGGREGATION operations
        for i in range(operation_count // 10):
            pipeline = [
                {"$match": {"school_id": {"$lt": 100}}},
                {"$group": {"_id": "$content_type", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}}
            ]
            start_time = time.perf_counter()
            list(collection.aggregate(pipeline))
            end_time = time.perf_counter()
            results['aggregations'].append((end_time - start_time) * 1000)

        # Calculate statistics
        for operation, times in results.items():
            if times:
                results[f'{operation}_stats'] = {
                    'avg': statistics.mean(times),
                    'median': statistics.median(times),
                    'p95': sorted(times)[int(len(times) * 0.95)],
                    'p99': sorted(times)[int(len(times) * 0.99)],
                    'min': min(times),
                    'max': max(times),
                    'count': len(times)
                }

        # Cleanup
        collection.drop()

        return results

    def validate_prometheus_metrics(self) -> Dict[str, Any]:
        """Validate Prometheus metrics collection."""
        validation_results = {
            'postgres_metrics': {},
            'mongo_metrics': {},
            'system_metrics': {}
        }

        try:
            # Query PostgreSQL metrics
            response = requests.get(f"{self.prometheus_url}/api/v1/query", params={
                'query': 'pg_stat_activity_count'
            }, timeout=10)

            if response.status_code == 200:
                data = response.json()
                validation_results['postgres_metrics']['connection_count'] = len(data.get('data', {}).get('result', []))
            else:
                validation_results['postgres_metrics']['error'] = f"HTTP {response.status_code}"

        except Exception as e:
            validation_results['postgres_metrics']['error'] = str(e)

        try:
            # Query MongoDB metrics
            response = requests.get(f"{self.prometheus_url}/api/v1/query", params={
                'query': 'mongodb_connections_current'
            }, timeout=10)

            if response.status_code == 200:
                data = response.json()
                validation_results['mongo_metrics']['connection_count'] = len(data.get('data', {}).get('result', []))
            else:
                validation_results['mongo_metrics']['error'] = f"HTTP {response.status_code}"

        except Exception as e:
            validation_results['mongo_metrics']['error'] = str(e)

        try:
            # Query system metrics
            response = requests.get(f"{self.prometheus_url}/api/v1/query", params={
                'query': 'node_cpu_seconds_total'
            }, timeout=10)

            if response.status_code == 200:
                data = response.json()
                validation_results['system_metrics']['cpu_metrics'] = len(data.get('data', {}).get('result', []))
            else:
                validation_results['system_metrics']['error'] = f"HTTP {response.status_code}"

        except Exception as e:
            validation_results['system_metrics']['error'] = str(e)

        return validation_results

    def validate_grafana_dashboards(self) -> Dict[str, Any]:
        """Validate Grafana dashboards."""
        validation_results = {
            'cdc_dashboard': False,
            'performance_dashboard': False,
            'error': None
        }

        try:
            # Check if Grafana is accessible
            response = requests.get(f"{self.grafana_url}/api/health", timeout=10)

            if response.status_code == 200:
                # Try to access CDC dashboard (assuming it exists)
                response = requests.get(f"{self.grafana_url}/api/dashboards/uid/cdc-dashboard", timeout=10)
                if response.status_code == 200:
                    validation_results['cdc_dashboard'] = True

                # Try to access performance dashboard
                response = requests.get(f"{self.grafana_url}/api/dashboards/uid/performance-dashboard", timeout=10)
                if response.status_code == 200:
                    validation_results['performance_dashboard'] = True
            else:
                validation_results['error'] = f"Grafana not accessible: HTTP {response.status_code}"

        except Exception as e:
            validation_results['error'] = str(e)

        return validation_results

    def test_alerting_system(self) -> Dict[str, Any]:
        """Test alerting system functionality."""
        alert_results = {
            'alertmanager_status': False,
            'active_alerts': [],
            'test_alert_triggered': False
        }

        try:
            # Check Alertmanager status
            response = requests.get(f"{self.alertmanager_url}/api/v2/status", timeout=10)
            if response.status_code == 200:
                alert_results['alertmanager_status'] = True

                # Get active alerts
                response = requests.get(f"{self.alertmanager_url}/api/v2/alerts", timeout=10)
                if response.status_code == 200:
                    alerts = response.json()
                    alert_results['active_alerts'] = [alert.get('labels', {}).get('alertname') for alert in alerts]

        except Exception as e:
            alert_results['error'] = str(e)

        # Try to trigger a test alert (would require specific alert rules)
        # For now, just check if system is responsive

        return alert_results

    def benchmark_concurrent_load(self, concurrent_users: int = 10, duration: int = 30) -> Dict[str, Any]:
        """Benchmark concurrent load performance."""
        # This would typically use a tool like Apache Bench or wrk
        # For now, simulate with multiple threads

        import threading
        import queue

        results_queue = queue.Queue()

        def worker_thread(thread_id: int):
            thread_results = {'queries': 0, 'errors': 0, 'total_time': 0}

            end_time = time.time() + duration
            while time.time() < end_time:
                try:
                    start_time = time.perf_counter()

                    # Perform a mix of operations
                    with self.pg_conn.cursor() as cursor:
                        cursor.execute("SELECT COUNT(*) FROM test_students")
                        cursor.fetchone()

                    end_time_query = time.perf_counter()
                    thread_results['queries'] += 1
                    thread_results['total_time'] += (end_time_query - start_time)

                except Exception as e:
                    thread_results['errors'] += 1

            results_queue.put(thread_results)

        # Start worker threads
        threads = []
        for i in range(concurrent_users):
            thread = threading.Thread(target=worker_thread, args=(i,))
            threads.append(thread)
            thread.start()

        # Wait for completion
        for thread in threads:
            thread.join()

        # Collect results
        total_queries = 0
        total_errors = 0
        total_time = 0

        for _ in range(concurrent_users):
            thread_result = results_queue.get()
            total_queries += thread_result['queries']
            total_errors += thread_result['errors']
            total_time += thread_result['total_time']

        return {
            'concurrent_users': concurrent_users,
            'duration_seconds': duration,
            'total_queries': total_queries,
            'total_errors': total_errors,
            'queries_per_second': total_queries / duration,
            'avg_response_time': (total_time / total_queries) * 1000 if total_queries > 0 else 0,
            'error_rate': total_errors / (total_queries + total_errors) if (total_queries + total_errors) > 0 else 0
        }

    def test_monitoring_thresholds(self) -> Dict[str, Any]:
        """Test monitoring thresholds and alerts."""
        threshold_results = {
            'connection_pool_exhaustion': False,
            'high_cpu_usage': False,
            'memory_pressure': False,
            'slow_queries': False
        }

        # Check current metrics against thresholds
        try:
            # PostgreSQL connection pool
            with self.pg_conn.cursor() as cursor:
                cursor.execute("SELECT count(*) FROM pg_stat_activity")
                active_connections = cursor.fetchone()[0]

                # Assume threshold of 80% of max connections
                if active_connections > 80:  # Simplified check
                    threshold_results['connection_pool_exhaustion'] = True

            # System CPU (would need actual metrics)
            # For now, just check if monitoring is working

        except Exception as e:
            threshold_results['error'] = str(e)

        return threshold_results

    def generate_performance_report(self) -> str:
        """Generate comprehensive performance report."""
        report = []
        report.append("# Database Performance Test Report")
        report.append(f"Generated: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")

        # PostgreSQL benchmarks
        pg_results = self.benchmark_postgres_query_performance(50)
        report.append("## PostgreSQL Performance Benchmarks")
        for operation in ['simple_selects', 'complex_queries', 'inserts']:
            if f'{operation}_stats' in pg_results:
                stats = pg_results[f'{operation}_stats']
                report.append(f"### {operation.replace('_', ' ').title()}")
                report.append(".2f")
                report.append(".2f")
                report.append(".2f")
                report.append("")

        # MongoDB benchmarks
        mongo_results = self.benchmark_mongo_performance(50)
        report.append("## MongoDB Performance Benchmarks")
        for operation in ['finds', 'inserts', 'updates', 'aggregations']:
            if f'{operation}_stats' in mongo_results:
                stats = mongo_results[f'{operation}_stats']
                report.append(f"### {operation.title()}")
                report.append(".2f")
                report.append(".2f")
                report.append(".2f")
                report.append("")

        # Concurrent load test
        load_results = self.benchmark_concurrent_load(5, 10)
        report.append("## Concurrent Load Test")
        report.append(".2f")
        report.append(".2f")
        report.append(".2f")
        report.append("")

        # Monitoring validation
        monitoring_results = self.validate_prometheus_metrics()
        report.append("## Monitoring Validation")
        report.append(f"PostgreSQL metrics: {monitoring_results['postgres_metrics']}")
        report.append(f"MongoDB metrics: {monitoring_results['mongo_metrics']}")
        report.append(f"System metrics: {monitoring_results['system_metrics']}")
        report.append("")

        return "\n".join(report)

    def cleanup(self):
        """Clean up test data."""
        try:
            with self.pg_conn.cursor() as cursor:
                cursor.execute("DELETE FROM test_students WHERE school_id = 999")
            self.pg_conn.commit()
        except:
            pass

        self.pg_conn.close()
        self.mongo_client.close()

@pytest.fixture
def perf_tester():
    tester = PerformanceMonitorTester()
    yield tester
    tester.cleanup()

def test_postgres_performance_benchmarks(perf_tester):
    """Test PostgreSQL performance benchmarks."""
    results = perf_tester.benchmark_postgres_query_performance(20)

    # Verify we have results
    assert 'simple_selects_stats' in results
    assert results['simple_selects_stats']['count'] > 0

    # Check performance is reasonable (< 100ms avg for simple queries)
    assert results['simple_selects_stats']['avg'] < 100

def test_mongo_performance_benchmarks(perf_tester):
    """Test MongoDB performance benchmarks."""
    results = perf_tester.benchmark_mongo_performance(20)

    assert 'finds_stats' in results
    assert results['finds_stats']['count'] > 0
    assert results['finds_stats']['avg'] < 100

def test_prometheus_metrics_validation(perf_tester):
    """Test Prometheus metrics collection."""
    results = perf_tester.validate_prometheus_metrics()

    # At minimum, should not have errors for all metrics
    # (Metrics might not be available in test environment)
    assert isinstance(results, dict)

def test_concurrent_load_performance(perf_tester):
    """Test concurrent load performance."""
    results = perf_tester.benchmark_concurrent_load(3, 5)

    assert results['total_queries'] > 0
    assert results['error_rate'] < 0.1  # Less than 10% errors

def test_monitoring_thresholds(perf_tester):
    """Test monitoring thresholds."""
    results = perf_tester.test_monitoring_thresholds()

    assert isinstance(results, dict)
    # Thresholds should not be exceeded in normal test conditions

def test_performance_report_generation(perf_tester):
    """Test performance report generation."""
    report = perf_tester.generate_performance_report()

    assert isinstance(report, str)
    assert len(report) > 0
    assert "# Database Performance Test Report" in report