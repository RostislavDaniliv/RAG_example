import os
from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai import ChatOpenAI

load_dotenv()

def demonstrate_without_rag():
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.9)
    
    questions = [
        "Скільки днів відпустки має співробітник у компанії?",
        "Як працюють премії в компанії GoWombat?"
    ]
    
    for question in questions:
        print(f"\n❓ Query: {question}")
        response = llm.invoke(question)
        print(f"🤖 Answer: {response.content}")
        print("-" * 50)

if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: Set OPENAI_API_KEY in .env file")
    else:
        demonstrate_without_rag()
