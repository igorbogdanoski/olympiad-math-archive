import json
import sys

target = 'tools/problems.json'
try:
    with open(target, 'r', encoding='utf-8') as f:
        json.load(f)
    print(f"{target} is valid")
except json.JSONDecodeError as e:
    print(f"{target} Error: {e}")
except Exception as e:
    print(f"Other Error: {e}")
