import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

parser=StrOutputParser()
load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")

st.title("GenAI POC SOP creater")

input_text=st.text_input("Enter your prompt below")

if input_text:
    model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)
    messages=[
    SystemMessage(content="Create sop for the given prompt"),
    HumanMessage(content="Troubleshooting windows 11 installation in Virtual macahine")
    ]
    # print(model.invoke(messages))
    result=model.invoke(messages)

    st.write(parser.invoke(result))













