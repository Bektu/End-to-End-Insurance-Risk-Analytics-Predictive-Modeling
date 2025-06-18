import pandas as pd

def compute_loss_ratio(df):
    if 'TotalClaims' not in df.columns or 'TotalPremium' not in df.columns:
        raise KeyError("Expected columns 'TotalClaims' and 'TotalPremium' not found in DataFrame.")
    return df['TotalClaims'].astype(float).sum() / df['TotalPremium'].astype(float).sum()

def group_loss_ratio(df, groupby_col):
    grouped = df.groupby(groupby_col)[['TotalClaims', 'TotalPremium']].sum()
    grouped['LossRatio'] = grouped['TotalClaims'] / grouped['TotalPremium'].replace(0, pd.NA)
    return grouped.sort_values('LossRatio', ascending=False)

def get_summary_stats(df, columns):
    """
    Get descriptive statistics for selected numeric columns.
    """
    valid_columns = [col for col in columns if col in df.columns]
    if not valid_columns:
        raise KeyError(f"None of the provided columns exist: {columns}")
    return df[valid_columns].astype(float).describe()


def check_missing(df):
    """
    Return missing value count per column, sorted descending.
    """
    return df.isnull().sum().sort_values(ascending=False)
