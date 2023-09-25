import pandas as pd

def apertura_html():
    ruta="C:\\Users\\Manuel Torres O\\OneDrive\\Documentos\\Codigos de Python\\fuenteDeDatos.html"
    datos = pd.read_html(ruta)[0]
    df = pd.DataFrame(datos)
    return df
