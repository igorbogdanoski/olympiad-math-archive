#!/bin/bash
# Quick Production Database Setup (Expert Version)
# Run this script on production server to populate MongoDB with all problems

set -e

echo "🚀 Quick Database Setup for Production"
echo "======================================"
echo ""

# Configuration
REPO_DIR="/opt/olympiad-math-archive"
DB_HOST="localhost:27035"
DB_NAME="olympiad_db"

cd "$REPO_DIR/backend"

echo "📊 Counting existing problems..."
EXISTING=$(python3 -c "import pymongo; c=pymongo.MongoClient('mongodb://$DB_HOST/'); print(c['$DB_NAME']['problems'].count_documents({}))" 2>/dev/null || echo "0")
echo "   Current: $EXISTING problems"

if [ "$EXISTING" -gt "100" ]; then
    echo "✅ Database already populated ($EXISTING problems)"
    echo "💡 Skipping import. Use ./clear_and_reimport.sh to reset."
    exit 0
fi

echo ""
echo "📥 Running import scripts..."
echo ""

# Find all import scripts
IMPORT_SCRIPTS=$(find . -name "import_*.py" | sort)
TOTAL=$(echo "$IMPORT_SCRIPTS" | wc -l)
CURRENT=0

for script in $IMPORT_SCRIPTS; do
    CURRENT=$((CURRENT + 1))
    SCRIPT_NAME=$(basename "$script")
    echo "[$CURRENT/$TOTAL] Running $SCRIPT_NAME..."
    
    python3 "$script" 2>&1 | grep -E "(Successfully|Error|inserted)" || echo "   ✅ Completed"
done

echo ""
echo "🔍 Verifying import..."
FINAL_COUNT=$(python3 -c "import pymongo; c=pymongo.MongoClient('mongodb://$DB_HOST/'); print(c['$DB_NAME']['problems'].count_documents({}))")
echo "📊 Total problems in database: $FINAL_COUNT"

if [ "$FINAL_COUNT" -gt "100" ]; then
    echo ""
    echo "✅ SUCCESS! Database populated with $FINAL_COUNT problems"
    
    echo ""
    echo "📊 Statistics:"
    python3 << 'PYEOF'
import pymongo
client = pymongo.MongoClient('mongodb://localhost:27035/')
db = client['olympiad_db']

# By grade
print("   By Grade:")
grades = db.problems.aggregate([
    {"$group": {"_id": "$grade", "count": {"$sum": 1}}},
    {"$sort": {"_id": 1}}
])
for g in grades:
    print(f"     Grade {g['_id']}: {g['count']}")

# By category
print("\n   By Category:")
categories = db.problems.aggregate([
    {"$group": {"_id": "$category", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
])
for c in categories:
    print(f"     {c['_id']}: {c['count']}")

client.close()
PYEOF
    
    echo ""
    echo "🌐 Test the deployment:"
    echo "   1. Backend API: curl http://localhost:8000/api/dashboard/stats | jq"
    echo "   2. Website: https://app.mismath.net/ (Ctrl+Shift+R)"
    echo ""
    echo "🎉 READY FOR USE!"
else
    echo ""
    echo "⚠️  WARNING: Only $FINAL_COUNT problems imported"
    echo "💡 Some import scripts may have failed. Check logs above."
fi
