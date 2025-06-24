import sys
import os 

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from modules.prompt_engineering import create_prompt
from modules.rag_engine import retrieve_context
from modules.ollama_solver import solve_questions
from modules.classifier import predict_type
from utils.histrory import save_question

def tutor_flow(question):
    q_type = predict_type(question)

    context = retrieve_context(question)

    prompt = create_prompt(question, context)

    answer = solve_questions(prompt)

    save_question(question, answer)

    print(f"\n Question Type: {q_type}")
    print("\n Answer:\n")
    print(answer)

if __name__ == '__main__':
    print("Welcome to AI Study Tutor")

    while True:
        question = input("\n Enter your question (or type exit): ").strip()
        if question.lower() == exit:
            print("\n Thank yoy for using AI Study Tutor. Goodbye!")
            break
        
        tutor_flow(question)