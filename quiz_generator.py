def generate_quiz(text, num_questions=5):
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip() != ""]

    quiz_questions = []

    for sentence in sentences:
        words = sentence.split()
        if len(words) < 4:
            continue

        clean_words = [w.strip(",.!?") for w in words]
        answer_word = max(clean_words, key=len)

        question_text = sentence.replace(answer_word, "_____")

        quiz_questions.append({
            "question": question_text,
            "answer": answer_word
        })

        if len(quiz_questions) == num_questions:
            break

    return quiz_questions