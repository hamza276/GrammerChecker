from groq import Groq
from constants import API_Key

def get_groq_response(input_text):
    """
    Sends input text to the Groq API and retrieves the response.
    """
    client = Groq(api_key=API_KEY)
    prompt = f"""Proofread and correct the given text: '''{input_text}'''.

    Your task:
    - Rewrite the text if it contains grammatical, spelling, or punctuation errors. Provide the corrected text only, without highlighting or explaining the errors.
    - If the text is already correct, respond only with: "The text is correct."

    Do not explain the corrections or highlight the errors in any way. Just rewrite the text or respond with the phrase exactly as specified."""
    
    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": input_text},
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    response = ""
    for chunk in completion:
        response += chunk.choices[0].delta.content or ""
    return response
