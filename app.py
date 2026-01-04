from flask import Flask, render_template, request, redirect
import sqlite3
import requests
from flask import session
SECRET_KEY = "secret123"

# ⚡ Remplace par TA clé Gemini (créée dans Google Cloud)
GEMINI_API_KEY = "AIzaSyAPTtVl6oeZScYHROhnXxnTcbDO6Md4beQ"

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-lite:generateContent?key=" + GEMINI_API_KEY

# -------------------------------
# Fonction pour générer les questions avec Gemini
# -------------------------------
def generate_questions(topic):
    prompt = f"""
    Crée 5 questions QCM faciles sur {topic}.

    Format EXACT :
    Question: ...
    A) ...
    B) ...
    C) ...
    D) ...
    Réponse: A
    """

    response = requests.post(
        GEMINI_URL,
        json={
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }
    )

    data = response.json()
    return data["candidates"][0]["content"]["parts"][0]["text"]

# --------------------------------
# Fonction pour parser les questions
# --------------------------------

def parse_questions(text):
    questions = []
    blocks = text.strip().split("Question:")

    for block in blocks[1:]:
        lines = block.strip().split("\n")

        question_text = lines[0]
        choices = {}
        correct = ""

        for line in lines[1:]:
            if line.startswith(("A)", "B)", "C)", "D)")):
                choices[line[0]] = line[3:]
            elif line.startswith("Réponse"):
                correct = line.split(":")[1].strip()

        questions.append({
            "question": question_text,
            "choices": choices,
            "correct": correct
        })

    return questions



# -------------------------------
# Flask app
# -------------------------------
app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route("/", methods=["GET", "POST"])
def index():
    quiz = []

    if request.method == "POST":
        topic = request.form["topic"]
        raw_text = generate_questions(topic)
        quiz = parse_questions(raw_text)

        # 👉 stocker le quiz pour la correction
        session["quiz"] = quiz

    return render_template("index.html", quiz=quiz)




@app.route("/result", methods=["POST"])
def result():
    quiz = session.get("quiz", [])  # questions stockées
    score = 0

    for i, q in enumerate(quiz):
        user_answer = request.form.get(f"q{i}")  # ex: q0, q1, q2

        if user_answer == q["correct"]:
            score += 1

    total = len(quiz)

    return render_template(
        "result.html",
        score=score,
        total=total,
        quiz=quiz,
        user_answers=request.form
    )



if __name__ == "__main__":
    app.run(debug=True)
