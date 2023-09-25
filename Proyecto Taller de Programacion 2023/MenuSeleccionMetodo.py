import pandas as pd
import numpy as np

from Despliegue import Despliegue
from MetodoLineaRecta import MetodoLineaRecta
from MetodoSumaDigitos import SumaDigitos


def Metodos(B,VS,n,Categoria,FechaCompra,Moneda,DetalleActivo,NumActivo):
    
    #Estos son para que los parametros que recibe metodos desde funcion_1 sean 'locales' dentro de metodos y puedan utilizarse en los metodos
    B = B
    VS = VS
    n = n
    Categoria = Categoria
    FechaCompra = FechaCompra
    Moneda = Moneda
    DetalleActivo = DetalleActivo
    NumActivo = NumActivo
    fecha_compra_especifica = FechaCompra
    añoCompra = int(FechaCompra.split("/")[2])
   
    

    while True:
        metodos=input("Ingrese el metodo que le gustaria elegir para calcular depreciacion \n1.Metodo Linea Recta\n2.Metodo Suma Digitos\n")
        if metodos.isdigit():
            metodos=int(metodos)
            if metodos==1:

                #DESCRIBE EL ACTIVO
                Despliegue(B,VS,n,Categoria,FechaCompra,Moneda,DetalleActivo,NumActivo,añoCompra)

                #Variables para tabular MetodoLineaRecta
                tasa_depreciacion = 1/n
                depreciacion_init = (B-VS)/n
                print(MetodoLineaRecta(añoCompra,n,depreciacion_init,tasa_depreciacion,B))
                break 

            elif metodos==2:

                
                #Variables para tabular SumaDigitos
                depreciacion_init = (B-VS)/n
                vidaUtil = n*(n+1)/2

                #DESCRIBE EL ACTIVO
                Despliegue(B,VS,n,Categoria,FechaCompra,Moneda,DetalleActivo,NumActivo,añoCompra)
                print("VIDA UTIL DEL ACTIVO = ", vidaUtil)

                print(SumaDigitos(B,VS,n,añoCompra,vidaUtil))
                break

            else:
                print("La opcion introducida no es valida, intente de nuevo")

