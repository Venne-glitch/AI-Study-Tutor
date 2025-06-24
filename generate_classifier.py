import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import os

# Example training data
questions = [
    "What is Newton's second law?",        # Conceptual
    "Derive the formula for kinetic energy",  # Derivation
    "Calculate the force when mass is 10kg and acceleration is 5m/s²",  # Numerical
    "Explain photosynthesis",              # Conceptual
    "Find the velocity from the given data", # Numerical
    "Prove Ohm’s law using basic principles" # Derivation
]

labels = ["conceptual", "derivation", "numerical", "conceptual", "numerical", "derivation"]

# Train model
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

clf = MultinomialNB()
clf.fit(X, labels)

# Save to db/classifier.pkl
os.makedirs("db", exist_ok=True)
with open("db/classifier.pkl", "wb") as f:
    pickle.dump((vectorizer, clf), f)

print("✅ Classifier saved successfully to db/classifier.pkl")
