"""
Batch Process GeoGebra Matching for All Problems
Processes problems.json and generates GeoGebra ID suggestions
"""

import sys
import json
from pathlib import Path

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent))

from geogebra_matcher import GeoGebraAutoMatcher

def load_problems():
    """Load problems from web/src/data/problems.json"""
    problems_path = Path(__file__).parent.parent / "web" / "src" / "data" / "problems.json"
    
    if not problems_path.exists():
        print(f"❌ Problems file not found: {problems_path}")
        sys.exit(1)
    
    with open(problems_path, 'r', encoding='utf-8') as f:
        problems = json.load(f)
    
    print(f"✅ Loaded {len(problems)} problems")
    return problems

def filter_geometry_problems(problems):
    """Filter to only geometry/visual problems that benefit from GeoGebra"""
    filtered = []
    
    geometry_keywords = [
        'триаголник', 'кружница', 'агол', 'паралелограм', 'трапез',
        'ромб', 'квадрат', 'правоаголник', 'височина', 'медијана',
        'биссектриса', 'тангент', 'хорда', 'геометр', 'график',
        'функција', 'координат', 'парабола'
    ]
    
    for problem in problems:
        body = problem.get('body', '').lower()
        category = problem.get('category', '').lower()
        topic = problem.get('meta', {}).get('topic', '').lower()
        
        # Check if geometry-related
        is_geometry = (
            'геометрија' in category or
            'geometry' in topic or
            any(keyword in body for keyword in geometry_keywords)
        )
        
        if is_geometry:
            filtered.append(problem)
    
    print(f"✅ Filtered to {len(filtered)} geometry/visual problems")
    return filtered

def main():
    print("=" * 60)
    print("🎯 GeoGebra Auto-Matcher - Batch Processing")
    print("=" * 60)
    
    # Load problems
    print("\n📚 Step 1: Loading problems...")
    problems = load_problems()
    
    # Filter to geometry
    print("\n🔍 Step 2: Filtering to geometry/visual problems...")
    geometry_problems = filter_geometry_problems(problems)
    
    # Initialize matcher
    print("\n🤖 Step 3: Initializing AI matcher...")
    try:
        matcher = GeoGebraAutoMatcher()
    except ValueError as e:
        print(f"❌ Error: {e}")
        print("\n💡 Set GEMINI_API_KEY environment variable:")
        print("   $env:GEMINI_API_KEY='your-api-key-here'  # PowerShell")
        sys.exit(1)
    
    # Batch process (start with first 50 for testing)
    print("\n🚀 Step 4: Processing problems...")
    print(f"   Processing first 50 problems for testing...")
    
    test_batch = geometry_problems[:50]
    results = matcher.batch_process(test_batch, "geogebra_matches_batch1.json")
    
    print("\n✅ Batch processing complete!")
    print(f"\n📋 Next steps:")
    print(f"   1. Review: tools/geogebra_matches_batch1.json")
    print(f"   2. Validate high-confidence matches")
    print(f"   3. Process remaining problems")
    print(f"   4. Update problems.json with approved IDs")

if __name__ == "__main__":
    main()
