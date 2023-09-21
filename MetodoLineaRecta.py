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