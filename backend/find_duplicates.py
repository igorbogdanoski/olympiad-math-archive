import os
import hashlib

def get_hash(path):
    with open(path, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

files = {}
for root, _, filenames in os.walk('problems'):
    for f in filenames:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            h = get_hash(path)
            if h in files:
                print(f"Duplicate found: {path} and {files[h]}")
            else:
                files[h] = path
