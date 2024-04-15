import pandas as pd
import plotly.express as px
import requests
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report
from streamlit_plotly_events import plotly_events

st.subheader("Pandas Profiling of Penguin Dataset")
df = pd.read_csv("penguins.csv")
fig = px.scatter(df, x="bill_length_mm", y="bill_depth_mm", 
color="species")
selected_point = plotly_events(fig, click_event=True)


penguin_profile = ProfileReport(df, explorative=True)
st_profile_report(penguin_profile)