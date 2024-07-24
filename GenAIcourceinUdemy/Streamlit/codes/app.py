import streamlit as st
import pandas as pd
import numpy as np

#title the application
st.title("Hello krishna :)")

#printing the data frame
df=pd.DataFrame({
    'X':[1,2,3,4,5],
    'Y':[10,20,30,40,50]
})

#printing the data frame in the website

st.write(df)

st.write("Line chart")

#ploting the linear plot in the web page
st.line_chart(df)