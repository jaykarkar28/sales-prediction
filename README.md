# Name : Jay Karkar
# Mobile No. : 9726907617



# Sales Prediction System

This project is a Machine Learning web application that predicts product sales demand based on its visual design and price. It extracts historical sales data from a PDF, processes product images using AI, and uses a Random Forest model to forecast future sales.

## Project Implementation
1. **Data Extraction**: Extracts historical sales logs (price, quantity sold) from `data/sales.pdf`.
2. **Computer Vision**: Uses a pre-trained PyTorch ResNet18 model to extract visual patterns from product images.
3. **Training**: Combines the image data and pricing data to train a Random Forest Regressor.
4. **Web App**: A Streamlit interface allows users to upload a new product image, enter a price, and get an instant sales prediction.

--------

## Dependencies
To install the required libraries, run:
```bash
pip install -r requirements.txt
```

The core libraries used are:
- `pandas`
- `numpy`
- `scikit-learn`
- `torch` & `torchvision` (PyTorch)
- `pdfplumber`
- `streamlit`

---

## How to Run the Project

### Step 1: Open the Terminal
Open your terminal or command prompt and navigate to the project directory:
```bash
cd "c:\00_Main_ALL_CODE\Company Project"
```

### Step 2: Activate the Virtual Environment
Activate the environment where all the dependencies are installed:
```bash
myenv\Scripts\activate
```

### Step 3: Run the Streamlit App
Start the web application by running:
```bash
streamlit run main.py
```

### Step 4: Use the App
- A browser window will automatically open.
- **Upload** a product image.
- **Enter** your proposed selling price.
- Click **Predict Sales** to see the estimated demand!

*Note: The first time you run the app, it will automatically train and save the model.*
