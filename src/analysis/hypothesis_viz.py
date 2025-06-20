# src/visualizations/hypothesis_viz.py

import seaborn as sns
import matplotlib.pyplot as plt
import os

def plot_claim_frequency(df, group_col, save_path=None):
    freq = df.groupby(group_col)["HasClaim"].mean().reset_index()
    plt.figure(figsize=(8,5))
    sns.barplot(x=group_col, y="HasClaim", data=freq)
    plt.title(f"📊 Claim Frequency by {group_col}")
    plt.xticks(rotation=45)
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_claim_severity(df, group_col, save_path=None):
    df_claims = df[df["HasClaim"]]
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=group_col, y="TotalClaims", data=df_claims)
    plt.title(f"💰 Claim Severity by {group_col}")
    plt.xticks(rotation=45)
    if save_path:
        plt.savefig(save_path)
    plt.show()

def plot_margin_distribution(df, group_col, save_path=None):
    plt.figure(figsize=(10, 5))
    sns.violinplot(x=group_col, y="Margin", data=df)
    plt.title(f"📈 Margin Distribution by {group_col}")
    plt.xticks(rotation=45)
    if save_path:
        plt.savefig(save_path)
    plt.show()
