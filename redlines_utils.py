from redlines import Redlines

def generate_highlighted_text(original_text, corrected_text):
    """
    Generates highlighted text using Redlines.
    """
    diff = Redlines(original_text, corrected_text)
    return diff.output_markdown
