import requests
import json

url = "http://localhost:8000/generate-worksheet"
headers = {"Content-Type": "application/json"}

def test_gen(code, teacher_mode=False):
    payload = {"standardCode": code, "teacherMode": teacher_mode}
    print(f"Testing {code} (Teacher: {teacher_mode})...")
    try:
        response = requests.post(url, json=payload, headers=headers)
        if response.status_code == 200:
            data = response.json()
            filename = f"test_worksheet_{'teacher' if teacher_mode else 'student'}.html"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(data['html'])
            print(f"Success! Saved to {filename}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Exception: {e}")

test_gen("MAT-O-G8-T3-S1", False)
test_gen("MAT-O-G8-T3-S1", True)
