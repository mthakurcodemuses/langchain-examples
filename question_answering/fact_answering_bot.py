from dotenv import load_dotenv
from langchain.chains import RetrievalQA
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()

# Instantiate embeddings
open_ai_embeddings = OpenAIEmbeddings()
open_ai_chat_llm = ChatOpenAI()

# Instantiate ChromaDB to be used in retrieval
chroma_db = Chroma(
    persist_directory="chroma_db",
    embedding_function=open_ai_embeddings)

# Get retriever from ChromaDB
embeddings_retriever = chroma_db.as_retriever()

# Instantiate RetrievalQA chain
facts_retrieval_qa_chain = RetrievalQA.from_chain_type(
    llm=open_ai_chat_llm,
    retriever=embeddings_retriever,
    chain_type="refine")

result = facts_retrieval_qa_chain.run("What is an interesting fact about the English language?")
print(result)
