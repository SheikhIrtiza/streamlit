import streamlit as st
# Step 1: Initialization
from dotenv import load_dotenv, find_dotenv
from langchain_community.llms import OpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.chat_models import ChatOpenAI
from langchain import PromptTemplate


# Load environment variables.
load_dotenv(find_dotenv())

# Initialize language model
llm = OpenAI(model_name="gpt-3.5-turbo")

# Initialize chat model
chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.3)

# streamlit framework
st.title('LangChain demo')
input_text=st.text_input("You:","Type your message here...")

llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))
# Step 2: Define Prompt Templates
python_prompt = PromptTemplate(
    input_variables=["question"],
    template="Explain {question} in simple terms."
)

# Step 3: Chat Functionality.
def process_message(message):
    if isinstance(message, str):
        message = HumanMessage(content=message)
    response = chat([message])
    return response.content

