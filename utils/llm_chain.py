"""
LLM Chain initialization and setup
"""
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import MODEL_NAME, TEMPERATURE, SYSTEM_PROMPT

def setup_environment():
    """Configure environment variables for API access"""
    load_dotenv()
    os.environ["LANGCHAIN_TRACING_V2"] = "true"

def get_llm_chain():
    """Initialize and return the LLM chain"""
    setup_environment()
    
    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", "Question: {question}")
    ])
    
    # Initialize LLM
    llm = ChatOpenAI(model=MODEL_NAME, temperature=TEMPERATURE)
    
    # Create chain
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    
    return chain
