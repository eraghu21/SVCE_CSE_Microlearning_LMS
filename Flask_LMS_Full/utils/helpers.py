
import pandas as pd

def read_excel(path):
    df = pd.read_excel(path)
    if 'RegNo' not in df.columns:
        raise ValueError("Excel must contain 'RegNo' column.")
    return df
