#!/bin/bash
# Production MongoDB Import Script (Expert Version)
# Run this on the production server after SCP upload

set -e  # Exit on error

echo "🚀 Production Database Import - Expert Mode"
echo "============================================"

# Configuration
DB_HOST="localhost"
DB_PORT="27035"
DB_NAME="olympiad_db"
COLLECTION="problems"
JSON_FILE="/tmp/problems_export.json"

# Check if file exists
if [ ! -f "$JSON_FILE" ]; then
    echo "❌ Error: $JSON_FILE not found!"
    echo "💡 Upload file first: scp problems_export.json root@76.13.129.9:/tmp/"
    exit 1
fi

echo "📄 File found: $JSON_FILE"
FILE_SIZE=$(du -h "$JSON_FILE" | cut -f1)
echo "📦 File size: $FILE_SIZE"

# Count existing problems (before import)
echo ""
echo "🔍 Checking existing problems..."
BEFORE_COUNT=$(mongosh --quiet --host $DB_HOST:$DB_PORT $DB_NAME --eval "db.problems.count()" 2>/dev/null || echo "0")
echo "📊 Current problems in database: $BEFORE_COUNT"

# Backup existing data (if any)
if [ "$BEFORE_COUNT" -gt 0 ]; then
    echo ""
    echo "⚠️  WARNING: Database contains $BEFORE_COUNT problems"
    echo "🗑️  Clearing existing problems before import..."
    mongosh --quiet --host $DB_HOST:$DB_PORT $DB_NAME --eval "db.problems.deleteMany({})" > /dev/null
    echo "✅ Cleared old problems"
fi

# Import problems
echo ""
echo "📥 Importing problems from JSON..."
mongoimport \
    --host $DB_HOST:$DB_PORT \
    --db $DB_NAME \
    --collection $COLLECTION \
    --file $JSON_FILE \
    --jsonArray \
    --drop 2>&1 | grep -E "(imported|failed|error)" || true

# Verify import
echo ""
echo "🔍 Verifying import..."
AFTER_COUNT=$(mongosh --quiet --host $DB_HOST:$DB_PORT $DB_NAME --eval "db.problems.count()" 2>/dev/null || echo "0")
echo "📊 Problems after import: $AFTER_COUNT"

if [ "$AFTER_COUNT" -gt 0 ]; then
    echo ""
    echo "✅ SUCCESS! Imported $AFTER_COUNT problems"
    
    # Show statistics
    echo ""
    echo "📊 Database Statistics:"
    mongosh --quiet --host $DB_HOST:$DB_PORT $DB_NAME --eval "
        print('   By Grade:');
        db.problems.aggregate([
            { \$group: { _id: '\$grade', count: { \$sum: 1 } } },
            { \$sort: { _id: 1 } }
        ]).forEach(g => print('     Grade ' + g._id + ': ' + g.count));
        
        print('');
        print('   By Category:');
        db.problems.aggregate([
            { \$group: { _id: '\$category', count: { \$sum: 1 } } },
            { \$sort: { count: -1 } }
        ]).forEach(c => print('     ' + c._id + ': ' + c.count));
    " 2>/dev/null
    
    # Cleanup
    echo ""
    echo "🧹 Cleaning up..."
    rm -f "$JSON_FILE"
    echo "✅ Removed temporary file"
    
    echo ""
    echo "🎉 DEPLOYMENT COMPLETE!"
    echo ""
    echo "🌐 Test the API:"
    echo "   curl http://localhost:8000/api/dashboard/stats | jq '.stats.problems_count'"
    echo ""
    echo "🌐 Test the website:"
    echo "   https://app.mismath.net/"
    echo "   (Hard refresh: Ctrl+Shift+R)"
    
else
    echo ""
    echo "❌ IMPORT FAILED! No problems in database."
    echo "💡 Check MongoDB logs for errors"
    exit 1
fi
