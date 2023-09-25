import pandas as pd
import numpy as np

# B = 7689300
# añoCompra = 2019
# VS = 450000
# n = 6
# vidaUtil = 21
# depreciacion_init = (7689300-450000)/6
# tasa_depreciacion = 1/n




def SumaDigitos(B,VS,n,añoCompra,vidaUtil):
    print("")
    print("========================= Proyeccion Anual mediante Metodo: Suma Digitos =========================")
    AÑO = list(range(añoCompra+1, añoCompra+n+1))
    PERIODO = list(range(1, n+1))
    DEPRECIACION_ANUAL = []
    DEPRECIACION_ACUMULADA = []
   

    Dep_acum = 0

    i = 1
    n_original = n  # Guarda el valor original de n
    while i <= n_original:
        Fraccion = n / vidaUtil
        Dep_Anual = Fraccion * (B-VS)
        DEPRECIACION_ANUAL.append(Dep_Anual)
        
        Dep_acum = Dep_acum + Dep_Anual
        DEPRECIACION_ACUMULADA.append(Dep_acum)

        n = n-1
        i = i+1

    
    VALORLIBROS = [B - Dep_acum for Dep_acum in DEPRECIACION_ACUMULADA]

    
    tabulado_SD = pd.DataFrame({
        'AÑOS': AÑO,
        'PERIODO': PERIODO,
        'DEPRECIACION ANUAL': DEPRECIACION_ANUAL,
        'DEPRECIACION ACUMULADA': DEPRECIACION_ACUMULADA,
        'VALOR EN LIBROS': VALORLIBROS
    })

    # Aplica round() a las columnas numéricas para redondear a 2 decimales
    tabulado_SD['DEPRECIACION ANUAL'] = tabulado_SD['DEPRECIACION ANUAL'].round(2)
    tabulado_SD['DEPRECIACION ACUMULADA'] = tabulado_SD['DEPRECIACION ACUMULADA'].round(2)
    tabulado_SD['VALOR EN LIBROS'] = tabulado_SD['VALOR EN LIBROS'].round(2)


    return tabulado_SD
