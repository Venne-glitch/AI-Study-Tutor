import os
import json

def save_question(question, answer):
    history_file = "db/user_questions.json"

    if os.path.exists(history_file) and os.path.getsize(history_file) > 0:
        with open(history_file, "r") as f:
            history = json.load(f)
    else:
        history = []

    history.append({"question": question, "answer": answer})

    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)
