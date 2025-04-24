import pandas as pd
import streamlit as st

def load_data(file_path: str) -> pd.DataFrame:
    @st.cache_data
    def _load_data():
        return pd.read_csv(file_path, parse_dates=["order_date"])

    return _load_data()

