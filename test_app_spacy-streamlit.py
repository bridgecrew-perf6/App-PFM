import spacy_streamlit

models = ["en_core_web_sm", "en_core_web_md"] #idioma 
default_text = "Sundar Pichai is the CEO of Google." #aquí debemos pasar el string que devuelve el OCR
spacy_streamlit.visualize(models, default_text)