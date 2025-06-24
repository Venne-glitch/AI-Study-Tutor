# 🧠 AI Study Tutor – Local STEM Question Solver with RAG & Ollama

A lightweight, offline AI tutor for Physics, Chemistry, and Math questions built using **Ollama**, **LangChain**, and **Python**.  
It uses **Retrieval-Augmented Generation (RAG)**, **prompt engineering**, and **in-context learning** to provide step-by-step explanations.

---

## 🚀 Features

- ✅ Solve STEM questions (Physics)
- ✅ Step-by-step explanations using local LLM (Ollama)
- ✅ RAG from your own textbooks (PDFs)
- ✅ Simple classifier to label question types (model training concept)
- ✅ In-context learning from past user questions
- ✅ Runs completely offline (no APIs required!)

---

## 🧰 Tech Stack

| Component       | Tech Used                     |
|----------------|-------------------------------|
| Language Model | [Ollama](https://ollama.com) (`mistral`, `phi`, etc.) |
| RAG            | LangChain + ChromaDB + HuggingFace embeddings |
| Prompting      | Custom prompt templates       |
| Classifier     | Scikit-learn (Naive Bayes)     |
| PDF Parsing    | PyMuPDF                        |
| Vector Store   | ChromaDB (local persistence)   |

---

## 📂 Project Structure

study_tutor/
├── main.py # Entry point
├── modules/
│ ├── ollama_solver.py # Query LLM via Ollama
│ ├── prompt_engineering.py # Create prompt templates
│ ├── rag_engine.py # Index & retrieve textbook chunks
│ └── classifier.py # Train and use question type classifier
├── data/
│ └── textbooks/ # Add NCERT or other PDFs here
├── db/
│ ├── chroma/ # Vector store
│ ├── user_questions.json # Stores Q&A history
│ └── classifier.pkl # Saved model for question type