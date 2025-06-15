import pandas as pd

def compute_loss_ratio(df):
    return df['TotalClaims'].sum() / df['TotalPremium'].sum()

def group_loss_ratio(df, groupby_col):
    grouped = df.groupby(groupby_col)[['TotalClaims', 'TotalPremium']].sum()
    grouped['LossRatio'] = grouped['TotalClaims'] / grouped['TotalPremium']
    return grouped.sort_values('LossRatio', ascending=False)

def get_summary_stats(df, columns):
    return df[columns].describe()

def check_missing(df):
    return df.isnull().sum().sort_values(ascending=False)
