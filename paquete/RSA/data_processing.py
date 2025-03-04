import pandas as pd
import numpy as np


def procesar_datos(archivo, umbral_expresion=10):
    """
    Preprocesa datos de expresión génica para PCA.

    - Normaliza los datos a CPM.
    - Aplica transformación log2(CPM + 1).
    - Filtra genes con baja expresión.
    - Guarda la matriz preprocesada en un archivo CSV.

    Parámetros:
    - archivo: ruta del archivo CSV con los datos de expresión.
    - umbral_expresion: umbral de expresión mínima para conservar un gen.

    Retorna:
    - DataFrame preprocesado listo para PCA.
    """
    # Cargar datos
    df = pd.read_csv(archivo, index_col=0, sep = "\t")

    # Normalización por CPM (Counts Per Million)
    df_cpm = df.div(df.sum(axis=0), axis=1) * 1e6

    # Transformación log2(CPM + 1) para estabilizar varianza
    df_log = np.log2(df_cpm + 1)

    # Filtrar genes con baja expresión (opcional)
    df_filtrado = df_log[df_log.mean(axis=1) > np.log2(umbral_expresion + 1)]

    # Guardar la matriz preprocesada
    df_filtrado.to_csv("datos_preprocesados.csv")

    return df_filtrado

# Nombre del archivo de entrada con los datos brutos
archivo = "GSE133979_rawcounts_NCBI.tsv"  # Reemplázalo con el nombre real de tu archivo

# Ejecutar la función de preprocesamiento
df_preprocesado = procesar_datos(archivo, umbral_expresion=5)