# RAG Example Project

This project demonstrates the difference between using a Large Language Model (LLM) with and without Retrieval-Augmented Generation (RAG) for answering questions about HR policies.

## Project Overview

The project contains two main examples:
1. **Simple LLM Example** (`simple_llm_example.py`) - Uses only the LLM without any external knowledge
2. **RAG Example** (`rag_example.py`) - Uses RAG to retrieve relevant information from HR documents before generating answers

## Setup Instructions

### Prerequisites
- Python 3.12 or higher
- OpenAI API key

### Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd RagExample
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Project Structure

```
RagExample/
├── hr_documents/           # HR policy documents
│   ├── vacation_policy.txt
│   ├── sick_leave_policy.txt
│   ├── work_schedule_policy.txt
│   └── bonus_policy.txt
├── rag_example.py         # RAG implementation
├── simple_llm_example.py  # Simple LLM example
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## File Descriptions

### `simple_llm_example.py`

This file demonstrates how a standard LLM responds to questions without access to specific company documents.

**Features:**
- Uses OpenAI's GPT-4o-mini model
- Asks questions about HR policies
- Shows responses based only on the model's training data
- Demonstrates limitations when specific company information is needed

**Usage:**
```bash
python simple_llm_example.py
```

**Example Questions:**
- "Скільки днів відпустки має співробітник у компанії?" (How many vacation days does an employee have in the company?)
- "Як працюють премії в компанії GoWombat?" (How do bonuses work at GoWombat company?)

### `rag_example.py`

This file implements a complete RAG system that retrieves relevant information from HR documents before generating answers.

**Features:**
- Loads HR policy documents from the `hr_documents/` folder
- Splits documents into chunks for better processing
- Creates vector embeddings using OpenAI embeddings
- Uses FAISS for efficient similarity search
- Retrieves relevant document chunks based on query similarity
- Generates answers using retrieved context
- Shows which documents were used for each answer

**Key Components:**
- **Document Loading:** Loads text files from the HR documents directory
- **Text Splitting:** Uses RecursiveCharacterTextSplitter to create manageable chunks
- **Vector Store:** FAISS vector database for storing and searching embeddings
- **Retrieval:** Similarity search to find relevant document chunks
- **Generation:** Uses retrieved context to generate accurate answers

**Usage:**
```bash
python rag_example.py
```

**Process Flow:**
1. Loads all HR policy documents
2. Splits documents into chunks (1000 characters with 200 character overlap)
3. Creates vector embeddings for all chunks
4. For each question:
   - Performs similarity search to find relevant chunks
   - Displays which documents were retrieved
   - Generates answer using retrieved context

## HR Documents

The project includes sample HR policy documents in Ukrainian:

- **vacation_policy.txt** - Company vacation policy (20 working days annually)
- **sick_leave_policy.txt** - Sick leave procedures and rules
- **work_schedule_policy.txt** - Work schedule and hours policy
- **bonus_policy.txt** - Comprehensive bonus and incentive system

## Key Dependencies

- **langchain-openai** - OpenAI integration for LLM and embeddings
- **langchain-community** - Community tools including FAISS vector store
- **faiss-cpu** - Vector similarity search
- **python-dotenv** - Environment variable management
- **langchain** - Core LangChain framework

## Comparison

| Aspect | Simple LLM | RAG System |
|--------|------------|------------|
| Knowledge Source | Training data only | Training data + company documents |
| Accuracy | Generic responses | Company-specific accurate answers |
| Context | No access to specific policies | Full access to HR documents |
| Transparency | No source information | Shows which documents were used |
| Setup Complexity | Simple | More complex with vector store |

## Running the Examples

1. **Run the simple LLM example:**
   ```bash
   python simple_llm_example.py
   ```

2. **Run the RAG example:**
   ```bash
   python rag_example.py
   ```

## Expected Output

The RAG example will show:
- Which documents were loaded
- For each question:
  - The question asked
  - Which HR documents were retrieved as relevant
  - The generated answer based on the retrieved context

## Customization

You can customize the system by:
- Adding more HR documents to the `hr_documents/` folder
- Modifying the chunk size and overlap in the text splitter
- Adjusting the number of retrieved documents (currently set to 3)
- Changing the LLM model or temperature settings

## Troubleshooting

- **API Key Error:** Ensure your OpenAI API key is correctly set in the `.env` file
- **File Not Found:** Make sure all HR document files exist in the `hr_documents/` folder
- **Import Errors:** Verify all dependencies are installed using `pip install -r requirements.txt`
