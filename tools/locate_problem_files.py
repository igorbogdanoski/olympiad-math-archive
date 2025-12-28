import os

target_files = [
    "municipal_competition_2022_2022_mun_y2_19b",
    "municipal_competition_2022_2022_mun_y3_17b",
    "municipal_competition_2025_2025_mun_y3_4a",
    "municipal_competition_2022_2022_mun_g6_3",
    "numerus_4367",
    "numerus_4367_4367",
    "numerus_4412_4412",
    "regional_competition_2022_geo_01",
    "numerus_4420_4420",
    "numerus_4416_4416",
    "classic_theorem_centroid_proof",
    "municipal_competition_2022_2022_mun_g8_12",
    "numerus_4331_4331",
    "numerus_4287_4287",
    "numerus_4419_4419",
    "numerus_l2_2024_2025_L2_2025_01",
    "sigma_137_138_sigma_adv_04",
    "numerus_l1_2025_L1_2025_07",
    "numerus_4421_4421"
]

found_files = {}

for root, dirs, files in os.walk("docs"):
    for file in files:
        name_no_ext = os.path.splitext(file)[0]
        if name_no_ext in target_files:
            found_files[name_no_ext] = os.path.join(root, file)

print("Found files:")
for name, path in found_files.items():
    print(f"{name}: {path}")

print("\nMissing files:")
for name in target_files:
    if name not in found_files:
        print(name)
