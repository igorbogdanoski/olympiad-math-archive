#!/bin/bash
set -e

# PostgreSQL Backup Script for Citus Cluster
# Uses wal-g for S3-compatible storage

# Configuration
S3_BUCKET="your-backup-bucket"
S3_PREFIX="postgres"
AWS_REGION="us-east-1"
BACKUP_TYPE="${1:-full}"  # full or incremental
RETENTION_DAYS_HOT=30
RETENTION_DAYS_COLD=365

# Environment variables (set in container or env file)
# WALG_S3_PREFIX=s3://$S3_BUCKET/$S3_PREFIX
# AWS_ACCESS_KEY_ID
# AWS_SECRET_ACCESS_KEY

export WALG_S3_PREFIX="s3://$S3_BUCKET/$S3_PREFIX"
export AWS_REGION

# Database connection
PGHOST="${PGHOST:-citus_coordinator}"
PGPORT="${PGPORT:-5432}"
PGUSER="${PGUSER:-postgres}"
PGDATABASE="${PGDATABASE:-olympiad_core}"

# Set password if needed
export PGPASSWORD="$POSTGRES_PASSWORD"

# Function to perform full backup
perform_full_backup() {
    echo "Starting full backup with wal-g..."
    wal-g backup-push /var/lib/postgresql/data
    echo "Full backup completed."
}

# Function to perform incremental backup (if supported)
perform_incremental_backup() {
    echo "Performing incremental backup (using full for now)..."
    perform_full_backup
}

# Function to clean up old backups
cleanup_old_backups() {
    echo "Cleaning up old backups..."
    # Keep hot storage for 30 days
    wal-g delete retain FIND_FULL "$RETENTION_DAYS_HOT" --confirm
    # For cold storage, we might need a separate script or bucket
    echo "Cleanup completed."
}

# Main logic
case $BACKUP_TYPE in
    full)
        perform_full_backup
        ;;
    incremental)
        perform_incremental_backup
        ;;
    cleanup)
        cleanup_old_backups
        ;;
    *)
        echo "Usage: $0 {full|incremental|cleanup}"
        exit 1
        ;;
esac

# Log backup info
echo "Backup operation completed at $(date)"