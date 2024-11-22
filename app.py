import streamlit as st
from groq_client import get_groq_response
from text_processing import process_input_text
from redlines_utils import generate_highlighted_text
from constants import WORD_LIMIT

# Streamlit UI
st.title("Grammar Checker and Proofreader")
st.markdown("This application proofreads the given text and corrects any grammatical mistakes. If the text is incorrect, it highlights changes and rewrites the corrected paragraph.")

# Input field for text
input_text = st.text_area(
    "Enter text to proofread (max 2700 words):",
    placeholder="Type or paste your text here...",
    height=200,  # Wider rectangular box
)

# Process input text for word count and trimming
trimmed_text, word_count, excess_text = process_input_text(input_text, WORD_LIMIT)

# Display word count and warning if exceeded
st.markdown(f"Word count: {min(word_count, WORD_LIMIT)} / {WORD_LIMIT}")
if excess_text:
    st.markdown("Exceeding words are faded and will not be processed by the model.")
    st.markdown(f"<p>{trimmed_text} <span style='color:lightgray;'>{excess_text}</span></p>", unsafe_allow_html=True)

# Action button
if st.button("Check Grammar"):
    if not trimmed_text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Processing..."):
            response = get_groq_response(trimmed_text)  # Get response from Groq API

        st.subheader("Corrected Sentence:")

        if response.strip() == "The text is correct.":
            st.markdown(f"<span style='color: green; font-size: 18px;'>{response}</span>", unsafe_allow_html=True)
        else:
            highlighted_text = generate_highlighted_text(trimmed_text, response)
            st.markdown(highlighted_text, unsafe_allow_html=True)
            st.markdown("### Corrected Paragraph:")
            st.markdown(f"<span style='font-size: 16px;'>{response}</span>", unsafe_allow_html=True)
