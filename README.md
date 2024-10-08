### Q&A System with PDF
## Installation Methods

### Method 1: Using Docker

1. **Build the Docker image:**
   ```bash
   docker build -t your_image_name .
   ```
2. **Run the Docker container:**
   ```bash
   docker run -d -p 8501:8501 your_image_name.
   ```
3. **use Docker Compose:**
   ```bash
   docker-compose up .
   ```
### Method 2: Using Python 
1. **Install required packages**
   ```bash
   pip install -r requirements.txt .
   ```
2. **Run the Streamlit application**
   ```bash
   streamlit run app.py .
   ```

### Description

This project demonstrates a question-answering (Q&A) system built using LangChain and Groq. It allows you to upload a PDF file, query the contents of the PDF, and receive relevant answers from a powerful large language model (LLM).

## How it Works

1. **PDF Processing:**
   - The project begins by taking a PDF file as input.
   - The PDF is loaded and split into smaller chunks of text.
   - Each chunk is embedded using Azure OpenAI embeddings.
   - The embeddings are then stored in a vector database (FAISS) for efficient similarity search.

2. **Question Answering:**
   - When a user asks a question, the system performs a similarity search in the vector database using the question.
   - The most relevant text chunks from the PDF are retrieved.
   - These chunks are passed as context to the Groq LLM (Mixtral-8x7b-32768).
   - The LLM generates an answer to the user's question based on the provided context.

## Requirements

- Python 3.12
- `requirements.txt`: Install necessary packages using `pip install -r requirements.txt`.

## Environment Variables

- **GROQ_API_KEY:** Your Groq API key.
- **AZURE_OPENAI_ENDPOINT:** Your Azure OpenAI endpoint.
- **MAJNU:** Your Azure OpenAI deployment name.

## Usage

1. **Upload PDF:** Provide a PDF file as input.
2. **Ask a Question:**  Enter your question related to the PDF's content.
3. **Receive Answer:** The system will generate an answer based on the PDF's content.
### Example Interaction

- **Document:** SampleSet Assignment (A PDF file uploaded)
- **Question:** What are the UI frameworks provided?
- **Response:**

    For your interactive question-answering (QA) bot interface, you can use the following UI frameworks:

    1. **Streamlit** ([streamlit.io](https://streamlit.io/)): Streamlit is an open-source app framework for machine learning and data science projects. It allows you to create interactive web apps with Python in just a few minutes. Streamlit is a great choice for building your QA bot interface due to its simplicity and ease of use. You can use Streamlit to create forms for uploading PDF documents and inputting user queries.

    2. **Gradio** ([gradio.app](https://gradio.app/)): Gradio is an open-source library for creating machine learning user interfaces. With Gradio, you can create interactive web interfaces for your models with just a few lines of code. Gradio is an excellent choice for your QA bot interface as it offers features like file uploads, text input, and real-time output rendering.

   You can choose either Streamlit or Gradio based on your preferences and familiarity with the framework. Both options should be suitable for your needs.

- **Source:** Part 2: Interactive QA Bot Interface 
Problem Statement: Develop an interactive interface for the QA bot from Part 1, allowing users to input queries and retrieve answers in real time. The interface should...

