import pandas as pd
from Abrir_html import apertura_html
from Validar_Codigo import validar_codigo
import datetime as dt

def SumarDigitos():
    activo = validar_codigo()
    df = apertura_html()
    DetalleActivo = df.iloc[activo, 2]
    Valor_Inicial = int(df.iloc[activo, 3])
    Valor_Salvamento = int(df.iloc[activo, 6])
    Periodo_Recuperacion = int(df.iloc[activo, 7])
    Numero_Activo = int(df.iloc[activo, 0])
    Categoria = df.iloc[activo, 1]
    Detalle = df.iloc[activo, 2]
    Fecha_Compra = df.iloc[activo, 4]
    Moneda = df.iloc[activo, 5]
    fecha_compra_obj = dt.datetime.strptime(Fecha_Compra, "%d/%m/%Y")
    año = fecha_compra_obj.year+1
    depreciacion_acumulada = 0
    resultados = []
    parte2=Periodo_Recuperacion*(Periodo_Recuperacion+1)/2
    periodo_original=Periodo_Recuperacion
    periodo = 1
    if Periodo_Recuperacion == 0:
        print("El periodo de recuperación del activo seleccionado es 0, no se puede procesar")
    else:
        while periodo <= periodo_original:
            factor = (periodo_original - periodo + 1) / parte2
            depreciacion_anual = factor * (Valor_Inicial - Valor_Salvamento)
            depreciacion_acumulada += depreciacion_anual
            valor_neto = Valor_Inicial - depreciacion_acumulada
            resultados.append({
                "Año": año,
                "Periodo": periodo,
                "Depreciación Anual": depreciacion_anual,
                "Depreciación Acumulada": depreciacion_acumulada,
                "Valor en Libros": valor_neto
            })
            periodo += 1
            año += 1
            df_resultado = pd.DataFrame(resultados)
        print("Identificador:        ", Numero_Activo)
        print("Categoria:            ", Categoria)
        print("Detalle:              ", Detalle)
        print("Valor Inicial:        ", Valor_Inicial)
        print("Fecha de Compra:      ", Fecha_Compra)
        print("Moneda:               ", Moneda)
        print("Valor Salvamento:     ", Valor_Salvamento)
        print("Periodo de Recuperacion: ", Periodo_Recuperacion)
        print("Tabla de Proyección de Depreciación Anual")
        print(df_resultado)


def SumarDigitos_Funcion2():
    activo = validar_codigo()
    df = apertura_html()
    DetalleActivo = df.iloc[activo, 2]
    Valor_Inicial = int(df.iloc[activo, 3])
    Valor_Salvamento = int(df.iloc[activo, 6])
    Numero_Activo = int(df.iloc[activo, 0])
    Categoria = df.iloc[activo, 1]
    Detalle = df.iloc[activo, 2]
    fecha_compra_str = df.iloc[activo, 4]
    fecha_compra = dt.datetime.strptime(fecha_compra_str, "%d/%m/%Y")
    Periodo_Recuperacion = dt.datetime.now().year-fecha_compra.year
    Moneda = df.iloc[activo, 5]
    año = fecha_compra.year+1
    depreciacion_acumulada = 0
    resultados = []
    parte2=Periodo_Recuperacion*(Periodo_Recuperacion+1)/2
    periodo = 1
    if Periodo_Recuperacion == 0:
        print("El periodo de recuperación del activo seleccionado es 0, no se puede procesar")
    else:
        while periodo <= Periodo_Recuperacion:
            factor = (Periodo_Recuperacion - periodo + 1) / parte2
            depreciacion_anual = factor * (Valor_Inicial - Valor_Salvamento)
            depreciacion_acumulada += depreciacion_anual
            valor_neto = Valor_Inicial - depreciacion_acumulada
            resultados.append({
                "Año": año,
                "Periodo": periodo,
                "Depreciación Anual": depreciacion_anual,
                "Depreciación Acumulada": depreciacion_acumulada,
                "Valor en Libros": valor_neto
            })
            periodo += 1
            año += 1
            df_resultado = pd.DataFrame(resultados)
        print("Identificador:        ", Numero_Activo)
        print("Categoria:            ", Categoria)
        print("Detalle:              ", Detalle)
        print("Valor Inicial:        ", Valor_Inicial)
        print("Fecha de Compra:      ", fecha_compra)
        print("Moneda:               ", Moneda)
        print("Valor Salvamento:     ", Valor_Salvamento)
        print("Periodo de Recuperacion: ", Periodo_Recuperacion)
        print("Tabla de Proyeccion de Depreciacion Anual")
        print(df_resultado)

