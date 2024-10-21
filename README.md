# DocuSummarize - AI-Powered PDF PPT Chatbot
The Llama Model Chatbot is a web application built using Streamlit that allows users to interact with a chatbot and summarize content from PDF and PowerPoint files. This project aims to provide users with an easy way to extract and summarize information from documents, enhancing their productivity and understanding of the content.

## Features
- **Chatbot Interface**: Users can interact with the chatbot and ask questions related to the summarized content.
- **PDF Summarization**: Upload PDF files, and the chatbot will extract and summarize the text for you.
- **PowerPoint Summarization**: Upload PPTX files, and the chatbot will extract text from the slides and provide a summary.
- **Future Enhancements**: Plans to add image summarization features in future releases, allowing users to upload images and receive summarized information.

## Technologies Used
- **Streamlit**: A Python library to create web apps for machine learning and data science projects.
- **PyPDF2**: A library to read and extract text from PDF files.
- **python-pptx**: A library to create and manipulate PowerPoint (.pptx) files.
- **OpenAI**: API for using the Llama model to generate responses.

## Installation
To run this project, clone the repository and install the required packages using the `requirements.txt` file.

### Steps to Install
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```
2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Open your web browser and go to `http://localhost:8501`.
3. Upload your PDF or PPTX files to get summaries.
4. Interact with the chatbot to ask questions regarding the summarized content.


This project is licensed under the MIT License. 
