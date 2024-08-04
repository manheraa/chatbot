from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
import os
from langchain.memory import StreamlitChatMessageHistory
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain
groq_api_key=os.environ['GROQ_API_KEY']
llm=ChatGroq(model="mixtral-8x7b-32768",groq_api_key=groq_api_key)

prompt_template="""
Use the following piece of context and chat History to answer the question asked.
Please try to provide the answer only based on the context and in few words
Question:{question}

Helpful Answers:
 """
prompt=PromptTemplate(template=prompt_template,input_variables=['question'])
sthistory=StreamlitChatMessageHistory(key='chatmessage')
hist=ConversationBufferMemory(chat_memory=sthistory)
chain=LLMChain(llm=llm,prompt=prompt,memory=hist)

import streamlit as st
st.title("HI THIS IS GROQ INFERENCE METHOD HI Rohitya")
for msg in sthistory.messages:
    st.chat_message(msg.type).write(msg.content)
if x := st.chat_input():
    st.chat_message("human").write(x)

    # As usual, new messages are added to StreamlitChatMessageHistory when the Chain is called.
    response = chain.invoke(x)
    st.chat_message("ai").write(response["text"])
