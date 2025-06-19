import pandas as pd

def load_data(filepath: str, sep: str = "|") -> pd.DataFrame:
    df = pd.read_csv(filepath, sep=sep)
    
    # Convert key numeric fields
    numeric_fields = ['TotalClaims', 'TotalPremium', 'CustomValueEstimate']
    for col in numeric_fields:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df
def parse_dates(df: pd.DataFrame, date_column: str = "transactionmonth") -> pd.DataFrame:
    """Parse transaction date column to datetime format."""
    if date_column in df.columns:
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    else:
        print(f"⚠️ Warning: '{date_column}' column not found.")
    return df
