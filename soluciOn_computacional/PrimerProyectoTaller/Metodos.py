#Modulos
from LineaRecta import lineaRectaAnual
from SumarDigitosProyecto import sumarDigitosAnual
from SumarDigitosProyecto import sumarDigitosHastaLaFecha
from LineaRecta import lineaRectaHastaLaFecha




def metodos():
    
    while True:
        metodos=input("[Ingrese el metodo que le gustaria elegir para calcular depreciacion] \n1).Metodo Linea Recta\n2).Metodo Suma Digitos\nIngrese una opción >>  ")
        if metodos.isdigit():
            metodos=int(metodos)
            if metodos==1:
                formula1=lineaRectaAnual()
                return formula1
               
            elif metodos==2:
                formula2=sumarDigitosAnual()
                return formula2
                
            else:
                print("ADVERTENCIA: La opcion introducida no es valida, intente de nuevo\n")

def metodosFuncion2():
    
    while True:
        metodos=input("[Ingrese el metodo que le gustaria elegir para calcular depreciacion] \n1.Metodo Linea Recta\n2.Metodo Suma Digitos\nIngrese una opción >>  ")
        if metodos.isdigit():
            metodos=int(metodos)
            if metodos==1:
                formula1=lineaRectaHastaLaFecha()
                return formula1
                
            elif metodos==2:
                formula2=sumarDigitosHastaLaFecha()
                return formula2
                
            else:
                print("ADVERTENCIA: La opcion introducida no es valida, intente de nuevo\n")


