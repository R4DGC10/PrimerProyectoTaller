#Librerias a utilizar
from math import * 
import pandas as pd

#Apertura de la fuente de datos.html
def abrir_html():
  ruta="C:\\Users\\cepc2\\OneDrive\\Desktop\\TEC\\2023 II Semestre\\Taller Programacion\\Primer Proyecto II Semestre\\PrimerProyectoTaller\\fuenteDeDatos.html"
  datos = pd.read_html(ruta)[0]
  print(datos)
abrir_html()

#Formulas

#Modelo de Depreciacion por Linea Recta
def LineaRecta(B,VS,n):
    Lr = (B-VS)/n
    return Lr

#Modelo de Depreciacion por Linea Recta (Valor en libros)
def LineaRectaVL(Lr, VS, n):
    i = 1
    while i<=n:
        VL = VS - i*(Lr)
        print("Valor en Libros ",i," = ",VL)
        i = i + 1

def Sumadigitos(n, B, VS):
  PrimeraEtapa=n*(n+1)/2
  while n>=1:
    SegundaEtapa = n/PrimeraEtapa
    n=n-1
    Aplicar_Formula= SegundaEtapa*(B-VS)
  return Aplicar_Formula
    


#Formar Tablas con DataFrame! 

