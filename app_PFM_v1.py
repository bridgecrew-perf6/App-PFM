import spacy_streamlit
import spacy
from spacy import displacy
import streamlit as st
import en_core_web_sm
# import csv
import pandas as pd

models = ["en_core_web_sm"]#, "en_core_web_md"] #idioma 

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
 
#------------Tratar el texto obtenido ----------------
nlp = en_core_web_sm.load()

#Tokenizar el texto  
documento_spacy = nlp(documento)
#Cre una lista con las plabras que me interesan usando Comprehension lists
documento_procesado = [token for token in documento_spacy if not token.is_stop and not token.is_punct]

spacy_streamlit.visualize(models, documento_spacy)
#---------------------------------------------------------------

#-----------Añadir botón para descargar csv --------------------
# Introducir el doc tokenizado en pandas
data = pd.DataFrame(documento_procesado,columns=["Title: Data Invoice"])

st.download_button(label='Download CSV', data=documento, file_name="app.csv", mime='text/csv')
#-------------------------------------------------------------------