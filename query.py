from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

db = Chroma(persist_directory="./chroma_db", embedding_function=OpenAIEmbeddings())
retriever = db.as_retriever()

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0),
    retriever=retriever,
    return_source_documents=True
)

query = "How can I create a function in Xano?"
result = qa_chain.invoke({"query": query})

print(result["result"])

