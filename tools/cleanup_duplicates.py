import os
import re

ARCHIVE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../"))

def clean_duplicates():
    print("🧹 Cleaning up duplicate Geo-Mentor blocks...")
    
    count = 0
    for root, dirs, files in os.walk(ARCHIVE_ROOT):
        if "tools" in root or "assets" in root: continue
        
        for file in files:
            if file.endswith(".md"):
                path = os.path.join(root, file)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Define the block pattern
                    # We look for the header line, followed by some text, then empty lines, then the header again
                    
                    # Pattern for the header
                    header = "> **👨‍💻 Geo-Mentor Code:**"
                    
                    if content.count(header) > 1:
                        print(f"📄 Found duplicates in: {file}")
                        
                        # Split by lines to handle it safely
                        lines = content.split(r'\n')
                        new_lines = []
                        seen_header = False
                        skip_until_next_section = False
                        
                        # This is a bit complex to do line-by-line because we need to know when the block ends.
                        # Simpler approach: Use regex to replace the second occurrence.
                        
                        # Regex to match the full block:
                        # > **👨‍💻 Geo-Mentor Code:**\n> .*?(\n\n|$)
                        
                        block_pattern = r"(> \*\*👨‍💻 Geo-Mentorr Code:\*\*.*?(?:\n> .*?)*)(\n\s*){2,}r
                        
                        # Find all matches
                        matches = list(re.finditer(block_pattern, content, re.DOTALL))
                        
                        if not matches:
                            # Maybe the spacing is different
                            block_pattern = r"(> \*\*👨‍💻 Geo-Mentorr Code:\*\*.*?(?:\n> .*?)*)r
                            matches = list(re.finditer(block_pattern, content, re.DOTALL))
                        
                        if len(matches) > 1:
                            # Keep the first one, remove subsequent ones if they are identical or similar
                            # Actually, let's just remove any subsequent occurrence of the header and its following lines
                            
                            # Strategy: Find the first index of the header.
                            first_idx = content.find(header)
                            # Find the second index
                            second_idx = content.find(header, first_idx + 1)
                            
                            if second_idx != -1:
                                # Check if it's a true duplicate (close proximity)
                                # If they are far apart, maybe it's intentional? Unlikely for this specific block.
                                
                                # We will remove the second block.
                                # Identify the end of the second block (empty line or next header)
                                end_idx = content.find(r"\n\n", second_idx)
                                if end_idx == -1:
                                    end_idx = len(content)
                                
                                # Remove from second_idx to end_idx
                                # Also remove preceding newlines if they are excessive
                                
                                print(f"   ✂️ Removing duplicate at index {second_idx}")
                                
                                # Construct new content
                                # We need to be careful. Let's just replace the second occurrence with empty string?
                                # But we need to capture the full block.
                                
                                # Let's use a safer regex replacement that replaces repeated blocks with a single one.
                                # Pattern: (Block)\s+(Block) -> \1
                                
                                regex = r"(> \*\*👨‍💻 Geo-Mentorr Code:\*\*.*?(?:\n> .*?)*)(\n\s*)+\1r
                                new_content = re.sub(regex, r"\1", content, flags=re.DOTALL)
                                
                                if new_content != content:
                                    with open(path, 'w', encoding='utf-8') as f:
                                        f.write(new_content)
                                    print("   ✅ Fixed (regex)")
                                    count += 1
                                else:
                                    # Fallback: Manual removal of second occurrence
                                    # Find the block starting at second_idx
                                    # Assume block ends at double newline
                                    block_end = content.find(r"\n\n", second_idx)
                                    if block_end == -1: block_end = len(content)
                                    
                                    to_remove = content[second_idx:block_end].strip()
                                    # Verify it looks like the header
                                    if to_remove.startswith(header):
                                        new_content = content[:second_idx] + content[block_end:].lstrip()
                                        with open(path, 'w', encoding='utf-8') as f:
                                            f.write(new_content)
                                        print("   ✅ Fixed (manual slice)")
                                        count += 1
                                    else:
                                        print("   ⚠️ Could not safely remove duplicate.")

                except Exception as e:
                    print(f"❌ Error processing {file}: {e}")

    print(fr"\nCleaned {count} files.")

if __name__ == "__main__":
    clean_duplicates()
