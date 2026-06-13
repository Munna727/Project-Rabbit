from flask import Flask, request, render_template,send_file
import pythoncom
import os
from deep_translator import GoogleTranslator
import google.generativeai as genai
from gtts import gTTS
from plugins import translator
from plugins import chat_bot as bot
from plugins import spellchecker as checker
from plugins import doc_extractor as de
from plugins import summarizer as summy
from plugins import txt_pdf as tp
from plugins import word_learner as learner
from plugins import dictionary as dic
from plugins import getdate as gd

pythoncom.CoInitialize()
app = Flask(__name__)

def audio(mytext, language):
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("static/audios/demo.mp3")
    return "static/audios/demo.mp3"


def converter(text, target):
    my_translator = GoogleTranslator(source="auto", target=target)
    result = my_translator.translate(text=text)
    return result


@app.route("/", methods=["GET", "POST"])
def home():
    with open("hist.txt","w+") as f:
        f.write("")
    info=gd.getDate()
    word=gd.getword()
    wordmean=dic.define(word)

    return render_template("/index.html", d=info, word=word, wordmean=wordmean)


@app.route("/about",methods=["GET","POST"])
def about():
    pass
    return render_template("/about.html")


@app.route("/team",methods=["GET","POST"])
def team():
    pass
    return render_template("/team.html")


@app.route('/translator', methods=["GET", "POST"])
def convert():
    text = ""
    k = ""
    audio_url = ""
    target = ""
    url = ""
    if request.method == "POST":
        target = request.form['target']
        text = request.form["text"]
        if len(text) <= 4000:
            k = translator.gtranslator(text, target)
            audio_url = audio(k, target)
        else:
            translator.split_text(text, 4000)
            k = translator.chunks_translating(text, target)
            audio_url = audio(k, target)
    return render_template("/translator.html", trans=k, url=audio_url,text=text)


@app.route('/dictionary', methods=["GET", "POST"])
def dictionary():
    response = ""
    if request.method == "POST":
        language = "en"
        word = request.form['input']
        response = dic.define(word)
        paryay = dic.synonym(word)
        vyatirekh = dic.antonym(word)
        audio(word, language)
        word = word.capitalize()
        own_sentence = dic.example_sentence(word)
        return render_template('dictionary.html', respon=response, wrd=word, paryay=paryay, vyatirekh=vyatirekh, own_sentence=own_sentence)
    else:
        return render_template('dictionary.html', respon=None, wrd=None)


@app.route("/doc_translator", methods=["GET", "POST"])
def doc_extractor():
    import pythoncom
    pythoncom.CoInitialize()
    result=''
    if request.method == "POST":
        target = request.form['target']
        pdf = request.files['myfile']
        pdf.save(f'uploaded_pdf/user_PDF.pdf')
        pdf_path = "uploaded_pdf/user_PDF.pdf"
        text = de.extract_text_from_pdf(pdf_path)
        if len(text) <= 4000:
            result = translator.gtranslator(text, target)
            tp.text_to_docx(result)
            tp.convertt("templates/output.docx", "output.pdf")
        else:
            translator.split_text(text, 4000)
            result = translator.chunks_translating(text, target)
            tp.text_to_docx(result)
            tp.convertt("templates/output.docx", "output.pdf")

    return render_template("doc_translator.html", translated=result)


@app.route('/output.pdf', methods=["GET", "POST"])
def pdfoutput():
    file="output.pdf"
    return send_file(file, as_attachment=True, download_name="Translated.pdf", mimetype='application/pdf')


@app.route("/word_learner", methods=["GET"])
def word_learner():
    word, definition = learner.meaning_finder()
    synonym = dic.synonym(word)
    antonym = dic.antonym(word)
    return render_template("word_learner.html", rand=word, meaning=definition, synonym=synonym, antonym=antonym)


@app.route("/spellchecker", methods=['GET', 'POST'])
def spell_checker():
    text = ""
    text_with_mistakes=""
    checked_text = ""
    underline_checked=""
    if request.method == "POST":
        text = request.form['text']
        checked_text = checker.spellcheck(text)
        mistake_words=checker.get_replaced_words(text,checked_text)
        text_with_mistakes=checker.underlined_mistakes_text(text,mistake_words)
        checked_words=checker.corrected_words(text,checked_text)
        underline_checked=checker.underlined_mistakes_text(checked_text,checked_words)
    return render_template("spellchecker.html", input_text=text_with_mistakes, checked=underline_checked)


@app.route("/summarizer",methods=['GET', 'POST'])
def summarize():
    text = ""
    edited = ""
    if request.method == "POST":
        text = request.form['text']
        edited = summy.saramsham(text)
    return render_template("summarizer.html", summarized=edited, input_text=text)


@app.route('/chat', methods=['GET', 'POST'])
def chat_bot():
    api = "AIzaSyBVOpDlIL0s-qWRfRl1QM9LBc9FhmAlmDo"
    # Configure the API key
    api_key = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=api)
    model = genai.GenerativeModel('gemini-1.5-flash')
    chat = model.start_chat(history=[])
    with open("hist.txt", "r") as f:
        hist = f.read()
    count = ""
    history = []
    user_input = ""
    if request.method == "POST":
        history, user_input = bot.main()
        for i in history:
            for l, k in i.items():
                hist += "<h3>"+l+"</h3>"+'<br>'
                hist += k+'<br>'
        with open("hist.txt",'w') as f:
            f.write(hist)
    return render_template('chat.html', response=hist, user_input=user_input)


if __name__ == "__main__":
    app.run(debug=True)