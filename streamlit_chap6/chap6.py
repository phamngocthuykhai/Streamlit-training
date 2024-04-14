import streamlit as st
import pandas as pd
import plotly.express as px

# tạo bố cục 
st.set_page_config(layout='wide')
st.title('SF Trees')
st.write(
 """
 This app analyses trees in San Francisco using
 a dataset kindly provided by SF DPW.
 """
)

#  Tạo biểu đồ theo hàng
trees_df = pd.read_csv('trees.csv')
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
col1, col2, col3 = st.columns(3, gap="large")
with col1: 
 st.line_chart(df_dbh_grouped)
with col2:
 st.bar_chart(df_dbh_grouped)
with col3:
 st.area_chart(df_dbh_grouped)

# Tạo các tab
tab1, tab2, tab3 = st.tabs(["Line Chart", "Bar Chart", "Area Chart"])
with tab1:
 st.line_chart(df_dbh_grouped)
with tab2:
 st.bar_chart(df_dbh_grouped)
with tab3:
 st.area_chart(df_dbh_grouped)

# tạo sidebar
owners = st.sidebar.multiselect( "Tree Owner Filter",  trees_df["caretaker"].unique())
if owners:
 trees_df = trees_df[trees_df["caretaker"].isin(owners)]
st.line_chart(df_dbh_grouped)
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n = 1000, replace=True) 
st.map(trees_df)


today = pd.to_datetime("today")
trees_df["date"] = pd.to_datetime(trees_df["date"])
trees_df["age"] = (today - trees_df["date"]).dt.days
graph_color = st.sidebar.color_picker("Graph Colors")
if owners:
 trees_df = trees_df[trees_df["caretaker"].isin(owners)]
col1, col2 = st.columns(2)
with col1:
 fig = px.histogram(
 trees_df,
 x=trees_df["dbh"],
 title="Tree Width",
 color_discrete_sequence=[graph_color],
 )
 fig.update_xaxes(title_text="Width")
 st.plotly_chart(fig, use_container_width=True)
with col2:
 fig = px.histogram(
 trees_df,
 x=trees_df["age"],
 title="Tree Age",
 color_discrete_sequence=[graph_color],
 )
 st.plotly_chart(fig, use_container_width=True)
