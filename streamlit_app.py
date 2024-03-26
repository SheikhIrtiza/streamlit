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

# Step 4: Main Loop
def main():
    print("Welcome! I'm a Python chatbot. Ask me anything about Python programming.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Chatbot: Goodbye!")
            break
        response = process_message(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()
