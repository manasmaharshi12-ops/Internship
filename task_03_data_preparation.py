"""
Task 03: Interactive Visualization - Data Preparation Pipeline
Author: SkillCraft Technology Intern
Description: Cleans, transforms, and structures raw datasets 
(e.g., HR Employee Attrition / Global Happiness Index) for Power BI/Tableau dashboards.
"""

import os
import pandas as pd
import numpy as np

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    """Loads raw data, handles missing values, and formats columns."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at: {file_path}")
        
    df = pd.read_csv(file_path)
    print(f"[*] Successfully loaded raw data. Shape: {df.shape}")
    
    # 1. Handle Missing Values
    for col in df.select_dtypes(include=[np.number]).columns:
        df[col] = df[col].fillna(df[col].median())
        
    for col in df.select_dtypes(include=[object]).columns:
        df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown")
        
    # 2. Feature Engineering
    if 'Age' in df.columns:
        df['Age_Group'] = pd.cut(
            df['Age'], 
            bins=[18, 25, 35, 45, 55, 100], 
            labels=['18-25', '26-35', '36-45', '46-55', '56+']
        )
        
    if 'TotalWorkingYears' in df.columns:
        df['Experience_Level'] = pd.cut(
            df['TotalWorkingYears'],
            bins=[-1, 2, 5, 10, 20, 100],
            labels=['Entry', 'Junior', 'Mid', 'Senior', 'Veteran']
        )

    print("[*] Data cleaning and feature engineering complete.")
    return df

def main():
    raw_path = "data/raw/HR_Employee_Attrition.csv"
    output_path = "data/processed/cleaned_dashboard_data.csv"
    
    os.makedirs("data/processed", exist_ok=True)
    
    try:
        df_cleaned = load_and_clean_data(raw_path)
        df_cleaned.to_csv(output_path, index=False)
        print(f"[*] Processed data successfully exported to: {output_path}")
    except FileNotFoundError:
        print(f"[!] Place your dataset inside '{raw_path}' or update the path in the script.")

if __name__ == "__main__":
    main()