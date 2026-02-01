import os
from dotenv import dotenv_values

env_path = os.path.join(os.path.dirname(__file__), '.env')
config = dotenv_values(env_path)
print(f"Config keys: {list(config.keys())}")
if 'GOOGLE_API_KEY' in config:
    val = config['GOOGLE_API_KEY']
    print(f"GOOGLE_API_KEY: {val[:5]}...{val[-5:]}")
else:
    print("GOOGLE_API_KEY not found in .env")
