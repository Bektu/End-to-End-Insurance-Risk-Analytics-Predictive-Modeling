# src/modeling/data_prep.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


def prepare_features(df, target_column, dropna_target=True):
    if dropna_target:
        df = df[df[target_column].notna()]
    
    y = df[target_column].astype(float)
    
    X = df.drop(columns=[target_column, "TotalPremium", "TotalClaims", "Margin", "HasClaim"], errors='ignore')
    X = X.select_dtypes(include=["number", "object"])  # drop datetime

    cat_cols = X.select_dtypes(include=["object"]).columns.tolist()
    num_cols = X.select_dtypes(include=["number"]).columns.tolist()

    # Pipeline
    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="mean"))
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(transformers=[
        ("num", numeric_transformer, num_cols),
        ("cat", categorical_transformer, cat_cols)
    ])

    return X, y, preprocessor
