import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os

# Ensure the output directory exists
PLOT_DIR = "reports/figs"
os.makedirs(PLOT_DIR, exist_ok=True)

def plot_histogram(df, column, bins=50):
    """Plot histogram of a numeric column."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column].dropna().astype(float), bins=bins, kde=True, color='skyblue')
    plt.title(f"Distribution of {column}")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"{PLOT_DIR}/hist_{column}.png")
    plt.close()


def plot_boxplot(df, column):
    """Plot boxplot of a numeric column."""
    plt.figure(figsize=(8, 6))
    sns.boxplot(y=df[column].dropna().astype(float), color='lightcoral')
    plt.title(f"Boxplot of {column}")
    plt.ylabel(column)
    plt.tight_layout()
    plt.savefig(f"{PLOT_DIR}/box_{column}.png")
    plt.close()


def plot_loss_ratio_by_category(loss_ratio_df, category):
    """
    Plot bar chart of loss ratio by a categorical feature.
    Input DataFrame must include:
        - index: category
        - column: 'lossratio'
    """
    loss_ratio_df = loss_ratio_df.reset_index()
    
    plt.figure(figsize=(12, 6))
    sns.barplot(data=loss_ratio_df, x=category, y='LossRatio', palette='viridis')
    plt.title(f"Loss Ratio by {category}")
    plt.xlabel(category)
    plt.ylabel("Loss Ratio")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f"{PLOT_DIR}/Loss_Ratio_by_{category}.png")
    plt.close()
