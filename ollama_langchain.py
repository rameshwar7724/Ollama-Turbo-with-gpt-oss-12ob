from langchain_core.prompts import ChatPromptTemplate
from langchain.llms import Ollama
import streamlit as st
from langchain_core.output_parsers import StrOutputParser

st.title("Deepseek-R1-Powered locally")
input=st.text_input("What question do you have in mind?")
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the question asked"),
        ("user","Question:{question}")
    ]
)
model=Ollama(model="deepseek-r1:1.5b")
output_parser=StrOutputParser()

chain=prompt|model|output_parser
#chain.invoke({"question":"What is the capital of France?"})

if input:
    st.write(chain.invoke({"question":input}))
