import requests
import time

url = "http://127.0.0.1:8000/generate-video"
data = {
    "text": "Именува, опишува и групира 2Д-форми (триаголник, квадрат, круг).",
    "grade": "I"
}

print(f"Sending request to {url}...")
try:
    response = requests.post(url, json=data, timeout=300) # Long timeout for rendering
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {e}")
