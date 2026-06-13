import google.generativeai as genai
import os
def saramsham(text):
    api="AIzaSyBVOpDlIL0s-qWRfRl1QM9LBc9FhmAlmDo"
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(f"summarize this text:{text}")
    return response.text