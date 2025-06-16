import pandas as pd

def load_data(filepath: str, sep: str = "|", encoding: str = "utf-8") -> pd.DataFrame:
    """Load insurance dataset with pipe delimiter and handle encoding issues."""
    try:
        return pd.read_csv(
            filepath,
            sep=sep,
            encoding=encoding,
            engine="python",           # fallback to Python engine
            on_bad_lines="skip",       # skip malformed rows
            dtype=str                  # force all as strings to avoid mixed types
        )
    except Exception as e:
        print(f"❌ Failed to load file: {filepath}\nReason: {e}")
        return pd.DataFrame()
def parse_dates(df: pd.DataFrame, date_column: str = "transactionmonth") -> pd.DataFrame:
    """Parse transaction date column to datetime format."""
    if date_column in df.columns:
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
    else:
        print(f"⚠️ Warning: '{date_column}' column not found.")
    return df
