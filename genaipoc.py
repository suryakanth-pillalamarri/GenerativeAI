import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import HumanMessage,SystemMessage
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import preprocessing
from docx import Document
from io import BytesIO



def create_word_document(content):
    doc=Document()
    doc.add_paragraph(content)
    buffer=BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return(buffer)

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
    input_text1=preprocessing.remove_special_charaters(input_text)
    input_text1=preprocessing.spell_corrector(input_text1)
    # st.write(f"Given problem statement: {input_text1}")
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
    # Creating a Word document
    word_buffer = create_word_document(parser.invoke(result))
    
    # Providing a download link
    st.download_button(
        label="Download SOP as Word document",
        data=word_buffer,
        file_name="SOP.docx",
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )
    
    
    



if refresh_button:
    input_text=""
    st.query_params.clear()











