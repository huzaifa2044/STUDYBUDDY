def generate_flashcards(text, num_cards=5):
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip() != ""]

    flashcards = []

    for sentence in sentences:
        words = sentence.split()
        if len(words) < 4:
            continue

        front = " ".join(words[:4]) + "..."
        back = sentence

        flashcards.append({
            "front": front,
            "back": back
        })

        if len(flashcards) == num_cards:
            break

    return flashcards