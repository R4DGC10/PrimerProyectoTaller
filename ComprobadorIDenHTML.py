#Identificar si la entrada del usuario es valida o existe en la columna de identificador
import pandas as pd
import numpy as np

#Apertura de la fuente de datos.html
def abrir_html():
  ruta="C:\\Users\\cepc2\\OneDrive\\Desktop\\TEC\\2023 II Semestre\\Taller Programacion\\Primer Proyecto II Semestre\\PrimerProyectoTaller\\fuenteDeDatos.html"
  datos = pd.read_html(ruta)[0]
  df = pd.DataFrame(datos)
  #desde la fila inicial(0) hasta columna  0 al  1 (exclusivo).  solo estamos seleccionando la primera columna.
  columna_ID = df.iloc[:,0:1]
  lista_identificadores = columna_ID.iloc[1:11]
  return lista_identificadores
print(abrir_html())


def solicitar_identificador(lista_identificadores):
    while True:
        entrada_id = str(input("Digite el identificador del activo -> "))
        # Convertir lista_identificadores.values a una lista de strings
        identificador = [str(id[0]) for id in lista_identificadores.values]
        if entrada_id in identificador:
            # Obtener el índice de entrada_id en lista_identificadores
            posicion = np.where(np.array(identificador) == entrada_id)[0][0] + 1
            print("Activo Encontrado con ID ", entrada_id, "[Posicion de Lista] ", posicion)
            break
        else:
            print("Activo no encontrado con ID, por favor verifique su entrada y vuelva a intentar")

lista_identificadores = abrir_html()
solicitar_identificador(lista_identificadores)




































# def CantidadDigitos(n):
#     x = 0
#     if n<=9:
#         x = 1
#         return x
#     while n>0:
#         n = n//10
#         x = x + 1
#     return x
# ID = int(input("Ingrese el codigo de Activo (4 Digitos) -> "))
# #Prueba
# def codigo_activo(ID):
#     valor = True
#     while valor==True:
#         if CantidadDigitos(ID) > 4:
#             print("Ingrese una codigo de activo valido! ")
#             ID = int(input("Ingrese el codigo de Activo -> "))

#         if CantidadDigitos(ID) == 4:
#             valor = False
#             print("Identificador Valido")
#             return ID
#         else:
#             print("Vuelva a intentarlo")
#             ID = int(input("Ingrese el codigo de Activo -> "))
        
# print(codigo_activo(ID))
           

    
  