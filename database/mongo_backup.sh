#!/bin/bash
set -e

# MongoDB Backup Script for Sharded Cluster
# Uses mongodump for snapshots and oplog backup

# Configuration
S3_BUCKET="your-backup-bucket"
S3_PREFIX="mongo"
AWS_REGION="us-east-1"
BACKUP_TYPE="${1:-snapshot}"  # snapshot or oplog
RETENTION_DAYS_HOT=30
RETENTION_DAYS_COLD=365

# MongoDB connection
MONGO_HOST="${MONGO_HOST:-mongos1}"
MONGO_PORT="${MONGO_PORT:-27017}"
MONGO_USER="${MONGO_USER:-admin}"
MONGO_PASS="${MONGO_PASS:-securepassword123}"
MONGO_DB="${MONGO_DB:-olympiad_db}"

# Backup directory
BACKUP_DIR="/backup/mongo_$(date +%Y%m%d_%H%M%S)"

# Function to perform snapshot backup
perform_snapshot_backup() {
    echo "Starting MongoDB snapshot backup..."
    mkdir -p $BACKUP_DIR

    # Dump the database with oplog for PITR
    mongodump \
        --host $MONGO_HOST:$MONGO_PORT \
        --username $MONGO_USER \
        --password $MONGO_PASS \
        --authenticationDatabase admin \
        --db $MONGO_DB \
        --out $BACKUP_DIR \
        --oplog

    echo "Snapshot backup completed."

    # Upload to S3 (assuming AWS CLI is available)
    if command -v aws &> /dev/null; then
        aws s3 cp $BACKUP_DIR s3://$S3_BUCKET/$S3_PREFIX/ --recursive --region $AWS_REGION
        echo "Backup uploaded to S3."
    else
        echo "AWS CLI not found, backup saved locally at $BACKUP_DIR"
    fi

    # Clean local backup
    rm -rf $BACKUP_DIR
}

# Function to perform oplog-only backup (for continuous PITR)
perform_oplog_backup() {
    echo "Starting oplog backup..."
    mkdir -p $BACKUP_DIR/oplog

    # Get oplog data
    mongo --host $MONGO_HOST:$MONGO_PORT \
        --username $MONGO_USER \
        --password $MONGO_PASS \
        --authenticationDatabase admin \
        --eval "db.getSiblingDB('local').oplog.rs.find().forEach(function(doc){printjson(doc);})" > $BACKUP_DIR/oplog.json

    echo "Oplog backup completed."

    # Upload to S3
    if command -v aws &> /dev/null; then
        aws s3 cp $BACKUP_DIR s3://$S3_BUCKET/$S3_PREFIX/oplog/ --recursive --region $AWS_REGION
        echo "Oplog uploaded to S3."
    fi

    rm -rf $BACKUP_DIR
}

# Function to clean up old backups
cleanup_old_backups() {
    echo "Cleaning up old MongoDB backups..."
    # Use AWS CLI to delete old objects
    if command -v aws &> /dev/null; then
        # Delete backups older than hot retention
        aws s3api list-objects-v2 --bucket $S3_BUCKET --prefix $S3_PREFIX \
            --query 'Contents[?LastModified<`'"$(date -d "-$RETENTION_DAYS_HOT days" +%Y-%m-%d)"'`].Key' \
            --output text | xargs -I {} aws s3 rm s3://$S3_BUCKET/{}

        echo "Old backups cleaned up."
    else
        echo "AWS CLI not available, manual cleanup required."
    fi
}

# Main logic
case $BACKUP_TYPE in
    snapshot)
        perform_snapshot_backup
        ;;
    oplog)
        perform_oplog_backup
        ;;
    cleanup)
        cleanup_old_backups
        ;;
    *)
        echo "Usage: $0 {snapshot|oplog|cleanup}"
        exit 1
        ;;
esac

echo "MongoDB backup operation completed at $(date)"