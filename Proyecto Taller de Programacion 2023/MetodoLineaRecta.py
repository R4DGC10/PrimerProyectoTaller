import pandas as pd
import numpy as np



#B,añoCompra,VS,n,vidaUtil,depreciacion_init



def MetodoLineaRecta(añoCompra,n,depreciacion_init,tasa_depreciacion,B):
    print("\n ", depreciacion_init, "durante ",n, " años")
    print("")
    print("========================= Proyeccion Anual mediante Metodo: Lineal =========================")
    AÑO = list(range(añoCompra+1, añoCompra+n+1))
    PERIODO = list(range(1, n+1))
    DEPRECIACION = [depreciacion_init] * n
    TASA_DEPRECIACION = [tasa_depreciacion] * n
    VALORLIBROS = [B - (n * depreciacion_init) for n in PERIODO]

    tabulado_LR = pd.DataFrame({
        'AÑOS': AÑO,
        'PERIODO': PERIODO,
        'DEPRECIACION': DEPRECIACION,
        'TASA_DEPRECIACION': TASA_DEPRECIACION,
        'VALOR EN LIBROS': VALORLIBROS
    })

    return tabulado_LR
