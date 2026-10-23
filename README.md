#  Internship Projects

This repository contains projects completed during my SkillCraft Technology internship.

## Task 1: Automated Sales Dashboard
- **Tool:** Microsoft Excel
- **File:** `SkillCraft_Task1_Automated_Sales_Dashboard.xlsx`
- **Objective:** Organize and analyze sales data through an Excel dashboard.

## Task 2: Data Cleaning
- **Tool:** Python, Pandas, Google Colab
- **File:** `SkillCraft_Task2_Data_Cleaning.ipynb`
- **Objective:** Clean and prepare data for further analysis.

## Skills Demonstrated
- Microsoft Excel
- Python
- Pandas
- Data analysis and visualization

- # Task 03 — Interactive HR Attrition Dashboard

An interactive data visualization project to explore employee attrition patterns across departments, age groups, regions, overtime status, and job satisfaction.

## Overview

This project helps explore employee attrition and identify workforce patterns that may deserve further investigation.

## Features

- Employee count, leavers, attrition rate, and average tenure KPIs
- Filters for department, age group, region, and job role
- Attrition comparisons by department and age group
- Overtime and job satisfaction analysis
- Interactive employee records table
- Standalone HTML preview

## Tech Stack

- Python
- Pandas
- Streamlit
- Plotly
- CSV
- HTML, CSS, and JavaScript

## Project Structure

```text
hr-attrition-dashboard/
├── app.py
├── hr_employee_attrition.csv
├── requirements.txt
├── preview.html
├── REQUIREMENTS.md
└── README.md
```

## Installation and Usage

**1. Install dependencies**

```bash
pip install -r requirements.txt
```

**2. Run the dashboard**

```bash
streamlit run app.py
```

**3. Open the local URL** displayed in your terminal.

## Key Metric

**Attrition Rate** = (Employees Leaving / Total Employees) × 100

## Publish the HTML Preview

1. Rename or copy `preview.html` to `index.html`.
2. Open your GitHub repository's **Settings → Pages**.
3. Select **Deploy from a branch**.
4. Select the `main` branch and root folder, then save.

GitHub Pages publishes the static HTML preview. The Python dashboard runs separately through Streamlit.

## Dataset

The sample dataset includes employee IDs, age, department, region, job role, years at company, monthly income, overtime, job satisfaction, and attrition status.

## Limitations

The included dataset is synthetic demonstration data. Replace it with authorized, real data before drawing business conclusions. The sample is small and should not be used to establish statistically reliable or causal relationships.

## Future Improvements

- Add time-based attrition trends
- Analyze employee exit reasons
- Add compensation and promotion history
- Deploy the Streamlit dashboard online

---

**Project:** 
Task 03 — Interactive HR Attrition Dashboard

An interactive data visualization project to explore employee attrition patterns across departments, age groups, regions, overtime status, and job satisfaction.

Overview

This project helps explore employee attrition and identify workforce patterns that may deserve further investigation.

Features

Employee count, leavers, attrition rate, and average tenure KPIs

Filters for department, age group, region, and job role

Attrition comparisons by department and age group

Overtime and job satisfaction analysis

Interactive employee records table

Standalone HTML preview

Tech Stack

Python

Pandas

Streamlit

Plotly

CSV

HTML, CSS, and JavaScript

Project Structure

hr-attrition-dashboard/
├── app.py
├── hr_employee_attrition.csv
├── requirements.txt
├── preview.html
├── REQUIREMENTS.md
└── README.md

Installation and Usage

1. Install dependencies

pip install -r requirements.txt

2. Run the dashboard

streamlit run app.py

3. Open the local URL displayed in your terminal.

Key Metric

Attrition Rate = (Employees Leaving / Total Employees) × 100

Publish the HTML Preview

Rename or copy preview.html to index.html.

Open your GitHub repository's Settings → Pages.

Select Deploy from a branch.

Select the main branch and root folder, then save.

GitHub Pages publishes the static HTML preview. The Python dashboard runs separately through Streamlit.

Dataset

The sample dataset includes employee IDs, age, department, region, job role, years at company, monthly income, overtime, job satisfaction, and attrition status.

Limitations

The included dataset is synthetic demonstration data. Replace it with authorized, real data before drawing business conclusions. The sample is small and should not be used to establish statistically reliable or causal relationships.

Future Improvements

Add time-based attrition trends

Analyze employee exit reasons

Add compensation and promotion history

Deploy the Streamlit dashboard online

Project: Task 03 — Interactive Visualization

Task 04 — Marketing Campaign Exploratory Data Analysis

A marketing analytics project exploring campaign performance, conversion funnels, spending efficiency, and return on ad spend (ROAS).

Overview

This project compares marketing campaigns and channels to help identify performance patterns and potential opportunities for optimization.

Features

KPI cards for total spend, attributed revenue, ROAS, and conversions

Interactive channel and spending filters

Campaign spend-versus-revenue comparison

ROAS comparisons across campaigns

Marketing funnel: impressions, clicks, leads, and conversions

Channel efficiency analysis

Campaign performance table

Written EDA findings and recommendations

Standalone HTML preview

Tech Stack

Python

Pandas

Streamlit

Plotly

CSV

Markdown

HTML, CSS, and JavaScript

Project Structure

marketing-campaign-eda/
├── app.py
├── marketing_campaigns.csv
├── requirements.txt
├── eda_report.md
├── preview.html
├── REQUIREMENTS.md
└── README.md

Installation and Usage

1. Install dependencies

pip install -r requirements.txt

2. Run the dashboard

streamlit run app.py

3. Open the local URL displayed in your terminal.

Key Performance Metrics

CTR: Clicks / Impressions

Lead Rate: Leads / Clicks

Conversion Rate: Conversions / Clicks

Cost per Lead: Spend / Leads

Cost per Conversion: Spend / Conversions

ROAS: Attributed Revenue / Spend

Publish the HTML Preview

Rename or copy preview.html to index.html.

Open your GitHub repository's Settings → Pages.

Select Deploy from a branch.

Select the main branch and root folder, then save.

GitHub Pages hosts the static HTML preview; the Python dashboard runs separately through Streamlit.

Dataset

The sample dataset contains campaign name, channel, spend, impressions, clicks, leads, conversions, and attributed revenue.

Business Questions

Which campaigns generate the highest attributed revenue relative to spending?

Where does the marketing funnel narrow?

Which channels could merit controlled budget tests?

Which campaigns need further investigation or optimization?

Limitations

The included dataset is synthetic demonstration data. ROAS is not profit and does not prove that marketing caused the attributed revenue. Consider margins, attribution windows, customer lifetime value, seasonality, and incrementality before making budget decisions.

Future Improvements

Add date-based campaign trends

Integrate advertising platform data

Include profit margins and customer lifetime value

Evaluate budget recommendations using controlled experiments

Deploy the dashboard online

Project: Task 04 — Business Insights Report (EDA)


