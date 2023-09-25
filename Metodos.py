import pandas as pd
import numpy as np
from LineaRecta import LineaRecta
from Abrir_html import apertura_html
from Validar_Codigo import validar_codigo
from SumarDigitosProyecto import SumarDigitos
from SumarDigitosProyecto import SumarDigitos_Funcion2
from LineaRecta import LineaRecta_Funcion2



def Metodos():
    
    while True:
        metodos=input("Ingrese el metodo que le gustaria elegir para calcular depreciacion \n1.Metodo Linea Recta\n2.Metodo Suma Digitos\n")
        if metodos.isdigit():
            metodos=int(metodos)
            if metodos==1:
                Formula1=LineaRecta()
                return Formula1
                break
            elif metodos==2:
                Formula2=SumarDigitos()
                return Formula2
                break
            else:
                print("La opcion introducida no es valida, intente de nuevo")

def Metodos_Funcion2():
    
    while True:
        metodos=input("Ingrese el metodo que le gustaria elegir para calcular depreciacion \n1.Metodo Linea Recta\n2.Metodo Suma Digitos\n")
        if metodos.isdigit():
            metodos=int(metodos)
            if metodos==1:
                Formula1=LineaRecta_Funcion2()
                return Formula1
                break
            elif metodos==2:
                Formula2=SumarDigitos_Funcion2()
                return Formula2
                break
            else:
                print("La opcion introducida no es valida, intente de nuevo")


