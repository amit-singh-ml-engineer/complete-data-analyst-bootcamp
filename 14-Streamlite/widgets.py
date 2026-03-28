import streamlit as st
import pandas as pd

st.title("Streamlite input")

name=st.text_input("Enter your name:")
age=st.slider("Select your age:",0,100,25)
st.write(f"Your age is {age}.")
options=['Python','Java','C++','JavaScript']
choice=st.selectbox("Choose your favourite language:",options)
st.write(f"You selected {choice}.")
if name:
    st.write(f"Hello, {name}")
data={
    'Name':['Amit','Ashish','Aditya','Ankit'],
    'Age':[20,21,22,23],
    'City':['New York','Bijing','Dubai','Delhi']
}
df=pd.DataFrame(data)
df.to_csv('sampledata.csv')
st.write(df)
uploaded_file=st.file_uploader("Choose your csv file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv('uploaded_file')
    st.write(df)