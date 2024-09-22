import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain.memory import ConversationBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
#print("successfully configured")

llm=model = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.7)
#print("llm initialized")
# to remember the chat we will import the memeory from langchain
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
embeddings = GoogleGenerativeAIEmbeddings(model = "models/embedding-001")
vector_db = Chroma(embedding_function=embeddings, collection_name="my_collection",persist_directory="./my_chroma_db")
retriever = ContextualCompressionRetriever(
    base_compressor=LLMChainExtractor.from_llm(llm),
    base_retriever=vector_db.as_retriever()
)

prompt_template = ChatPromptTemplate.from_template("""
    Context: {context}
    Chat History: {chat_history}
    Human: {question}
    AI: Please provide a relevant answer based on the context and chat history.
""")

conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    memory=memory,
    combine_docs_chain_kwargs={"prompt": prompt_template}
)

def chatbot_response(user_input):

    return conversation_chain.invoke({"question": user_input})["answer"]