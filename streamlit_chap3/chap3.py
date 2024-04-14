import streamlit as st
import pandas as pd
import altair as alt
import pydeck as pdk
import plotly.express as px

st.title('SF Trees')
st.write(
 """This app analyzes trees in San Francisco using
 a dataset kindly provided by SF DPW"""
)
trees_df = pd.read_csv('trees.csv')
st.write(trees_df.head())

# Line chart
df_dbh_grouped = pd.DataFrame( trees_df.groupby(["dbh"]).count()["tree_id"]).reset_index()
df_dbh_grouped.columns = ["dbh", "tree_count"]
st.line_chart(df_dbh_grouped, x="dbh", y="tree_count")

# tạo dữ liệu trên bản đồ
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n = 1000)
st.map(trees_df)


fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)


df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
df_caretaker.columns = ['caretaker', 'tree_count']
fig = alt.Chart(df_caretaker).mark_bar().encode(x = 'caretaker', y = 'tree_count').properties(width=600, height=400)
st.altair_chart(fig)


# ---vẽ biểu đồ map--
trees_df.dropna(how='any', inplace=True)
sf_initial_view = pdk.ViewState(
 latitude=37.77,
 longitude=-122.4,
 zoom=11,
 pitch=30
 )
hx_layer = pdk.Layer( 'HexagonLayer', data = trees_df, get_position = ['longitude', 'latitude'], radius=100, extruded=True)
st.pydeck_chart(pdk.Deck(
 map_style='mapbox://styles/mapbox/outdoors-v11',
 initial_view_state=sf_initial_view,
 layers = [hx_layer]
 ))
