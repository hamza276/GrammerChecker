# Grammar Checker and Proofreader App

## Overview
The **Grammar Checker and Proofreader App** is a Streamlit-powered web application that helps users identify and correct grammatical, spelling, and punctuation mistakes in text. The app highlights incorrect sections, provides corrected sentences, and ensures the text is clear and error-free. It integrates with the **Groq API** for language processing and utilizes **Redlines** for highlighting changes in the text.

---

## Features
- **Proofreading and Grammar Correction**:
  - Automatically detects and corrects errors in the input text.
- **Word Limit Handling**:
  - Supports up to **2700 words** per input.
  - Exceeds words are visually faded and not sent to the model for processing.
- **Highlighted Changes**:
  - Highlights changes in the text using **Redlines** for easy comparison.
- **Corrected Paragraph**:
  - Displays the fully corrected paragraph below the highlights for convenience.
- **User-Friendly Interface**:
  - Built with Streamlit for a clean, interactive, and responsive UI.

---

## Project Structure
```
grammar_checker/
│
├── app.py                 # Main Streamlit application
├── constants.py           # Configuration and constants (e.g., API keys, word limits)
├── utils/                 # Utility functions
│   ├── groq_client.py     # Handles Groq API requests
│   ├── text_processing.py # Processes and trims input text
│   ├── redlines_utils.py  # Generates highlighted changes using Redlines
└── README.md              # Project documentation
```

---

## Prerequisites
### **Software Requirements**
- Python 3.8 or higher
- A valid API key for the Groq API

### **Dependencies**
Install the required Python packages:
```bash
pip install streamlit redlines
```

---

## How to Run the App
1. Clone the repository:
   ```bash
   git clone https://github.com/hamza276/GrammerChecker.git
   cd grammar-checker-app
   ```

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Add your **Groq API key** in `constants.py`:
   ```python
   API_KEY = "your_api_key_here"
   ```

4. Start the application:
   ```bash
   streamlit run app.py
   ```

5. Open the application in your browser (usually at `http://localhost:8501`).

---

## How It Works
1. **Input**:
   - Users can paste or type text into the input box (up to **2700 words**).
2. **Processing**:
   - The app sends the trimmed input to the **Groq API** for grammar checking and corrections.
3. **Output**:
   - If the text is correct, the app displays: **"The text is correct."**
   - If the text has errors:
     - **Highlighted Changes**: Displays changes using `Redlines`.
     - **Corrected Paragraph**: Shows the corrected text below the highlights.

---

## Features in Detail
### **Word Limit Handling**
- Supports up to **2700 words** per input.
- Words exceeding the limit are visually faded and ignored during processing.

### **Redlines Integration**
- Highlights grammatical changes:
  - **Incorrect Text**: Strikethrough in red.
  - **Corrected Text**: Displayed in bold.

### **Error-Free Paragraph Display**
- Provides a clean, rewritten version of the text without highlights.

---

## Example Usage
### Input
```
Me and my brother was goin to the market to buys sandwichs.
```

### Output
1. **Highlighted Changes**:
   ```markdown
   ~~Me and my brother~~ **My brother and I** ~~was goin~~ **were going** to the market to ~~buys sandwichs~~ **buy sandwiches**.
   ```

2. **Corrected Paragraph**:
   ```
   My brother and I were going to the market to buy sandwiches.
   ```

3. **Correct Text Example**:
   ```
   The text is correct.
   ```

---

## Customization
1. **Adjust Word Limit**:
   - Modify the `WORD_LIMIT` variable in `constants.py` to set a new limit.
2. **Change the Model**:
   - Update the `model` parameter in `groq_client.py` to use a different Groq language model.

---

## Troubleshooting
### **Common Issues**
1. **API Key Errors**:
   - Ensure the API key is correctly set in `constants.py`.
   - Verify your Groq API access.
2. **Streamlit Not Recognized**:
   - Ensure Streamlit is installed:
     ```bash
     pip install streamlit
     ```
   - Add Python to your system PATH if necessary.
3. **Text Too Long**:
   - Ensure the input text is within the 2700-word limit.

---

## Future Improvements
- Add multilingual support.
- Support custom dictionaries for specific jargon.
- Integrate a database to save corrections for future use.

---

## License
This project is licensed under the MIT License. Please use, modify, and distribute this app according to the license terms.

---

## Contact
If you have questions or feedback, feel free to reach out:
- **Email**: hafizhamzakhan1997@gmail.com
- **GitHub**: https://github.com/hamza276/GrammerChecker.git

Enjoy using the Grammar Checker and Proofreader App! 🎉
