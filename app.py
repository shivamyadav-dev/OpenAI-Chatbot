import streamlit as st
from utils.llm_chain import get_llm_chain
from config import APP_TITLE, APP_DESCRIPTION

# Page configuration
st.set_page_config(page_title=APP_TITLE, layout="centered")

# Title and description
st.title(APP_TITLE)
st.markdown(APP_DESCRIPTION)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask me anything..."):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                chain = get_llm_chain()
                response = chain.invoke({'question': prompt})
                st.markdown(response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": response})
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
