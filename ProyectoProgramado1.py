#Librerias a utilizar
from math import * 
import pandas as pd
from SumaDigitosProyecto import Sumadigitos
from MetodoLineaRecta import LineaRecta


import numpy as np  


#Apertura de la fuente de datos.html
def abrir_html():
  ruta="C:\\Users\\cepc2\\OneDrive\\Desktop\\TEC\\2023 II Semestre\\Taller Programacion\\Primer Proyecto II Semestre\\PrimerProyectoTaller\\fuenteDeDatos.html"
  datos = pd.read_html(ruta)[0]
  df = pd.DataFrame(datos)
  print(df)
abrir_html()


# def Menu():

#   codigo_activo = 0
#   datos = 0
#   prueba(datos, codigo)
  

#   #Menu 
#   print("   ->>>>> Bienvenido al sistema <<<<<-  ")
#   valor=True
#   while valor==True:
#     f = input("1. Ver la Depreciacion Anual\n2. Ver la Depreciacion hasta la Fecha\n3. Salir\nIngrese una opción: ")
#     if f=="1":
#       opcion_activo=input(("Ingrese el codigo del activo: "))
#       valor=False
#       while True:
#         opcion_metodo=input(("Elija el metodo para ver la Depreciacion del activo\n1.Metodo de Linea Recta\n2.Metodo de Suma de Digitos "))
#         if opcion_metodo=="1":
#           LineaRecta(50000,10000,5)
#           break
#         elif opcion_metodo=="2":
#           Sumadigitos(4,6500,500)
#           break
#         else:
#           print("La opcion no es valida, intente de nuevo")
#     elif f=="2":
#       opcion_activo=input(("Ingrese el codigo del activo: "))
#       valor=False
#       while True:
#         opcion_metodo=input(("Elija el metodo para ver la Depreciacion del activo\n1.Metodo de Linea Recta\n2.Metodo de Suma de Digitos "))
#         if opcion_metodo=="1":
#           LineaRecta(50000,10000,5)
#           break
#         elif opcion_metodo=="2":
#           Sumadigitos(4,6500,500)
#           break
#         else:
#           print("La opcion no es valida, intente de nuevo") 
#     elif f == "3":
#       print("Gracias por usar el sistema")
#       break  

#     else:
#       print("La opción no es válida, intente de nuevo")


#   #Formar Tablas con DataFrame! 


def Principal():
  seleccion = input("Ingrese funcion ")
  if seleccion == 1:
    print(HolaMundo())

Principal()