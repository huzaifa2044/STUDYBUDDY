def summarize(text, num_sentences=3):
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if s.strip() != ""]

    if len(sentences) <= num_sentences:
        return text

    word_frequency = {}
    words = text.lower().split()
    for word in words:
        word = word.strip(",.!?")
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    sentence_scores = {}
    for sentence in sentences:
        score = 0
        sentence_words = sentence.lower().split()
        for word in sentence_words:
            word = word.strip(",.!?")
            if word in word_frequency:
                score += word_frequency[word]
        sentence_scores[sentence] = score

    ranked_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)
    top_sentences = ranked_sentences[:num_sentences]

    final_summary = []
    for sentence in sentences:
        if sentence in top_sentences:
            final_summary.append(sentence)

    return ". ".join(final_summary) + "."