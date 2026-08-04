from flask import Flask, render_template, request
from summarizer import summarize
from flashcard_generator import generate_flashcards
from quiz_generator import generate_quiz

app = Flask(__name__)

notes_text = ""


@app.route("/")
def home():
    status = "Loaded" if notes_text != "" else "Not loaded"
    return render_template("index.html", status=status)


@app.route("/load", methods=["POST"])
def load_notes():
    global notes_text

    uploaded_file = request.files.get("notes_file")
    typed_notes = request.form.get("typed_notes")

    if uploaded_file and uploaded_file.filename != "":
        notes_text = uploaded_file.read().decode("utf-8")
    elif typed_notes and typed_notes.strip() != "":
        notes_text = typed_notes
    else:
        notes_text = ""

    return home()


@app.route("/summary")
def summary_page():
    if notes_text == "":
        return render_template("summary.html", summary=None)
    summary = summarize(notes_text)
    return render_template("summary.html", summary=summary)


@app.route("/flashcards")
def flashcards_page():
    if notes_text == "":
        return render_template("flashcards.html", flashcards=None)
    cards = generate_flashcards(notes_text)
    return render_template("flashcards.html", flashcards=cards)


@app.route("/quiz")
def quiz_page():
    if notes_text == "":
        return render_template("quiz.html", quiz=None)
    quiz = generate_quiz(notes_text)
    return render_template("quiz.html", quiz=quiz)


@app.route("/quiz/submit", methods=["POST"])
def quiz_submit():
    total = int(request.form.get("total_questions"))
    score = 0
    results = []

    quiz = generate_quiz(notes_text)

    for i in range(total):
        user_answer = request.form.get(f"answer_{i}", "").strip().lower()
        correct_answer = request.form.get(f"correct_{i}", "").strip().lower()
        is_correct = (user_answer == correct_answer)

        if is_correct:
            score += 1

        results.append({
            "question": quiz[i]["question"],
            "user_answer": request.form.get(f"answer_{i}", ""),
            "correct_answer": request.form.get(f"correct_{i}", ""),
            "is_correct": is_correct
        })

    return render_template("quiz_result.html", score=score, total=total, results=results)


if __name__ == "__main__":
    app.run(debug=True)