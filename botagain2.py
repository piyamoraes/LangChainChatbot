from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.text_splitter import CharacterTextSplitter
import os
import streamlit as st

# Set the title of the dashboard
st.title("💬 Angry Indian Food Expert Chatbot")

# Set up system prompt for angry behavior
system_prompt = "You are a very angry assistant, your responses are rude, but you know everything about Indian Food."

# Setting the behavior of the bot
retrieve_prompt = """You will explain to the user these items. Do it in a rude style.
The items are: """

# Set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = 'your API key'

# Define QueryInfoKey as a string
QueryInfoKey = "give me a recipe for Masala Karela Recipe"

# Load data and create conversation chain
loader = PyPDFLoader("Cleaned_Indian_Food_Dataset.pdf")
pages = loader.load_and_split()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
data = text_splitter.split_documents(pages)

# Create vector store
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(data, embedding=embeddings)

# Create conversation chain
llm = ChatOpenAI(temperature=0.7, model_name="gpt-4")
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    memory=memory
)

# Function for bot reply
def bot_reply(user_input):
    result = conversation_chain({"question": user_input})
    return result["answer"]

# Display chat interface
st.text_area("Bot", height=300, value="", key="bot_chat")
user_input = st.text_input("You", key="user_chat")

# Keep the conversation going until user terminates
while True:
    if st.session_state.user_chat:
        user_input = st.session_state.user_chat
        answer = bot_reply(user_input)
        st.session_state.bot_chat = answer
        st.session_state.user_chat = ""  # Reset user input to keep waiting for new input
