from deep_translator import GoogleTranslator
import time
def gtranslator(text, dest):
    root = GoogleTranslator(source="auto", target=dest)
    result = root.translate(text)
    return result
def split_text(text, max_length):
    return [text[i:i + max_length] for i in range(0, len(text), max_length)]
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
def chunks_translating(text,target):
    translated_text = ""
    for i in split_text(text, 4000):
        translated_text += gtranslator(i,target )
        time.sleep(1)
    return translated_text