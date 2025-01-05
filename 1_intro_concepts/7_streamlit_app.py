import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Load environment variables
load_dotenv()

# Initialize the model
model = ChatOpenAI(model="gpt-3.5-turbo")

# Define prompt templates
system_template = """
You are an expert software developer who helps explain code to others.
Given a code snippet, analyze it and explain:
1. What the code does in simple terms
2. Key concepts and patterns used
3. Potential issues or improvements to consider

Code to analyze: {code}
"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("user", "User query: {user_query}")
])

# Streamlit app
st.title('GDGOnCampus Coding Assistant')

# User inputs
user_query = st.text_input("Enter your question:")
code = st.text_area("Enter the code snippet:")

# Button to submit
if st.button('Analyze Code'):
    if user_query and code:
        # Process the prompt through the model
        # LCEL: Langchain Expression Language
        chain = prompt_template | model | StrOutputParser()
        result = chain.invoke({"code": code, "user_query": user_query})
        
        # Display the result
        st.write(result)
    else:
        st.warning("Please enter both a question and a code snippet.")
