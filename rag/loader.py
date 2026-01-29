import os
from pypdf import PdfReader

def load_pdfs(file_path):
    texts=[]
    for file in os.listdir(file_path):
        if file.endswith('.pdf'):
            reader=PdfReader(os.path.join(file_path,file))
            full_text=""
            for page in reader.pages:
                if page.extract_text():
                    full_text+=page.extract_text()+'\n'

            texts.append(full_text)
    return texts