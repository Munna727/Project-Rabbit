from docx import Document
from docx2pdf import convert
import pythoncom

pythoncom.CoInitialize()
# Convert a single file

def text_to_docx(text):
    doc = Document()
    doc.add_paragraph(text)
    doc.save("templates/output.docx")


def convertt(froom,to):
    convert(froom,to)
