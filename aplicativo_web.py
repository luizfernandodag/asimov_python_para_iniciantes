import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import streamlit as st
from IPython.display import display

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("data/customer reviews.csv")
df_top_100_books = pd.read_csv("data/Top-100 Trending Books.csv")

price_max = df_top_100_books['book price'].max()
print(price_max)
price_min = df_top_100_books['book price'].min()
print(price_min)

max_p = st.sidebar.slider("Price Range", price_min, price_max, price_max)

df_top_100_books[df_top_100_books['book price'] < max_p]


fig = px.bar(df_top_100_books["year of publication"].value_counts() )
fig2 = px.histogram(df_top_100_books["book price"])
col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)

