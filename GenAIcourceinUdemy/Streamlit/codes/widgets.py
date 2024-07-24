import streamlit as st
import pandas as pd
st.title("Text input demo")

name=st.text_input("What is your name?")
st.write(f"Hai {name} :) how are you?")

age=st.slider("select your age :",0,100,25)
st.write(f"YOur age is :{age}")

options=["siksha","vyakarnam","nirutham"]

choice=st.selectbox("what you want to learn:",options)

st.write(f"ok learn {choice}")



#option for uploading the any file
uploaded_file=st.file_uploader("Choose a csv file:",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write("Data in the uploded file")
    st.write(df)




