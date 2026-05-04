import os
import numpy as np
from src.image_model import extract_image_features

def build_dataset(df_grouped, image_folder):
    features = []
    targets = []

    available_images = [f for f in os.listdir(image_folder) if f.endswith(('.jpg', '.jpeg', '.png'))]
    fallback_img_idx = 0

    for _, row in df_grouped.iterrows():
        code = str(row["code"])
        img_path = os.path.join(image_folder, f"{code}.jpg")

        if not os.path.exists(img_path) and available_images:
            img_path = os.path.join(image_folder, available_images[fallback_img_idx % len(available_images)])
            fallback_img_idx += 1

        if os.path.exists(img_path):
            img_feat = extract_image_features(img_path)

            numeric_feat = [
                row["rate"],
                row["month"],
                row["weekday"]
            ]

            final_feat = np.concatenate([img_feat, numeric_feat])

            features.append(final_feat)
            targets.append(row["qty"])

    return np.array(features), np.array(targets)