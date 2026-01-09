import os
import sys
from pathlib import Path

# Додај ја tools папката во патеката за импорт
tools_dir = Path(__file__).parent.resolve()
sys.path.append(str(tools_dir))

import indexer

def main():
    base_dir = tools_dir.parent
    print(f"Refreshing index from: {base_dir}")
    
    problems = indexer.build_index(str(base_dir))
    
    # Патеки за зачувување
    index_path = base_dir / "web" / "src" / "data" / "problems.json"
    public_index_path = base_dir / "web" / "public" / "data" / "problems.json"
    
    # Осигурај се дека фолдерите постојат
    index_path.parent.mkdir(parents=True, exist_ok=True)
    public_index_path.parent.mkdir(parents=True, exist_ok=True)
    
    indexer.save_index(problems, str(index_path))
    indexer.save_index(problems, str(public_index_path))
    
    print(f"SUCCESS: Index refreshed with {len(problems)} genuine math problems.")

if __name__ == "__main__":
    main()
