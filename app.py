# app.py
import streamlit as st
from dashboard.utils import Utils
from dashboard.kpi_section import KPISection
from dashboard.charts import Charts
from dashboard.data_loader import load_data

st.set_page_config(page_title="Sales Dashboard", layout="wide")
st.title("📈 Sales Analytics Dashboard")

df = load_data("dashboard/data/sales.csv")

# Filter data
utils = Utils()
filtered_df = utils.filter_data(df)

# KPIs
kpi = KPISection(filtered_df)
kpi.render()

# Charts
charts = Charts(filtered_df)
charts.revenue_over_time()
charts.revenue_by_category()
