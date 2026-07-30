from pypdf import PdfReader

def extract_text(uploded_file):

    reader = PdfReader(uploded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text() + "\n\n"

    return text