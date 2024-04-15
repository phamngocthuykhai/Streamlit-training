import pandas as pd
import streamlit as st
from st_aggrid import AgGrid
import plotly.express as px
from streamlit_plotly_events import plotly_events


st.title("Streamlit AgGrid Example: Penguins")
penguins_df = pd.read_csv("penguins.csv")
st.write("AgGrid DataFrame:")
response = AgGrid(penguins_df, height=500, editable=True)
df_edited = response["data"]
st.write("Edited DataFrame:")
st.dataframe(df_edited)


st.title("Streamlit Plotly Events Example: Penguins")
df = pd.read_csv("penguins.csv")
fig = px.scatter(df, x="bill_length_mm", y="bill_depth_mm", 
color="species")
selected_point = plotly_events(fig, click_event=True)
if len(selected_point) == 0:
 st.stop()
selected_x_value = selected_point[0]["x"]
selected_y_value = selected_point[0]["y"]
df_selected = df[
 (df["bill_length_mm"] == selected_x_value)
 & (df["bill_depth_mm"] == selected_y_value)
]
st.write("Data for selected point:")
st.write(df_selected)


