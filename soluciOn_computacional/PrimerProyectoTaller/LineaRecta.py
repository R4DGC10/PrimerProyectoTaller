#Librerias
import pandas as pd
import datetime as dt
#Modulos
from Abrir_html import aperturaHTML
from Validar_Codigo import validarCodigo



def lineaRectaAnual():

    #Variables a utilizar en metodo Linea Recta para Depreciacion Anual
    activo = validarCodigo()
    df = aperturaHTML()
    detalleActivo = df.iloc[activo, 2]
    print("\n")
    print("[ACTIVO A CONSULTAR]: ", detalleActivo)
    valorInicial = int(df.iloc[activo, 3])
    valorSalvamiento = int(df.iloc[activo, 6])
    periodoRecuperacion = int(df.iloc[activo, 7])
    numeroActivo = int(df.iloc[activo, 0])
    categoria = df.iloc[activo, 1]
    fechaCompra = df.iloc[activo, 4]
    moneda = df.iloc[activo, 5]
    fechaCompraObj = dt.datetime.strptime(fechaCompra, "%d/%m/%Y")
    año =fechaCompraObj.year+1
    periodo=1

    if periodoRecuperacion == 0:
        print("EL ACTIVO: ", detalleActivo, "NO ES SUJETO A DEPRECIACION \n Vuelva a Intentar con otro activo\n") 
        lineaRectaAnual()
        

    else:
        data = []
        valorEnLibros = valorInicial
        while periodo <= periodoRecuperacion:
            depreciacionAnual = (valorInicial - valorSalvamiento) / periodoRecuperacion
            valorEnLibros -= depreciacionAnual
            tasa= 1/periodoRecuperacion

            data.append({
                'AÑO': año,
                'PERIODO': periodo,
                'DEPRECIACION ANUAL': depreciacionAnual,
                'TASA DE DEPRECIACION': tasa,
                'VALOR EN LIBROS': valorEnLibros
            })
            año += 1  
            periodo +=1
        
        dfResultado = pd.DataFrame(data)

        #REDONDEA LOS RESULTADOS
        dfResultado['DEPRECIACION ANUAL'] = dfResultado['DEPRECIACION ANUAL'].round(2)
        dfResultado['TASA DE DEPRECIACION'] = dfResultado['TASA DE DEPRECIACION'].round(2)
        dfResultado['VALOR EN LIBROS'] = dfResultado['VALOR EN LIBROS'].round(2)

        print("")
        print("Identificador:        ", numeroActivo)
        print("categoria:            ", categoria)
        print("Detalle:              ", detalleActivo)
        print("Valor Inicial:        ", valorInicial)
        print("Fecha de Compra:      ", fechaCompra)
        print("moneda:               ", moneda)
        print("Valor Salvamento:     ", valorSalvamiento)
        print("Periodo de Recuperacion:         ", periodoRecuperacion)
        print("============================= Tabla de Proyeccion: Metodo Lineal =============================")
        print(dfResultado)


def lineaRectaHastaLaFecha():

    #Variables a utilizar en metodo Linea Recta para Depreciacion Anual
    activo = validarCodigo()
    df = aperturaHTML()
    detalleActivo = df.iloc[activo, 2]
    print("\n")
    print("[ACTIVO A CONSULTAR]: ", detalleActivo)
    valorInicial = int(df.iloc[activo, 3])
    valorSalvamiento = int(df.iloc[activo, 6])
    numeroActivo = int(df.iloc[activo, 0])
    categoria = df.iloc[activo, 1]
    fechaCompraStr = df.iloc[activo, 4]
    fechaCompra = dt.datetime.strptime(fechaCompraStr, "%d/%m/%Y")
    periodoRecuperacion = dt.datetime.now().year-fechaCompra.year
    periodoRecuperacionOriginal=int(df.iloc[activo, 7])
    moneda = df.iloc[activo, 5]
    año = fechaCompra.year+1


    if periodoRecuperacionOriginal == 0:
        print("EL ACTIVO: ", detalleActivo, "NO ES SUJETO A DEPRECIACION \n Vuelva a Intentar con otro activo") 
        lineaRectaHastaLaFecha()

    else:
        data = []
        valorEnLibros = valorInicial
        periodo = 1 
        while periodo <= periodoRecuperacion:
            depreciacionAnual = (valorInicial - valorSalvamiento) / periodoRecuperacion
            tasa= 1/periodoRecuperacion
            valorEnLibros -= depreciacionAnual
            data.append({
                'AÑO': año,
                'DEPRECIACION ANUAL': depreciacionAnual,
                'TASA DE DEPRECIACION': tasa,
                'VALOR EN LIBROS': valorEnLibros
            })
            año += 1
            periodo += 1  

        dfResultado = pd.DataFrame(data)

        #REDONDEA LOS RESULTADOS
        dfResultado['DEPRECIACION ANUAL'] = dfResultado['DEPRECIACION ANUAL'].round(2)
        dfResultado['TASA DE DEPRECIACION'] = dfResultado['TASA DE DEPRECIACION'].round(2)
        dfResultado['VALOR EN LIBROS'] = dfResultado['VALOR EN LIBROS'].round(2)


        
        print("")
        print("Identificador:        ", numeroActivo)
        print("categoria:            ", categoria)
        print("Detalle:              ", detalleActivo)
        print("Valor Inicial:        ", valorInicial)
        print("Fecha de Compra:      ", fechaCompra)
        print("moneda:               ", moneda)
        print("Valor Salvamento:     ", valorSalvamiento)
        print("Periodo de Recuperacion:         ", periodoRecuperacion)
        print("============================= Tabla de Proyeccion: Metodo Lineal hasta Fecha Actual=============================")
        print(dfResultado)

