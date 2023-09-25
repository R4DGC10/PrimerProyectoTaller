import pandas as pd
from Abrir_html import apertura_html
from Validar_Codigo import validar_codigo
import datetime as dt

def LineaRecta():
    activo = validar_codigo()
    df = apertura_html()
    DetalleActivo = df.iloc[activo, 2]
    print("[ACTIVO A CONSULTAR]: ", DetalleActivo)
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
    periodo=1
    if Periodo_Recuperacion == 0:
        print("El periodo de recuperación del activo seleccionado es 0, no se puede procesar")   
    else:
        data = []
        valor_en_libros = Valor_Inicial
        while periodo <= Periodo_Recuperacion:
            depreciacion_anual = (Valor_Inicial - Valor_Salvamento) / Periodo_Recuperacion
            valor_en_libros -= depreciacion_anual
            tasa= 1/Periodo_Recuperacion
            data.append({
                'Año': año,
                'Periodo': periodo,
                'Depreciación Anual': depreciacion_anual,
                'Tasa de Depreciacion': tasa,
                'Valor en Libros': valor_en_libros
            })
            año += 1  
            periodo +=1
        df_resultado = pd.DataFrame(data)
        print("Identificador:        ", Numero_Activo)
        print("Categoria:            ", Categoria)
        print("Detalle:              ", Detalle)
        print("Valor Inicial:        ", Valor_Inicial)
        print("Fecha de Compra:      ", Fecha_Compra)
        print("Moneda:               ", Moneda)
        print("Valor Salvamento:     ", Valor_Salvamento)
        print("Periodo de Recuperacion:         ", Periodo_Recuperacion)
        print("Tabla de Proyeccion de Depreciacion Anual")
        print(df_resultado)


def LineaRecta_Funcion2():
    activo = validar_codigo()
    df = apertura_html()
    DetalleActivo = df.iloc[activo, 2]
    print("[ACTIVO A CONSULTAR]: ", DetalleActivo)
    Valor_Inicial = int(df.iloc[activo, 3])
    Valor_Salvamento = int(df.iloc[activo, 6])
    Numero_Activo = int(df.iloc[activo, 0])
    categoria = df.iloc[activo, 1]
    Detalle = df.iloc[activo, 2]
    fecha_compra_str = df.iloc[activo, 4]
    fecha_compra = dt.datetime.strptime(fecha_compra_str, "%d/%m/%Y")
    Periodo_Recuperacion = dt.datetime.now().year-fecha_compra.year
    Moneda = df.iloc[activo, 5]
    año = fecha_compra.year+1
    if Periodo_Recuperacion == 0:
        print("El periodo de recuperación del activo seleccionado es 0, no se puede procesar")
    else:
        data = []
        valor_en_libros = Valor_Inicial
        periodo = 1 
        while periodo <= Periodo_Recuperacion:
            depreciacion_anual = (Valor_Inicial - Valor_Salvamento) / Periodo_Recuperacion
            tasa= 1/Periodo_Recuperacion
            valor_en_libros -= depreciacion_anual
            data.append({
                'Año': año,
                'Depreciación Anual': depreciacion_anual,
                'Tasa de Depreciacion': tasa,
                'Valor en Libros': valor_en_libros
            })
            año += 1
            periodo += 1  
        df_resultado = pd.DataFrame(data)
        print("Identificador:        ", Numero_Activo)
        print("Categoria:            ", categoria)
        print("Detalle:              ", Detalle)
        print("Valor Inicial:        ", Valor_Inicial)
        print("Fecha de Compra:      ", fecha_compra)
        print("Moneda:               ", Moneda)
        print("Valor Salvamento:     ", Valor_Salvamento)
        print("Periodo de Recuperacion:         ", Periodo_Recuperacion)
        print("Tabla de Proyeccion de Depreciacion Anual")
        print(df_resultado)

