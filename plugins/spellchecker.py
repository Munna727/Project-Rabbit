import google.generativeai as genai
import os
import difflib
def spellcheck(text):
    api="AIzaSyBVOpDlIL0s-qWRfRl1QM9LBc9FhmAlmDo"
    # Configure the API key
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"please check and correct any spelling and grammar mistakes in the following paragraph, and return only the corrected version:{text}")
    return response.text


def get_replaced_words(original_text, corrected_text):
    # Split texts into words for comparison
    original_words = original_text.split()
    corrected_words = corrected_text.split()

    # Use difflib to find differences
    diff = difflib.ndiff(original_words, corrected_words)

    # Extract replaced words
    replaced_words = []
    for change in diff:
        if change.startswith("- "):  # Words removed from the original text
            replaced_words.append(change[2:])

    return replaced_words


def corrected_words(original_text, corrected_text):
    original_words = original_text.split()
    corrected_words = corrected_text.split()

    diff = difflib.ndiff(corrected_words,original_words)

    replaced_words = []
    for change in diff:
        if change.startswith("- "):  # Words removed from the original text
            replaced_words.append(change[2:])

    return replaced_words


def underlined_mistakes_text(text,replaced_words):
    for mistake in replaced_words:
        text=text.replace(mistake,f"<b>{mistake}</b>")
    return text






