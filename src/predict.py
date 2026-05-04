import joblib
import numpy as np
from src.image_model import extract_image_features

def load_model(path="models/model.pkl"):
    return joblib.load(path)

def predict(image_path, price, model):
    img_feat = extract_image_features(image_path)

    numeric_feat = [price, 6, 3]  # avg assumptions

    final_feat = np.concatenate([img_feat, numeric_feat])

    prediction = model.predict([final_feat])
    return prediction[0]