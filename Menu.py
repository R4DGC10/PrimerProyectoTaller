import pandas as pd
import numpy as np
from Abrir_html import apertura_html 
from Funcion1 import Funcion1
from Funcion2 import Funcion2

def MenuPrincipal():

  print("[ ->>> Bienvenido al Sistema <<<- ]\n")

  validez_menu = True
  while validez_menu:

    f = input("[Por favor ingrese una opcion]\n1. 1. Ver la Depreciacion Anual\n2. Ver la Depreciacion hasta la Fecha\n3. Salir\nIngrese una opción: ")
    if f.isdigit():
      f = int(f)
      if f==1:
          Funcion1()
          break  
      elif f==2:
          Funcion2()
          break
      elif f==3:
          print("Saliendo del Sistema")
          break
      else:
        print("La opcion ingresada no es valida, intente de nuevo")
    else:
      print("La entrada no es un número, intente de nuevo")
MenuPrincipal()
