import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_histogram(df, column, bins=50):
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column].dropna(), bins=bins)
    plt.title(f"Distribution of {column}")
    plt.savefig(f"reports/figs/hist_{column}.png")
    plt.close()

def plot_boxplot(df, column):
    plt.figure(figsize=(10, 6))
    sns.boxplot(y=df[column])
    plt.title(f"Boxplot of {column}")
    plt.savefig(f"reports/figs/box_{column}.png")
    plt.close()

def plot_loss_ratio_by_category(loss_ratio_df, category):
    loss_ratio_df.reset_index(inplace=True)
    sns.barplot(data=loss_ratio_df, x=category, y='lossratio')
    plt.title(f"Loss Ratio by {category}")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(f"reports/figs/loss_ratio_by_{category}.png")
    plt.close()
