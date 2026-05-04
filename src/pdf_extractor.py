import pdfplumber
import pandas as pd

def extract_pdf_data(pdf_path):
    data = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            lines = text.split("\n")

            for line in lines:
                parts = line.split()
                if len(parts) >= 5:
                    try:
                        date = parts[0]
                        code = parts[2]
                        qty = int(parts[3])
                        rate = float(parts[4])

                        data.append([date, code, qty, rate])
                    except:
                        continue

    df = pd.DataFrame(data, columns=["date", "code", "qty", "rate"])
    return df