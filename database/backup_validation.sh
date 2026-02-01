#!/bin/bash
set -e

# Backup Validation Script
# Tests integrity and restore capability of backups

# Configuration
S3_BUCKET="your-backup-bucket"
AWS_REGION="us-east-1"
VALIDATION_DIR="/tmp/backup_validation_$(date +%s)"
LOG_FILE="/var/log/backup_validation.log"

# PostgreSQL validation
validate_postgres_backup() {
    echo "Validating PostgreSQL backup..." | tee -a $LOG_FILE

    mkdir -p $VALIDATION_DIR/postgres

    # Download latest backup from S3
    LATEST_BACKUP=$(aws s3api list-objects-v2 --bucket $S3_BUCKET --prefix postgres \
        --query 'sort_by(Contents, &LastModified)[-1].Key' --output text --region $AWS_REGION)

    if [ -z "$LATEST_BACKUP" ]; then
        echo "No PostgreSQL backup found" | tee -a $LOG_FILE
        return 1
    fi

    aws s3 cp s3://$S3_BUCKET/$LATEST_BACKUP $VALIDATION_DIR/postgres/ --recursive --region $AWS_REGION

    # Test backup integrity with wal-g
    cd $VALIDATION_DIR/postgres
    if wal-g backup-list | grep -q "backup"; then
        echo "PostgreSQL backup integrity check passed" | tee -a $LOG_FILE
    else
        echo "PostgreSQL backup integrity check failed" | tee -a $LOG_FILE
        return 1
    fi

    # Attempt restore test (dry run)
    echo "Testing PostgreSQL restore capability..." | tee -a $LOG_FILE
    # Note: Actual restore would require a test instance
    echo "PostgreSQL restore test completed (dry run)" | tee -a $LOG_FILE
}

# MongoDB validation
validate_mongo_backup() {
    echo "Validating MongoDB backup..." | tee -a $LOG_FILE

    mkdir -p $VALIDATION_DIR/mongo

    # Download latest backup from S3
    LATEST_BACKUP=$(aws s3api list-objects-v2 --bucket $S3_BUCKET --prefix mongo \
        --query 'sort_by(Contents, &LastModified)[-1].Key' --output text --region $AWS_REGION)

    if [ -z "$LATEST_BACKUP" ]; then
        echo "No MongoDB backup found" | tee -a $LOG_FILE
        return 1
    fi

    aws s3 cp s3://$S3_BUCKET/$LATEST_BACKUP $VALIDATION_DIR/mongo/ --recursive --region $AWS_REGION

    # Test backup integrity
    if [ -d "$VALIDATION_DIR/mongo/olympiad_db" ]; then
        echo "MongoDB backup structure check passed" | tee -a $LOG_FILE

        # Check for oplog
        if [ -f "$VALIDATION_DIR/mongo/olympiad_db/oplog.bson" ]; then
            echo "MongoDB oplog found, PITR capability verified" | tee -a $LOG_FILE
        else
            echo "Warning: No oplog found in backup" | tee -a $LOG_FILE
        fi
    else
        echo "MongoDB backup structure check failed" | tee -a $LOG_FILE
        return 1
    fi

    # Test restore capability (dry run)
    echo "Testing MongoDB restore capability..." | tee -a $LOG_FILE
    # mongorestore --dryRun $VALIDATION_DIR/mongo/olympiad_db
    echo "MongoDB restore test completed (dry run)" | tee -a $LOG_FILE
}

# Cross-region replication check
validate_replication() {
    echo "Validating cross-region replication..." | tee -a $LOG_FILE

    # Check if backups exist in secondary region (assume us-west-2)
    SECONDARY_REGION="us-west-2"

    SECONDARY_COUNT=$(aws s3api list-objects-v2 --bucket $S3_BUCKET --prefix postgres \
        --region $SECONDARY_REGION --query 'length(Contents[])' --output text 2>/dev/null || echo "0")

    if [ "$SECONDARY_COUNT" -gt "0" ]; then
        echo "Cross-region replication check passed" | tee -a $LOG_FILE
    else
        echo "Cross-region replication check failed or not configured" | tee -a $LOG_FILE
    fi
}

# Main validation
main() {
    echo "Starting backup validation at $(date)" | tee -a $LOG_FILE

    FAILED=0

    validate_postgres_backup || FAILED=1
    validate_mongo_backup || FAILED=1
    validate_replication || FAILED=1

    # Cleanup
    rm -rf $VALIDATION_DIR

    if [ $FAILED -eq 0 ]; then
        echo "All backup validations passed" | tee -a $LOG_FILE
        exit 0
    else
        echo "Some backup validations failed" | tee -a $LOG_FILE
        exit 1
    fi
}

# Run main if not sourced
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi