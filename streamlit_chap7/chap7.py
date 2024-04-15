import streamlit as st
import pandas as pd
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_plotly_events import plotly_events
import folium
from streamlit_folium import st_folium

st.title("Streamlit Components Examples")
st.write(
 """This app contains examples of 
 Streamlit Components, find them all in the sidebar!"""
)


def load_lottieurl(url: str):
 r = requests.get(url)
 if r.status_code != 200:
  return None
 return r.json()
lottie_penguin = load_lottieurl(
 "https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json"
)
st_lottie(lottie_penguin, height=200)
st.title("Streamlit Plotly Events + Lottie Example: Penguins")




st.title("SF Trees Map")
trees_df = pd.read_csv("trees.csv")
trees_df = trees_df.dropna(subset=["longitude", "latitude"])
trees_df = trees_df.head(n=100)
lat_avg = trees_df["latitude"].mean()
lon_avg = trees_df["longitude"].mean()
m = folium.Map(
location=[lat_avg, lon_avg], 
zoom_start=12)
st_folium(m)
lat_avg = trees_df["latitude"].mean()
lon_avg = trees_df["longitude"].mean()
m = folium.Map(location=[lat_avg, lon_avg], zoom_start=12)

for _, row in trees_df.iterrows():
 folium.Marker(
 [row["latitude"], row["longitude"]],
 ).add_to(m)
events = st_folium(m)
st.write(events)

from streamlit_extras.mandatory_date_range import date_range_picker
result = date_range_picker("Select a date range")
st.write("Result:", result)

from streamlit_extras.stoggle import stoggle
stoggle(
 "Click me!",
 """ Surprise! Here's some additional content""",
)
