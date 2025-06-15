# End-to-End-Insurance-Risk-Analytics-Predictive-Modeling
 
# 🚗 AlphaCare Insurance Analytics

A modular data science pipeline for analyzing car insurance claims and optimizing pricing strategies using predictive modeling, hypothesis testing, and risk segmentation.

---

## 📌 Project Overview

**AlphaCare Insurance Solutions (ACIS)** aims to develop predictive analytics tools to identify low-risk clients, optimize premiums, and inform targeted marketing strategies. This repository delivers a complete data pipeline from raw data ingestion through model development, using a reproducible and version-controlled workflow.

---

## 🔍 Objectives

- Perform EDA to understand claims risk and profitability.
- Use DVC for reproducible data versioning and pipeline management.
- Conduct statistical hypothesis testing to validate risk segmentation strategies.
- Build ML models to predict:
  - **Claim severity**
  - **Claim probability**
  - **Optimal premium pricing**

---

## 🧱 Project Structure

ACIS_Insurance_Analytics/
│
├── data/
│ ├── raw/ # Raw data files (DVC tracked)
│ └── processed/ # Cleaned / transformed data
│
├── notebooks/
│ └── task1_eda.ipynb # Jupyter notebook for initial EDA
│
├── reports/
│ ├── figs/ # EDA visualizations
│
├── src/ # Modular Python code
│ ├── init.py
│ ├── data_loader.py # Load and preprocess data
│ ├── eda.py # EDA/statistical functions
│ ├── visualizations.py # Plotting functions
│ ├── hypothesis_tests.py # Hypothesis testing logic
│ ├── modeling.py # ML models and evaluation
│ └── utils.py # Outlier detection, helpers
│
├── dvc.yaml # DVC pipeline configuration
├── .gitignore
├── requirements.txt
├── README.md
└── main.py # Optional CLI interface