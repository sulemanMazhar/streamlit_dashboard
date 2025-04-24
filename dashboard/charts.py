# dashboard/charts.py
import plotly.express as px
import streamlit as st
import pandas as pd

class Charts:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def revenue_over_time(self):
        st.subheader("📅 Revenue Over Time")
        fig = px.line(self.df, x="order_date", y="revenue", title="Revenue Over Time", markers=True)
        st.plotly_chart(fig, use_container_width=True)

    def revenue_by_category(self):
        st.subheader("📦 Revenue by Category")
        category_data = self.df.groupby("category")["revenue"].sum().sort_values(ascending=False).reset_index()
        fig = px.bar(category_data, x="category", y="revenue", title="Revenue by Category")
        st.plotly_chart(fig, use_container_width=True)
