#Librerias a utilizar
from math import * 
import pandas as pd
import numpy as np

from lectura_html import apertura_html
from verificarID import validar_codigo
from FPrincipal1 import FPrincipal1
from FPrincipal2 import FPrincipal2



def MenuPrincipal():
  print("[ ->>> Bienvenido al Sistema <<<- ]\n")
  #Solicitar un identficador//codigo activo, y comprobar si este esta en .html
  tabla = apertura_html()
  fila_activo_encontrado = validar_codigo()


  DetalleActivo = tabla.iloc[fila_activo_encontrado,2]
  print("[ACTIVO A CONSULTAR]: ", DetalleActivo)

  NumActivo = fila_activo_encontrado
  Categoria = tabla.iloc[fila_activo_encontrado,1]
  FechaCompra = tabla.iloc[fila_activo_encontrado,4]
  Moneda = tabla.iloc[fila_activo_encontrado, 5]
  B = int(tabla.iloc[fila_activo_encontrado, 3])
  VS = int(tabla.iloc[fila_activo_encontrado, 6])
  n = int(tabla.iloc[fila_activo_encontrado,7])
  
  # Comprobar si n es igual a 0 ES DECIR: que el activo debe ser sujeto a depreciacion
  if n == 0:
    print("ADVERTENCIA! ACTIVO:  ", DetalleActivo, "NO ESTA SUJETO A DEPRECIACION! \n Por Favor vuelva a intentar con otro activo")
    return

  validez_menu = True
  while validez_menu:
    f = input("[Por favor ingrese una opcion]\n1. Ver la Depreciacion Anual\n2. Ver la Depreciacion hasta la Fecha\n3. Salir\nIngrese una opción: ")
    if f.isdigit():
      f = int(f)
      if f==1:
          FPrincipal1(B,VS,n,Categoria,FechaCompra,Moneda,DetalleActivo,NumActivo)
          break  
      elif f==2:
          FPrincipal2(B,VS,n,Categoria,FechaCompra,Moneda,DetalleActivo,NumActivo)
          break
      elif f==3:
          print("Saliendo del Sistema")
          break
      else:
        print("La opcion ingresada no es valida, intente de nuevo")
    else:
      print("La entrada no es un número, intente de nuevo")

MenuPrincipal()


