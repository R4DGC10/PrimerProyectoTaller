#Librerias
import pandas as pd

def aperturaHTML():
    ruta="C:\\Users\\cepc2\\OneDrive\\Desktop\\VersionFinal\\PrimerProyectoTaller\\fuenteDeDatos.html"
    datos = pd.read_html(ruta)[0]
    df = pd.DataFrame(datos)
    return df
