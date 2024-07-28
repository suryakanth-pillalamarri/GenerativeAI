import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import preprocessing



#initiaizing the output parser
parser=StrOutputParser()

#loading environment variables from the environment variables
#getting groq api key
load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")

#setting the title to the streamlit app
st.title("GenAI POC SOP creater")

input_text=st.text_area("Enter your prompt below")

# Arrange buttons side by side using columns
col1, col2 = st.columns([1, 1])
with col1:
    submit_button = st.button(label='Submit')
with col2:
    refresh_button = st.button(label='Refresh Input')



#if input text is provided by the user
if submit_button and input_text:
    
    input_text1=preprocessing.spell_corrector(input_text)
    input_text1=preprocessing.add_context(input_text1)
    st.write(f"Given problem statement: {input_text}")
    
    
    #initializing the Chatgroq model with the specified model id and api key
    #here i am selecting the Gemma-2b-It
    model=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)
    #defining the messages for sending to the model
    messages=[
    SystemMessage(content="Create sop for the given prompt"),
    # HumanMessage(content="Troubleshooting windows 11 installation in Virtual macahine")
    HumanMessage(content=input_text1)
    ]
    # print(model.invoke(messages))
    #invoking the model
    result=model.invoke(messages)
    #displaying the result using the Streamlit in the website
    st.write(parser.invoke(result))
    
    
    



if refresh_button:
    input_text=""
    st.query_params.clear()











