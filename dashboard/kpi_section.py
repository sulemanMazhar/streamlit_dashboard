import streamlit as st
import pandas as pd

class KPISection:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def render(self):
        total_revenue = self.df["revenue"].sum()
        avg_order_value = self.df["revenue"].mean()
        num_orders = self.df["order_id"].nunique()

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Revenue", f"${total_revenue:,.2f}")
        col2.metric("Avg Order Value", f"${avg_order_value:,.2f}")
        col3.metric("Total Orders", num_orders)
