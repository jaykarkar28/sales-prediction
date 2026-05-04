import pandas as pd

def process_features(df):
    df["date"] = pd.to_datetime(df["date"])

    df["month"] = df["date"].dt.month
    df["day"] = df["date"].dt.day
    df["weekday"] = df["date"].dt.weekday

    grouped = df.groupby("code").agg({
        "qty": "sum",
        "rate": "mean",
        "month": "mean",
        "weekday": "mean"
    }).reset_index()

    return grouped