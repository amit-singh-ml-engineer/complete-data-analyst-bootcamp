import streamlit as st
import pandas as pd
import numpy as np

## Title of the application
st.title("Hello Streamlite")

## Display a simple text
st.write("This is the simple text")

## Create the DataFrame

df=pd.DataFrame({
    'first_column':[1,2,3,4],
    'Second_column':[10,20,30,40]
})

## Display DataFrame

st.write("Here is the dataframe")
st.write(df)


## Create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c']
)
st.line_chart(chart_data)