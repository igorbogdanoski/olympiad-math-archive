#!/usr/bin/env python3
"""
Database Testing Suite Runner

This script runs comprehensive tests for PostgreSQL Citus cluster, MongoDB sharded cluster,
CDC synchronization, backup/recovery, and multi-AZ failover scenarios.
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path

def run_pytest(test_path: str, extra_args: list = None) -> int:
    """Run pytest on specified path."""
    cmd = [sys.executable, '-m', 'pytest', test_path, '-v', '--tb=short']
    if extra_args:
        cmd.extend(extra_args)
    return subprocess.run(cmd, cwd=Path(__file__).parent).returncode

def run_locust(test_file: str) -> int:
    """Run Locust load testing."""
    cmd = [sys.executable, '-m', 'locust', '-f', test_file, '--headless', '-u', '100', '-r', '10', '--run-time', '30s']
    return subprocess.run(cmd, cwd=Path(__file__).parent).returncode

def run_bash_script(script_path: str) -> int:
    """Run bash script."""
    return subprocess.run(['bash', script_path], cwd=Path(__file__).parent).returncode

def main():
    parser = argparse.ArgumentParser(description='Database Testing Suite Runner')
    parser.add_argument('--unit', action='store_true', help='Run unit tests')
    parser.add_argument('--integration', action='store_true', help='Run integration tests')
    parser.add_argument('--scalability', action='store_true', help='Run scalability tests')
    parser.add_argument('--failover', action='store_true', help='Run failover tests')
    parser.add_argument('--synchronization', action='store_true', help='Run synchronization tests')
    parser.add_argument('--backup-recovery', action='store_true', help='Run backup/recovery tests')
    parser.add_argument('--multi-az', action='store_true', help='Run multi-AZ tests')
    parser.add_argument('--performance', action='store_true', help='Run performance benchmarks')
    parser.add_argument('--all', action='store_true', help='Run all tests')
    parser.add_argument('--setup', action='store_true', help='Setup test environment')

    args = parser.parse_args()

    if args.setup:
        print("Setting up test environment...")
        # Install requirements if needed
        subprocess.run([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'], cwd=Path(__file__).parent)
        print("Test environment setup complete.")
        return 0

    if args.all:
        args.unit = args.integration = args.scalability = args.failover = args.synchronization = args.backup_recovery = args.multi_az = args.performance = True

    results = []

    if args.unit:
        print("Running unit tests...")
        results.append(("Unit Tests", run_pytest('unit/')))

    if args.integration:
        print("Running integration tests...")
        results.append(("Integration Tests", run_pytest('integration/')))

    if args.scalability:
        print("Running scalability tests...")
        # Assuming there's a locust file
        if Path('scalability/load_test.py').exists():
            results.append(("Scalability Tests", run_locust('scalability/load_test.py')))
        else:
            results.append(("Scalability Tests", run_pytest('scalability/')))

    if args.failover:
        print("Running failover tests...")
        results.append(("Failover Tests", run_pytest('failover/')))

    if args.synchronization:
        print("Running synchronization tests...")
        results.append(("Synchronization Tests", run_pytest('synchronization/')))

    if args.backup_recovery:
        print("Running backup/recovery tests...")
        results.append(("Backup/Recovery Tests", run_pytest('backup_recovery/')))

    if args.multi_az:
        print("Running multi-AZ tests...")
        results.append(("Multi-AZ Tests", run_pytest('multi_az/')))

    if args.performance:
        print("Running performance benchmarks...")
        results.append(("Performance Benchmarks", run_pytest('performance/')))

    # Print summary
    print("\n" + "="*50)
    print("TEST RESULTS SUMMARY")
    print("="*50)

    all_passed = True
    for test_name, return_code in results:
        status = "PASSED" if return_code == 0 else "FAILED"
        print(f"{test_name}: {status}")
        if return_code != 0:
            all_passed = False

    print("="*50)
    overall_status = "ALL TESTS PASSED" if all_passed else "SOME TESTS FAILED"
    print(f"Overall: {overall_status}")

    return 0 if all_passed else 1

if __name__ == '__main__':
    sys.exit(main())