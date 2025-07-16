import streamlit as st
import pandas as pd
import os

st.title("📊 Roomie Admin Dashboard")

if os.path.exists("chat_logs.csv"):
    df = pd.read_csv("chat_logs.csv")
    st.dataframe(df)
else:
    st.warning("No logs found yet.")
