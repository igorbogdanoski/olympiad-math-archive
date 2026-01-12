import os

def check_theorem_proofs():
    theorems_dir = '../web/src/data/theorems'
    theorems = []

    for file in sorted(os.listdir(theorems_dir)):
        if file.endswith('.md') and not file.startswith('_'):
            path = os.path.join(theorems_dir, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Read frontmatter for title
            lines = content.split('\n')
            title = file[:-3]  # default to filename
            for line in lines:
                if line.startswith('title:'):
                    title = line.split(':', 1)[1].strip().strip('"\'')
                    break

            has_proof = '## 📝 Доказ' in content
            status = 'HAS_PROOF' if has_proof else 'NO_PROOF'

            theorems.append({
                'filename': file[:-3],
                'title': title,
                'has_proof': has_proof,
                'status': status
            })

    return theorems

def main():
    theorems = check_theorem_proofs()

    print("LIST OF THEOREMS AND PROOF STATUS")
    print("=" * 50)

    for th in theorems:
        print(f"{th['status']}: {th['title']} ({th['filename']})")

    print("\nTHEOREMS MISSING PROOFS:")
    print("-" * 30)
    no_proof = [th for th in theorems if not th['has_proof']]
    for th in no_proof:
        print(f"- {th['title']} ({th['filename']})")

    proof_percentage = (len(theorems) - len(no_proof)) / len(theorems) * 100
    print(".2f")
    print(f"Total theorems: {len(theorems)}")

if __name__ == "__main__":
    main()