import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import plotly.express as px
import matplotlib
matplotlib.use("Agg")  # Must come BEFORE importing project
import pandas as pd

import streamlit as st
import import_ipynb
from Src import project as p

columns=['transaction_id',	'transaction_date',
         	'customer_id',	'customer_gender',	
            'customer_age_group',	'customer_segment',
            'product_id',	'product_name',	'category',	
            'brand',	'quantity'	,'unit_price',	'discount_pct',	
            'sales_amount'	,'payment_method',	'sales_channel',	'region']

RED, GREY, BLUE = "#ff2b2b", "#9aa0a6", "#7cc4ff"

LINE_COLORS = [
    "#4aa3ff", "#ff6b6b", "#ffd166",
    "#06d6a0", "#c77dff", "#ff9f43", "#8ee3e6"
]

st.set_page_config(
    page_title='Retail Sales Analysis',
    page_icon='🛒',
    layout="wide"
)

background_costume_theme="#0f172b"

st.title(":material/school: Retail Sales Analysis")

st.caption(
    "Easily compare products sales against others in their peer group."
)
st.sidebar.title("Dashboard filters :")
st.sidebar.write("costumize your analysis here")

selected_columns=st.sidebar.multiselect("Select features to visualize",default=columns,options=columns)
for col in selected_columns:
    st.sidebar.write(col)

products = p.df['product_name'].unique()
selected_products=st.multiselect("Select products :" , products , default=list(products[:5]))
filtered_df = p.df[
    p.df["product_name"].isin(selected_products)
]

monthly_sales = (
    filtered_df
    .groupby([
        pd.Grouper(key="transaction_date", freq="MS"),
        "product_name"
    ])["sales_amount"]
    .sum()
    .reset_index()
)

st.subheader("Product Sales Over Time")

with st.container(border=True):
 st.line_chart(
    data=monthly_sales,
    x="transaction_date",
    y="sales_amount",
    color="product_name",
    use_container_width=True,
 )

st.write("here's our dataset:")
print(st.dataframe(p.df))


    