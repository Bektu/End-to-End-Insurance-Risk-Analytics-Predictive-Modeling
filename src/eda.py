import pandas as pd

def compute_loss_ratio(df):
    """
    Calculate overall portfolio loss ratio.
    Loss Ratio = Total Claims / Total Premium
    """
    return df['totalclaims'].astype(float).sum() / df['totalpremium'].astype(float).sum()


def group_loss_ratio(df, groupby_col):
    """
    Group by a column and calculate the loss ratio per group.
    Returns sorted DataFrame by loss ratio descending.
    """
    grouped = df.groupby(groupby_col)[['totalclaims', 'totalpremium']].sum()
    grouped['lossratio'] = grouped['totalclaims'] / grouped['totalpremium'].replace(0, pd.NA)
    return grouped.sort_values('lossratio', ascending=False)


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
