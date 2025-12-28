import os

files_to_check = {
    "municipal_competition_2022_2022_mun_y2_19b": "docs/grade_10/geometry/municipal_competition_2022_2022_mun_y2_19b.md",
    "municipal_competition_2022_2022_mun_y3_17b": "docs/grade_11/geometry/municipal_competition_2022_2022_mun_y3_17b.md",
    "municipal_competition_2025_2025_mun_y3_4a": "docs/grade_11/stereometry/municipal_competition_2025_2025_mun_y3_4a.md",
    "municipal_competition_2022_2022_mun_g6_3": "docs/grade_6/geometry/municipal_competition_2022_2022_mun_g6_3.md",
    "numerus_4367": "docs/grade_6/geometry/numerus_4367.md",
    "numerus_4367_4367": "docs/pre_olympiad/grade_6/geometry/numerus_4367_4367.md",
    "numerus_4412_4412": "docs/grade_7/geometry/numerus_4412_4412.md",
    "numerus_4416_4416": "docs/grade_7/geometry/numerus_4416_4416.md",
    "numerus_4420_4420": "docs/grade_7/geometry/numerus_4420_4420.md",
    "regional_competition_2022_geo_01": "docs/grade_7/geometry/regional_competition_2022_geo_01.md",
    "classic_theorem_centroid_proof": "docs/grade_8/geometry/classic_theorem_centroid_proof.md",
    "municipal_competition_2022_2022_mun_g8_12": "docs/grade_8/geometry/municipal_competition_2022_2022_mun_g8_12.md",
    "numerus_4287_4287": "docs/grade_8/geometry/numerus_4287_4287.md",
    "numerus_4331_4331": "docs/grade_8/geometry/numerus_4331_4331.md",
    "numerus_4419_4419": "docs/grade_8/geometry/numerus_4419_4419.md",
    "numerus_4421_4421": "docs/grade_8/geometry/numerus_4421_4421.md",
    "numerus_l1_2025_L1_2025_07": "docs/grade_8/geometry/numerus_l1_2025_L1_2025_07.md",
    "numerus_l2_2024_2025_L2_2025_01": "docs/grade_8/geometry/numerus_l2_2024_2025_L2_2025_01.md",
    "sigma_137_138_sigma_adv_04": "docs/grade_8/geometry/sigma_137_138_sigma_adv_04.md"
}

assets_dir = os.path.abspath("docs/assets/images")
image_extensions = [".png", ".jpg", ".jpeg", ".svg", ".gif"]

for name, path in files_to_check.items():
    abs_path = os.path.abspath(path)
    if not os.path.exists(abs_path):
        print(f"File not found: {path}")
        continue
        
    with open(abs_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    has_image_tag = "![" in content
    
    # Check if image exists in assets
    found_image = None
    for ext in image_extensions:
        image_name = name + ext
        image_path = os.path.join(assets_dir, image_name)
        if os.path.exists(image_path):
            found_image = image_name
            break
            
    status = []
    if has_image_tag:
        status.append("Has Tag")
    else:
        status.append("MISSING Tag")
        
    if found_image:
        status.append(f"Found Image: {found_image}")
    else:
        status.append("MISSING Image File")
        
    print(f"{name}: {', '.join(status)}")
