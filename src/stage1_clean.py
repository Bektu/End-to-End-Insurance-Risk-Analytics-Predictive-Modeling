import pandas as pd
from src.data_loader import load_data, parse_dates

def main():
    df = load_data("data/raw/MachineLearningRating_v3.txt", sep="|")
    df.columns = df.columns.str.strip().str.replace(" ", "").str.lower()
    df = parse_dates(df)

    output_path = "data/processed/cleaned.csv"
    df.to_csv(output_path, index=False)
    print(f"✅ Cleaned data saved to {output_path}")

if __name__ == "__main__":
    main()
