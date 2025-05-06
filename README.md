# Wigan-Council-Spending-Dashboard
Interactive Streamlit dashboard for analyzing Wigan Council’s spending over £500 by category, supplier, and month
# 💸 Wigan Council Spending Dashboard

This is a Streamlit-powered interactive dashboard built to explore and visualize payment transactions over £500 made by Wigan Council. It allows users to filter and analyze spending trends, top suppliers, and spending categories over time.

## 📂 Dataset

- **Title:** Wigan Council Spending Over £500
- **Source:** [wigan.gov.uk](https://www.wigan.gov.uk)
- **Format:** CSV
- **Description:** Lists payments over £500, including date, amount, supplier name, and merchant category.

## 🚀 Features

- Filter by **Month** and **Merchant Category**
- View **Total Spend**, **Suppliers Count**, and **Transaction Count**
- Visualize:
  - 🏆 Top 10 Merchant Categories by Spend
  - 📈 Monthly Spending Trends
  - 📊 Top 10 Suppliers by Spend
- Expandable section for **raw filtered data**

## 🛠️ Tech Stack

- Python
- Streamlit
- Plotly
- Pandas

## 📸 Screenshots

![Dashboard Overview](./screenshots/dashboard_summary.png)
![Monthly Spend](./screenshots/monthly_trend.png)
![Top Suppliers](./screenshots/top_suppliers.png)

## 🔧 Installation

```bash
pip install streamlit pandas plotly
streamlit run app.py
