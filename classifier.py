from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

def train_classifier():
    questions = [
        "State Newton's 1st law",
        "Derive the formula for emf",
        "A ball is trhown at 30m/s...."
    ]
    labels = ["conceptual", "derivation","numerical"]

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(questions)

    clf = MultinomialNB()
    clf.fit(X, labels)

    pickle.dump((vectorizer, clf), open("db/classifier.pkl", "wb"))

def predict_type(question):
    vectorizer, clf = pickle.load(open("db/classifier.pkl", "rb"))
    X = vectorizer.transform([question])
    return clf.predict(X)[0]
