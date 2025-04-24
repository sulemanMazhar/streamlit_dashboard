# dashboard/utils.py
import streamlit as st
import pandas as pd

class Utils:
    def filter_data(self, df: pd.DataFrame):
        st.sidebar.header("🔍 Filter Data")
        start_date = st.sidebar.date_input("Start Date", df["order_date"].min())
        end_date = st.sidebar.date_input("End Date", df["order_date"].max())
        categories = st.sidebar.multiselect("Product Category", df["category"].unique(), default=df["category"].unique())

        mask = (
            (df["order_date"] >= pd.to_datetime(start_date)) &
            (df["order_date"] <= pd.to_datetime(end_date)) &
            (df["category"].isin(categories))
        )
        return df[mask]
