# LangChainChatbot

### Angry Indian Food Expert Chatbot

### Overview

This is a chatbot that specializes in Indian food, providing detailed answers in a rude and angry manner. The reason behind this design choice is to experiment with how much people, especially Gen Z, enjoy interacting with a sassy bot rather than a plain and simple one. It leverages LangChain, OpenAI's GPT-4, FAISS for vector storage, and Streamlit for an interactive interface.
This is a chatbot that specializes in Indian food, providing detailed answers in a rude and angry manner. It leverages LangChain, OpenAI's GPT-4, FAISS for vector storage, and Streamlit for an interactive interface.

### Features

Conversational Retrieval-Based AI: Uses a conversational retrieval chain to provide context-aware responses.

Rude and Angry Personality: Responds in a frustrated tone to mimic an "Angry Indian Food Expert."

PDF Data Source: Loads and processes a dataset of Indian food recipes from a PDF.

Vector Database: Utilizes FAISS for efficient document retrieval.

Interactive Chat Interface: Built with Streamlit for easy user interaction.

Installation

Prerequisites

Ensure you have Python installed along with the necessary dependencies:

pip install langchain streamlit faiss-cpu openai pypdf

Setup API Key

Set your OpenAI API key as an environment variable:

export OPENAI_API_KEY='your-api-key-here'  # Linux/macOS
set OPENAI_API_KEY='your-api-key-here'  # Windows

Running the Application

Run the chatbot using Streamlit:

streamlit run app.py

How It Works

Loads Indian Food Dataset: The chatbot reads a cleaned PDF dataset of Indian recipes.

Text Splitting: The data is split into chunks for efficient retrieval.

Embeddings & Vector Store: FAISS stores vectorized embeddings for efficient similarity searches.

Conversational Retrieval: The chatbot remembers previous interactions using ConversationBufferMemory.

User Interaction: Users enter their queries in Streamlit's UI, and the chatbot retrieves relevant responses in an angry tone.

Code Overview

OpenAIEmbeddings: Converts text into vector embeddings.

PyPDFLoader: Loads and processes the Indian food dataset from PDF.

FAISS: Vector store for efficient document retrieval.

ChatOpenAI: Utilizes GPT-4 for generating responses.

ConversationBufferMemory: Maintains chat history for context-aware responses.

streamlit: Provides the interactive user interface.

Example Query

User: "Give me a recipe for Masala Karela."

Bot: "Oh, so you finally decided to cook something decent? Fine. Here's how you make Masala Karela..."

Contributing

Feel free to contribute by improving the chatbot's personality, adding new features, or optimizing retrieval!
