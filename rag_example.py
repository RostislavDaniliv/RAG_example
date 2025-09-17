import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
from langchain.schema import Document
from langchain_community.document_loaders import TextLoader

load_dotenv()

def demonstrate_with_rag():
    embeddings = OpenAIEmbeddings()
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9)
    
    hr_documents_path = "hr_documents"
    documents = []
    
    hr_files = [
        "vacation_policy.txt",
        "sick_leave_policy.txt", 
        "work_schedule_policy.txt",
        "bonus_policy.txt"
    ]
    
    for file_name in hr_files:
        file_path = os.path.join(hr_documents_path, file_name)
        if os.path.exists(file_path):
            loader = TextLoader(file_path, encoding='utf-8')
            docs = loader.load()
            for doc in docs:
                doc.metadata['source'] = file_path
                doc.metadata['filename'] = file_name
            documents.extend(docs)
        else:
            print(f"File not found: {file_path}")
    
    if not documents:
        print("Failed to load any documents!")
        return
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    splits = text_splitter.split_documents(documents)
    
    vectorstore = FAISS.from_documents(splits, embeddings)
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=vectorstore.as_retriever(search_kwargs={"k": 3})
    )
    
    questions = [
        "Скільки днів відпустки має співробітник у компанії?",
        "Як працюють премії в компанії?"
    ]
    
    for question in questions:
        print(f"\n❓ Query: {question}")
        print("=" * 60)
        
        relevant_docs = vectorstore.similarity_search(question, k=3)
        print("📄 Relevant documents:")
        for i, doc in enumerate(relevant_docs, 1):
            filename = doc.metadata.get('filename', 'Unknown source')
            print(f"   {i}. 📋 {filename}")
        print()
        
        response = qa_chain.invoke({"query": question})
        print("🤖 RAG Answer:")
        print(response['result'])
        print("-" * 60)

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: Set OPENAI_API_KEY in .env file")
    else:
        demonstrate_with_rag()
