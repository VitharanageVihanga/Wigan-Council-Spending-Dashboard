import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("cleaned wigan spending.csv")

# Streamlit page config
st.set_page_config(page_title="Wigan Council Dashboard", layout="wide")
st.title("📊 Wigan Council Spending Dashboard")
st.markdown("Analyze spending trends, top suppliers, and merchant categories over time.")

# Sidebar Filters
st.sidebar.header("🔎 Filter Options")
month_options = sorted(df['Month'].unique())
category_options = sorted(df['Category'].dropna().unique())

selected_month = st.sidebar.selectbox("Select Month", month_options)
selected_category = st.sidebar.selectbox("Select Category", ["All"] + category_options)

filtered_df = df[df['Month'] == selected_month]
if selected_category != "All":
    filtered_df = filtered_df[filtered_df['Category'] == selected_category]

# Summary Metrics
st.subheader(f"📌 Summary for {selected_month} ({'All Categories' if selected_category == 'All' else selected_category})")
col1, col2, col3 = st.columns(3)

col1.metric("Total Spend", f"\u00a3{filtered_df['Amount'].sum():,.2f}")
col2.metric("# of Suppliers", filtered_df['Supplier'].nunique())
col3.metric("# of Transactions", filtered_df.shape[0])

st.divider()

# Top Categories Bar Chart
st.subheader("🧾 Top 10 Merchant Categories")
category_sum = df.groupby('Category')['Amount'].sum().sort_values(ascending=False).head(10).reset_index()
fig1 = px.bar(category_sum, x='Amount', y='Category', orientation='h', color='Amount',
              color_continuous_scale='Blues', text_auto=True, title='Top 10 Categories by Spend')
fig1.update_layout(margin=dict(l=40, r=20, t=50, b=40), xaxis_tickformat="\u00a3,.0f")
st.plotly_chart(fig1, use_container_width=True)

# Monthly Spend Trend Line Chart
st.subheader("📈 Monthly Spending Trend")
monthly_trend = df.groupby('Month')['Amount'].sum().reset_index()
fig2 = px.line(monthly_trend, x='Month', y='Amount', markers=True, title="Total Monthly Spend",
               color_discrete_sequence=["#F63366"])
fig2.update_layout(yaxis_tickformat="\u00a3,.0f")
st.plotly_chart(fig2, use_container_width=True)

# Top Suppliers Horizontal Bar
st.subheader("🏢 Top 10 Suppliers")
top_suppliers = df.groupby('Supplier')['Amount'].sum().sort_values(ascending=False).head(10).reset_index()
fig3 = px.bar(top_suppliers, x='Amount', y='Supplier', orientation='h', color='Amount',
              color_continuous_scale='Tealgrn', title='Top 10 Suppliers by Spend', text_auto=True)
fig3.update_layout(margin=dict(l=40, r=20, t=50, b=40), xaxis_tickformat="\u00a3,.0f")
st.plotly_chart(fig3, use_container_width=True)

# Raw Data Table
with st.expander("📄 Show Filtered Raw Data"):
    st.dataframe(filtered_df.reset_index(drop=True))
