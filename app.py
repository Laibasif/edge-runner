import os
import streamlit as st
import PyPDF2
from pptx import Presentation
from openai import OpenAI

# Initialize session state variables for managing chat history
if 'history' not in st.session_state:
    st.session_state['history'] = []

# Set up the page configuration
st.set_page_config(layout="wide")

# Initialize the Llama model through OpenAI API
@st.cache_resource
def initialize_llama():
    client = OpenAI(
        api_key="93a2e316faaf46e386453a2ac90ebf0a",  # Replace with your OpenAI API key
        base_url="https://api.aimlapi.com",
    )
    return client

def summarize_pdf(file):
    text = ""
    with PyPDF2.PdfReader(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text

def summarize_ppt(file):
    text = ""
    presentation = Presentation(file)
    for slide in presentation.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text += shape.text + "\n"
    return text

def main():
    llama_client = initialize_llama()

    st.title("Llama Model Chatbot with PDF and PPT Summarization")

    # Chat interface
    chat_container = st.container()
    with chat_container:
        for message in st.session_state['history']:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # File upload section
    uploaded_files = st.file_uploader("Upload PDF or PPT files", type=["pdf", "pptx"], accept_multiple_files=True)

    if uploaded_files:
        summaries = []
        for uploaded_file in uploaded_files:
            if uploaded_file.type == "application/pdf":
                summaries.append(summarize_pdf(uploaded_file))
            elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.presentationml.presentation":
                summaries.append(summarize_ppt(uploaded_file))

        if summaries:
            full_summary = "\n".join(summaries)
            st.session_state['history'].append({"role": "assistant", "content": full_summary})
            st.markdown(full_summary)

    user_input = st.chat_input("Enter your query:")

    if user_input:
        with st.chat_message("user"):
            st.markdown(user_input)
        st.session_state['history'].append({"role": "user", "content": user_input})

        with st.chat_message("assistant"):
            with st.spinner("Generating response..."):
                # Generate response using OpenAI Llama model
                response = llama_client.chat.completions.create(
                    model="meta-llama/Llama-3.2-3B-Instruct-Turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an AI assistant who knows everything.",
                        },
                        {
                            "role": "user",
                            "content": user_input
                        },
                    ],
                )
                full_response = response.choices[0].message.content
                st.markdown(full_response)

        st.session_state['history'].append({"role": "assistant", "content": full_response})
        st.rerun()  # Force a rerun to update the chat display

    # Add a clear button
    if st.button("Clear Chat"):
        st.session_state['history'] = []
        st.rerun()

if __name__ == "__main__":
    main()
