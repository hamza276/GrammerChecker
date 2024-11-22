def process_input_text(input_text, word_limit):
    """
    Processes the input text to calculate word count, trim excess words, and return them for display.
    """
    words = input_text.split()
    word_count = len(words)
    trimmed_text = " ".join(words[:word_limit])
    excess_text = " ".join(words[word_limit:]) if word_count > word_limit else ""
    return trimmed_text, word_count, excess_text
