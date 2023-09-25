import pandas as pd
import numpy as np


# Encontrar en la columna de identificadores, el identificador input del usuario 

def validar_codigo():
  
  validez = True
  while validez:
    codigo_activo = str(input("Digite el codigo del activo a consultar -> "))

    #Acceso al HTML a la columna de los identificadores
    ruta="C:\\Users\\cepc2\\OneDrive\\Documents\\Proyecto Taller de Programacion 2023\\fuenteDeDatos.html"
    datos = pd.read_html(ruta)[0]
    df = pd.DataFrame(datos)
    #desde la fila inicial(0) hasta columna  0 al  1 (exclusivo).  solo estamos seleccionando la primera columna.
    columna_ID = df.iloc[:,0:1]
    lista_identificadores = columna_ID.iloc[1:]
    codigos = [str(codigo[0]) for codigo in lista_identificadores.values]
    if codigo_activo in codigos:
        #Posicion obtiene la fila en la que el identificador se encuentra
        posicion_activo = np.where(np.array(codigos) == codigo_activo)[0][0] + 1
        #Imprime donde se encuentra el activo con el codigo de usuario
        print("Activo Encontrado con ID: ", codigo_activo)
        return posicion_activo
        break
    else:
        print("Activo NO encontrado! Por favor ingrese una opcion valida")

