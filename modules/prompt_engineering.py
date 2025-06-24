def create_prompt(question, context="", student_level="class 12"):
    context_section = f"Context:\n{context}\n\n" if context else ""

    return f"""You are a helpful STEM tutor.

Question: {question}

{context_section}Answer in simple terms, step-by-step, suitable for a {student_level} student.
Include formulas if relevant. Use LaTeX-style formatting where needed.
"""
