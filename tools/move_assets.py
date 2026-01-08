import os
import shutil

src_base = r"assets/images"
dst_base = r"web/public/assets/images"

if os.path.exists(src_base):
    os.makedirs(dst_base, exist_ok=True)
    for item in os.listdir(src_base):
        s = os.path.join(src_base, item)
        d = os.path.join(dst_base, item)
        if os.path.isdir(s):
            if os.path.exists(d):
                shutil.rmtree(d)
            shutil.move(s, d)
            print(f"Moved directory {item}")
        elif os.path.isfile(s):
            shutil.copy2(s, d)
            print(f"Copied file {item}")
else:
    print("Source assets/images not found")
