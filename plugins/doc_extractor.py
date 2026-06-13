import PyPDF2
import pythoncom
pythoncom.CoInitialize()
def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        count=1
        for page in range(len(reader.pages)):
            text+=f"\n Page:{count}\n"
            text += reader.pages[page].extract_text()
            count+=1
        return text


