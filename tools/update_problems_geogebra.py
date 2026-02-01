"""
Update problems.json with approved GeoGebra material IDs
Reads geogebra_approved_matches.json and updates problems.json
"""

import json
from pathlib import Path

def load_json(file_path: Path) -> dict:
    """Load JSON file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(file_path: Path, data: dict):
    """Save JSON file with formatting"""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def update_problems_with_geogebra():
    """Main function to update problems.json with approved GeoGebra IDs"""
    
    # Paths
    root_dir = Path(__file__).parent
    matches_file = root_dir / "geogebra_approved_matches.json"
    problems_file = root_dir / "web" / "src" / "data" / "problems.json"
    
    if not matches_file.exists():
        print(f"❌ Matches file not found: {matches_file}")
        return
    
    if not problems_file.exists():
        print(f"❌ Problems file not found: {problems_file}")
        return
    
    # Load data
    print("📂 Loading data...")
    matches = load_json(matches_file)
    problems = load_json(problems_file)
    
    # Filter approved matches only
    approved = [m for m in matches if m.get('status') == 'approved']
    print(f"✅ Found {len(approved)} approved matches")
    
    if len(approved) == 0:
        print("⚠️  No approved matches to process")
        return
    
    # Create lookup map: problem_id -> material_id
    match_map = {m['problem_id']: m['material_id'] for m in approved}
    
    # Update problems
    updated_count = 0
    for problem in problems:
        problem_id = problem.get('id')
        if problem_id in match_map:
            old_id = problem.get('geogebra_id')
            new_id = match_map[problem_id]
            
            if old_id != new_id:
                problem['geogebra_id'] = new_id
                updated_count += 1
                print(f"  ✓ Updated {problem_id}: {old_id or 'None'} → {new_id}")
    
    # Backup original
    backup_file = problems_file.with_suffix('.json.backup')
    print(f"\n💾 Backing up original to: {backup_file}")
    save_json(backup_file, problems)
    
    # Save updated problems
    print(f"💾 Saving updated problems to: {problems_file}")
    save_json(problems_file, problems)
    
    # Stats
    print(f"\n📊 Summary:")
    print(f"  - Total problems: {len(problems)}")
    print(f"  - Approved matches: {len(approved)}")
    print(f"  - Updated problems: {updated_count}")
    print(f"  - GeoGebra coverage: {len([p for p in problems if p.get('geogebra_id')])} / {len(problems)} ({len([p for p in problems if p.get('geogebra_id')]) / len(problems) * 100:.1f}%)")
    
    print("\n✅ Update complete!")

if __name__ == "__main__":
    update_problems_with_geogebra()
