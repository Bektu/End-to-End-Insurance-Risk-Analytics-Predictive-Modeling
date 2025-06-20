# src/analysis/hypothesis_testing.py

import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency
import numpy as np


def preprocess_for_testing(df):
    df["TotalPremium"] = df["TotalPremium"].astype(float)
    df["TotalClaims"] = df["TotalClaims"].astype(float)
    df["HasClaim"] = df["TotalClaims"] > 0
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]
    return df


def claim_frequency_test(df, group_col):
    """
    Chi-squared test for claim frequency across categories (e.g. Gender, Province)
    """
    contingency = pd.crosstab(df[group_col], df["HasClaim"])
    chi2, p, _, _ = chi2_contingency(contingency)
    return chi2, p


def claim_severity_ttest(df, group_col, group1, group2):
    """
    T-test for claim severity among claimants between two groups (e.g., Male vs Female)
    """
    df_claims = df[df["HasClaim"]]
    g1 = df_claims[df_claims[group_col] == group1]["TotalClaims"]
    g2 = df_claims[df_claims[group_col] == group2]["TotalClaims"]
    return ttest_ind(g1, g2, equal_var=False)


def margin_anova(df, group_col):
    """
    ANOVA test for margin differences across multiple categories
    """
    from scipy.stats import f_oneway

    groups = [group["Margin"].values for _, group in df.groupby(group_col)]
    return f_oneway(*groups)
