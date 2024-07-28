from textblob import TextBlob
from langchain_core.prompts import PromptTemplate
from langchain.prompts import PromptTemplate
import re

def remove_special_charaters(input_text):
    #using  regex to remove non alpha nenumaric characters
    return re.sub(r'[^A-Za-z0-9]+',' ',input_text)

def spell_corrector(text):
    blob = TextBlob(text)
    corrected_text = blob.correct()
    return str(corrected_text)



def add_context(input_text):
    # Adding context to the text
    context = "Help me for installing OS in Virtual machines it may be cloud/virtualbox/VMware you are new to this process"
    template_text = "{context} please write an SOP for {input_text}."
    
    template = PromptTemplate(
        input_variables=["context", "input_text"],
        template=template_text
    )
    
    formatted_prompt = template.format(context=context, input_text=input_text)
    return formatted_prompt






# input_text = "troubleshooting #11234% Windows 11 installation in a virtual machine"

# print(add_context(input_text))



