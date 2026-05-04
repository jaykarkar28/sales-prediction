import streamlit as st
import tempfile

from src.pdf_extractor import extract_pdf_data
from src.feature_engineering import process_features
from src.dataset_builder import build_dataset
from src.train import train_model
from src.predict import load_model, predict


# ==============================
# 🔹 PATHS
# ==============================
PDF_PATH = "data/sales.pdf"
IMAGE_FOLDER = "data/images"


# ==============================
# 🔹 LOAD OR TRAIN MODEL
# ==============================
@st.cache_resource
def get_model():
    try:
        # Try loading saved model
        model = load_model()
        return model
    except:
        print("Model not found. Training new model...")

        # Train if model doesn't exist
        df = extract_pdf_data(PDF_PATH)
        df_grouped = process_features(df)

        X, y = build_dataset(df_grouped, IMAGE_FOLDER)

        model = train_model(X, y)
        return model


model = get_model()

# STREAMLIT UI
st.set_page_config(page_title="Sales Predictor", layout="centered")

st.title(" Product Sales Prediction System")
st.write("Upload a product design image and predict its sales quantity.")

uploaded_file = st.file_uploader("Upload Product Image", type=["jpg", "png", "jpeg"])

price = st.number_input("Enter Product Price (₹)", min_value=100, max_value=5000, value=999)


if uploaded_file is not None:
    # Save uploaded image temporarily
    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.read())
        temp_path = tmp.name

    st.image(temp_path, caption="Uploaded Product", use_column_width=True)

    if st.button("Predict Sales"):
        try:
            prediction = predict(temp_path, price, model)

            st.success(f" Estimated Sales Quantity: {int(prediction)} units")

            if prediction > 20:
                st.info(" High demand product")
            elif prediction > 8:
                st.info(" Moderate demand")
            else:
                st.info(" Low demand")

        except Exception as e:
            st.error(f"Error: {str(e)}")


# SAMPLE OUTPUTS
st.markdown("---")
st.subheader(" Sample Outputs")

st.write("""
- ₹350 → ~15-20 units (High demand)  
- ₹900 → ~8-12 units (Moderate demand)  
- ₹1500 → ~3-5 units (Low demand)  
""")