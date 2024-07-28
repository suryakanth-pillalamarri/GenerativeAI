from langchain_ollama import OllamaLLM
import streamlit as st 



st.title("Langchain demo with LLAMA3")

input_text=st.text_input("Enter your prompt in below")




if input_text:
    model=OllamaLLM(model="llama3")
    result=model.invoke(input=input_text)
    st.write(result)