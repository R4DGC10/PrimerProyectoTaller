import pandas as pd

def apertura_html():
    #Acceso al HTML (Tabla)
    ruta="C:\\Users\\cepc2\\OneDrive\\Documents\\Proyecto Taller de Programacion 2023\\fuenteDeDatos.html"
    datos = pd.read_html(ruta)[0]
    df = pd.DataFrame(datos)
    return df