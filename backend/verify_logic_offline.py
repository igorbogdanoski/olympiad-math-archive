import sys
import os

# Add the current directory to path so we can import worksheet_generator
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from worksheet_generator import generate_worksheet_html

def verify():
    code = "MAT-O-G8-T3-S1"
    print(f"Generating worksheet for {code} offline...")
    
    html = generate_worksheet_html(code, teacher_mode=True)
    
    if html:
        output_file = "verify_offline_result.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Success! Output saved to {output_file}")
        
        # Simple check for expected tags
        if "content-body" in html:
            print("Check passed: 'content-body' found in HTML.")
        else:
            print("Check FAILED: 'content-body' NOT found in HTML.")
            
        if "teacher-mode" in html:
            print("Check passed: 'teacher-mode' found in body class.")
            
        if "\\\(" in html or "\\\[" in html:
             print("Check passed: LaTeX escaped delimiters found.")
    else:
        print("Failed to generate HTML. Check if MongoDB is running and has the data.")

if __name__ == "__main__":
    verify()
