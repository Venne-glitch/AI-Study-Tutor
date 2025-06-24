from langchain_chroma import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyMuPDFLoader
import os
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

CHROMA_DIR = "db/chroma"

def load_and_index_pdf(path: str):
    print("📚 Loading textbook...")
    loader = PyMuPDFLoader(path)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(pages)

    embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')

    db = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=CHROMA_DIR)
    db.persist()
    print("✅ Indexing complete!")

def retrieve_context(query: str, top_k=3) -> str:
    import re
    if not os.path.exists(CHROMA_DIR):
        raise ValueError("Chroma index not found. Run `load_and_index_pdf()` first.")

    embeddings = HuggingFaceEmbeddings(model_name='all-MiniLM-L6-v2')
    db = Chroma(persist_directory=CHROMA_DIR, embedding_function=embeddings)

    results = db.similarity_search(query, k=top_k)
    context = "\n\n".join([doc.page_content for doc in results])

    context = re.sub(
        r'Second Law\s*\(.*?Gravitation.*?\)',
        'Second Law (Force = mass × acceleration)',
        context,
        flags=re.IGNORECASE
    )

    context = context.replace("inversely proportional to the square", "inversely proportional")  # If needed

    return context

if __name__ == "__main__":
    load_and_index_pdf("data/textbooks/physics_sample.pdf")
