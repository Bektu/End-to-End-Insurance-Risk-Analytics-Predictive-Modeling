import pandas as pd
def compute_loss_ratio(df):
    df['TotalClaims'] = df['TotalClaims'].astype(float)
    df['TotalPremium'] = df['TotalPremium'].astype(float)
    return df['TotalClaims'].sum() / df['TotalPremium'].sum()
def group_loss_ratio(df, groupby_col):
    # ✅ Convert BEFORE grouping
    df['TotalClaims'] = pd.to_numeric(df['TotalClaims'], errors='coerce')
    df['TotalPremium'] = pd.to_numeric(df['TotalPremium'], errors='coerce')

    # ✅ Confirm type conversion (for debug)
    print("\n🧪 Types after conversion:")
    print(df[['TotalClaims', 'TotalPremium']].dtypes)

    # ✅ Group
    grouped = df.groupby(groupby_col)[['TotalClaims', 'TotalPremium']].sum()

    # ✅ Confirm grouped dtypes
    print("\n📊 Types in grouped DataFrame:")
    print(grouped.dtypes)

    # ✅ Calculate loss ratio safely
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
