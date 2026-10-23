"""
Task 04: Business Insights Report (EDA)
Author: SkillCraft Technology Intern
Description: Analyzes marketing campaign data, visualizes customer funnels,
calculates ROI per channel, and generates actionable business recommendations.
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")

def generate_synthetic_marketing_data(num_rows=5000) -> pd.DataFrame:
    """Generates a sample marketing dataset if none is provided."""
    np.random.seed(42)
    channels = ['Google Ads', 'Facebook Ads', 'Email Marketing', 'Affiliates', 'Organic Search']
    
    data = {
        'Campaign_ID': [f"CMP_{i:04d}" for i in range(num_rows)],
        'Channel': np.random.choice(channels, num_rows, p=[0.3, 0.3, 0.15, 0.15, 0.1]),
        'Budget': np.random.uniform(500, 5000, num_rows),
    }
    df = pd.DataFrame(data)
    
    multiplier = {'Google Ads': 1.2, 'Facebook Ads': 1.0, 'Email Marketing': 1.8, 'Affiliates': 0.9, 'Organic Search': 2.5}
    df['Impressions'] = df['Budget'] * df['Channel'].map(lambda x: np.random.uniform(10, 20) * multiplier[x])
    df['Clicks'] = df['Impressions'] * np.random.uniform(0.03, 0.08, num_rows)
    df['Conversions'] = df['Clicks'] * np.random.uniform(0.05, 0.15, num_rows)
    df['Revenue'] = df['Conversions'] * np.random.uniform(40, 120, num_rows)
    
    return df

def perform_eda(df: pd.DataFrame):
    """Calculates ROI, channel performance, and summarizes findings."""
    print("=================== EDA SUMMARY REPORT ===================")
    
    # Calculate ROI = (Revenue - Budget) / Budget
    df['ROI'] = (df['Revenue'] - df['Budget']) / df['Budget']
    df['CTR'] = df['Clicks'] / df['Impressions']
    df['Conversion_Rate'] = df['Conversions'] / df['Clicks']
    
    channel_summary = df.groupby('Channel')[['Budget', 'Revenue', 'Conversions', 'ROI', 'Conversion_Rate']].mean().reset_index()
    print("\n--- Average Performance by Marketing Channel ---")
    print(channel_summary.to_string(index=False))
    
    return df, channel_summary

def plot_marketing_funnel(df: pd.DataFrame, output_dir: str):
    """Visualizes channel ROI and saves chart."""
    os.makedirs(output_dir, exist_ok=True)
    
    plt.figure(figsize=(10, 6))
    channel_roi = df.groupby('Channel')['ROI'].mean().sort_values(ascending=False)
    
    ax = sns.barplot(x=channel_roi.index, y=channel_roi.values, palette="viridis")
    plt.title("Average Return on Investment (ROI) by Marketing Channel", fontsize=14, fontweight='bold')
    plt.xlabel("Marketing Channel", fontsize=12)
    plt.ylabel("Mean ROI", fontsize=12)
    plt.xticks(rotation=15)
    
    for p in ax.patches:
        ax.annotate(f"{p.get_height():.2f}x", 
                    (p.get_x() + p.get_width() / 2., p.get_height()), 
                    ha='center', va='bottom', fontsize=10, color='black', xytext=(0, 3), 
                    textcoords='offset points')
                    
    plt.tight_layout()
    chart_path = os.path.join(output_dir, "channel_roi_analysis.png")
    plt.savefig(chart_path, dpi=300)
    plt.close()
    print(f"\n[*] Funnel visualization saved to: {chart_path}")

def main():
    print("[*] Initializing Task 04: Business Insights Report (EDA)...")
    
    df = generate_synthetic_marketing_data()
    df, channel_summary = perform_eda(df)
    plot_marketing_funnel(df, output_dir="reports")
    
    print("\n=================== RECOMMENDATIONS ===================")
    best_channel = channel_summary.loc[channel_summary['ROI'].idxmax()]['Channel']
    print(f"1. Budget Reallocation: Shift additional budget toward {best_channel} due to high ROI efficiency.")
    print("2. Conversion Optimization: Address mid-funnel drop-offs by optimizing landing pages for lower performing channels.")

if __name__ == "__main__":
    main()