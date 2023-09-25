import pandas as pd
import numpy as np
from Abrir_html import apertura_html 

def validar_codigo():
  
  validez = True

  while validez:

    codigo_activo = str(input("Digite el codigo del activo a consultar -> "))
    ruta="C:\\Users\\Manuel Torres O\\OneDrive\\Documentos\\Codigos de Python\\fuenteDeDatos.html"
    datos = pd.read_html(ruta)[0]
    df = pd.DataFrame(datos)
    columna_ID = df.iloc[:,0:1]
    lista_identificadores = columna_ID.iloc[1:]
    codigos = [str(codigo[0]) for codigo in lista_identificadores.values]

    if codigo_activo in codigos:
      posicion_activo = np.where(np.array(codigos) == codigo_activo)[0][0] + 1
      return posicion_activo
    else:
      print("Activo NO encontrado! Por favor ingrese una opcion valida")
