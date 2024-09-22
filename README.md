# Chatbot with Conversational Retrieval and Google Generative AI

## Overview

Welcome to the **Chatbot with Conversational Retrieval and Google Generative AI**! This FastAPI application allows users to interact with a sophisticated chatbot that leverages advanced language models and a contextual retrieval system to provide intelligent responses based on conversation history and external documents.

## Features

- **Conversational AI:** Engage in dynamic conversations with the chatbot using natural language.
- **Contextual Retrieval:** The chatbot can pull in relevant information from a vector database based on the conversation history.
- **Document Upload:** Users can add text documents to the system, enhancing the chatbot’s knowledge base.

## Getting Started

### Prerequisites

Make sure you have the following installed:


### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chatbot-repo.git
   ```
2. Setup Your Environment Vairables:

Create a .env file in the root of your project and add your Google API key:
```text
GOOGLE_API_KEY=your_google_api_key_here
```
# Running the Application
```bash
python app.py
```
# Using the Chatbot
1. Open your web browser and navigate to http://localhost:8000/docs to access the interactive API documentation provided by FastAPI.
2. Use the /chat endpoint to send messages to the chatbot.
# Adding Documents
You can add text documents to the Chroma vector database by running the add_document_to_chroma function. Simply execute the script and provide the path to the text file you wish to add.
```bash
python chroma_embedding.py
```
# Example Usage
To interact with the chatbot:
1. Send a POST request to /chat with the user's input.
2. Receive a JSON response containing the chatbot's answer.
```json
POST /chat
{
    "user_input": "What is the capital of France?"
}

Response:
{
    "response": "The capital of France is Paris."
}
```




   
   
