from pathlib import Path
import pandas as pd

def load_reviews(file_path):
    file_path = Path(file_path)
    if not file_path.exists():
        raise FileNotFoundError(f"Data file not found: {file_path}")
    return pd.read_csv(file_path)

def select_review_columns(df):
    return df[["review_text", "sentiment"]].copy()