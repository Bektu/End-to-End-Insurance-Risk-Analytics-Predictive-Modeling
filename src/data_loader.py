import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Load the raw insurance dataset"""
    return pd.read_csv(filepath)

def parse_dates(df: pd.DataFrame, date_column: str = "TransactionMonth") -> pd.DataFrame:
    """Convert TransactionMonth to datetime format"""
    df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    return df