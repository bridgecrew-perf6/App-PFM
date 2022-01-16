import spacy_streamlit
import spacy
from spacy import displacy
import streamlit as st
import en_core_web_sm
import pandas as pd
import numpy as np
import string 
#import random
#import tesseract-ocr
#import pytesseract

#try:
 #   from PIL import Image
#except ImportError:
#    import Image
####------------------MODELO---------------------------------------------

####---------------------------------------------------------------------


models = ["es_core_news_lg"]#en_core_web_sm"]#, es_core_news_la, "en_core_web_md"] #idioma 

#------------Texto devuelto por el OCR------------------------------(Esto lo debería devolver el modelo correctamente transformado e identificado)
#Guardo en una variable el texto de la factura , asumiendo que esto lo que extrajo el OCR. 
documento = """Geprom Software Engineering S.L.
DOMICILIO SOCIAL
Octavi Lecante, 8-10 Pol. Can Magarola 08100 Mollet del Vallès - Barcelona - Administracion: T. 935 707 292
www.geprom.com info@geprom.com
Página 1 de 1
OFICINA CASTELLDEFELS
Ronda de Can Rabadà, 2 5-5 Edifici Lògic 08860 Castelldefels - Barcelona -
T. 933 284 328
PRICE DTO DISC. IMPORTE AMOUNT
Albarán: 18444 Fecha/Date: 27/02/2020 Ref. Client: 342157890
P40LG201580 0030
FASE 1 DESPLAZAMIENTOS Y DIETAS SOLUCIÓN OBJECTIVE WMS
REF: W72001010 30% ACEPTACIÓN
0,30
750,00 225,00
Importe Bruto
Gross Amount
Base Imponible
Net Amount
% I.V.A.
V.A.T.
225,00"""
#----------------------------------------------------
 
#------------Tratar el texto obtenido ----------------(Parte suministrada por el modelo)
nlp = en_core_web_sm.load()
# #Tokenizar el texto  
documento_spacy = nlp(documento)
# #Creear una lista con las plabras que me interesan usando Comprehension lists
documento_procesado = [token for token in documento_spacy if not token.is_stop and not token.is_punct]
#Mostrar la categorización de campos por colores 
st.title("Modelo de extracción de información de facturas")
st.write("""
Extracción de la información utilizando la librería Spacy 
""")
spacy_streamlit.visualize(models, default_text= documento_spacy, visualizers=["ner"])
#---------------------------------------------------------------

#------------Construir una tabla con la clasificación de la inf de la factura----------------------------------
# Introducir el doc tokenizado en pandas
st.write("""
Resumen de la información categorizada y disponible para descargar 
""")
table_data = pd.DataFrame(list(documento), columns=["Data Invoice"])
#Añadir una columna que contendrá la clasificación de la palabra (dirección, teléfono, etc)
table_data['Word Classification'] = "word"

#Mostrar la tabla que hemos creado con los datos de la factura y su categorización
st.dataframe(table_data,1000)

#Añadir botón para descargar csv //PROBLEMA: no separa los datos por columnas
@st.cache
def convert_csv(df):
    csv = df.to_csv().encode('utf-8')
    return df.to_csv(
      sep=";",
      index = False,
      float_format='%g'
      ).encode('utf-8')

csv = convert_csv(table_data)

st.download_button(
  label="Download data as CSV",
  data=csv,
  file_name='data_app.csv',
  mime='text/csv',
)
