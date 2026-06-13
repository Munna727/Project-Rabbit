import google.generativeai as genai
from flask import Flask, request, render_template
# Set your API key directly
api_key = "the gemini api key to be placed here"
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

def main():
        print("Welcome to the Gemini LLM Console Application")
        count = 0
        history = []
        count+=1
        if request.method=='POST':
            user_input = request.form['question']
        if user_input.lower() in ["exit", "quit"]:
            print("")
        response = get_gemini_response(user_input)
        res=""
        for chunk in response:
            res+=chunk.text
        each = {" You:": user_input, "Rabbit:": res}
        history.append(each)
        return history,user_input
