#Librerias
import pandas as pd
import datetime as dt
#Modulos
from Abrir_html import aperturaHTML
from Validar_Codigo import validarCodigo




def sumarDigitosAnual():

    #Variables a utilizar en metodo Suma Digitos para Depreciacion hasta la Fecha
    activo = validarCodigo()
    df = aperturaHTML()
    DetalleActivo = df.iloc[activo, 2]
    print("\n")
    print("[ACTIVO A CONSULTAR]: ", DetalleActivo)
    valorInicial = int(df.iloc[activo, 3])
    valorSalvamento = int(df.iloc[activo, 6])
    periodoRecuperacion = int(df.iloc[activo, 7])
    numeroActivo = int(df.iloc[activo, 0])
    categoria = df.iloc[activo, 1]
    Fecha_Compra = df.iloc[activo, 4]
    moneda = df.iloc[activo, 5]
    fechaCompraObj = dt.datetime.strptime(Fecha_Compra, "%d/%m/%Y")
    año = fechaCompraObj.year+1
    depreciacionAcumulada = 0
    resultados = []
    parte2=periodoRecuperacion*(periodoRecuperacion+1)/2
    periodoOriginal=periodoRecuperacion
    periodo = 1
    #
    vidaUtil = periodoRecuperacion*(periodoRecuperacion+1)/2

    if periodoRecuperacion == 0:
        print("EL ACTIVO: ", DetalleActivo, "NO ES SUJETO A DEPRECIACION \n Vuelva a Intentar con otro activo")
        sumarDigitosAnual()


    else:
        while periodo <= periodoOriginal:
            factor = (periodoOriginal - periodo + 1) / parte2
            depreciacion_anual = factor * (valorInicial - valorSalvamento)
            depreciacionAcumulada += depreciacion_anual
            valor_neto = valorInicial - depreciacionAcumulada
            resultados.append({
                "AÑO": año,
                "PERIODO": periodo,
                "DEPRECIACION ANUAL": depreciacion_anual,
                "DEPRECIACION ACUMULADA": depreciacionAcumulada,
                "VALOR EN LIBROS": valor_neto
            })
            periodo += 1
            año += 1
            dfResultado = pd.DataFrame(resultados)

        #REDONDEA LOS RESULTADOS
        dfResultado['DEPRECIACION ANUAL'] = dfResultado['DEPRECIACION ANUAL'].round(2)
        dfResultado['DEPRECIACION ACUMULADA'] = dfResultado['DEPRECIACION ACUMULADA'].round(2)
        dfResultado['VALOR EN LIBROS'] = dfResultado['VALOR EN LIBROS'].round(2)


        print("Identificador:        ", numeroActivo)
        print("categoria:            ", categoria)
        print("Detalle:              ", DetalleActivo)
        print("Valor Inicial:        ", valorInicial)
        print("Fecha de Compra:      ", Fecha_Compra)
        print("moneda:               ", moneda)
        print("Valor Salvamento:     ", valorSalvamento)
        print("Periodo de Recuperacion: ", periodoRecuperacion)
        print("")
        print("Vida Util del activo   ", vidaUtil)
        print("============================= Tabla de Proyeccion: Metodo Suma Digitos =============================")
        print(dfResultado)


def sumarDigitosHastaLaFecha():

    #Variables a utilizar en metodo Suma Digitos para Depreciacion hasta la Fecha
    activo = validarCodigo()
    df = aperturaHTML()
    DetalleActivo = df.iloc[activo, 2]
    print("\n")
    print("[ACTIVO A CONSULTAR]: ", DetalleActivo)
    valorInicial = int(df.iloc[activo, 3])
    valorSalvamento = int(df.iloc[activo, 6])
    numeroActivo = int(df.iloc[activo, 0])
    categoria = df.iloc[activo, 1]
    fechaCompraStr = df.iloc[activo, 4]
    fechaCompra = dt.datetime.strptime(fechaCompraStr, "%d/%m/%Y")
    periodoRecuperacion = dt.datetime.now().year-fechaCompra.year
    periodoRecuperacionOriginal=int(df.iloc[activo, 7])
    moneda = df.iloc[activo, 5]
    año = fechaCompra.year+1
    depreciacionAcumulada = 0
    resultados = []
    parte2=periodoRecuperacion*(periodoRecuperacion+1)/2
    periodo = 1
    vidaUtil = periodoRecuperacion*(periodoRecuperacion+1)/2

    if periodoRecuperacionOriginal == 0:
        print("EL ACTIVO: ", DetalleActivo, "NO ES SUJETO A DEPRECIACION \n Vuelva a Intentar con otro activo")
        sumarDigitosHastaLaFecha()
    else:
        while periodo <= periodoRecuperacion:
            factor = (periodoRecuperacion - periodo + 1) / parte2
            depreciacion_anual = factor * (valorInicial - valorSalvamento)
            depreciacionAcumulada += depreciacion_anual
            valor_neto = valorInicial - depreciacionAcumulada
            resultados.append({
                "AÑO": año,
                "PERIODO": periodo,
                "DEPRECIACION ANUAL": depreciacion_anual,
                "DEPRECIACION ACUMULADA": depreciacionAcumulada,
                "VALOR EN LIBROS": valor_neto
            })
            periodo += 1
            año += 1
            dfResultado = pd.DataFrame(resultados)
        #REDONDEA LOS RESULTADOS
        dfResultado['DEPRECIACION ANUAL'] = dfResultado['DEPRECIACION ANUAL'].round(2)
        dfResultado['DEPRECIACION ACUMULADA'] = dfResultado['DEPRECIACION ACUMULADA'].round(2)
        dfResultado['VALOR EN LIBROS'] = dfResultado['VALOR EN LIBROS'].round(2)
        print("Identificador:        ", numeroActivo)
        print("categoria:            ", categoria)
        print("Detalle:              ", DetalleActivo)
        print("Valor Inicial:        ", valorInicial)
        print("Fecha de Compra:      ", fechaCompra)
        print("moneda:               ", moneda)
        print("Valor Salvamento:     ", valorSalvamento)
        print("Periodo de Recuperacion: ", periodoRecuperacion)
        print("")
        print("Vida Util del activo   ", vidaUtil)
        print("============================= Tabla de Proyeccion: Metodo Suma Digitos Hasta la Fecha=============================")
        print(dfResultado)

