import re

def clean_text(text):
    text=re.sub(r'\s+'," ",text)
    return text.strip()

def chunk_text(text,chunk_size=3):
    sentences=text.split('. ')
    chunks=[]
    for i in range(0,len(sentences),chunk_size):
        chunk='. '.join(sentences[i:i+chunk_size])
        chunks.append(chunk)

    return chunks