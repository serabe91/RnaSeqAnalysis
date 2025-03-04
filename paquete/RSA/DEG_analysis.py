import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.linalg import svd



def analizar_expresion_genica(archivo_preprocesado, rango_condicion, rango_control, umbral_pvalor=0.05,
                              umbral_logfc=1.0):
    """
    Realiza Análisis de Componentes Principales (PCA) y genera un Volcano Plot para visualizar genes diferencialmente expresados.

    Parámetros:
    - archivo_preprocesado: ruta del archivo CSV generado por `procesar_datos`.
    - rango_condicion: rango de columnas pertenecientes a la condición biológica.
    - rango_control: rango de columnas pertenecientes al grupo control.
    - umbral_pvalor: umbral para significancia estadística en el Volcano Plot.
    - umbral_logfc: umbral de cambio en la expresión para el Volcano Plot.

    Retorna:
    - Gráficas de PCA y Volcano Plot.
    """
    # Cargar los datos preprocesados desde el archivo
    df = pd.read_csv(archivo_preprocesado, index_col=0)

    # Seleccionar las columnas correspondientes
    muestras_condicion = df.columns[rango_condicion[0]:rango_condicion[1] + 1].tolist()
    muestras_control = df.columns[rango_control[0]:rango_control[1] + 1].tolist()

    # Extraer datos de expresión
    data = df[muestras_condicion + muestras_control].T

    # Centrar los datos
    media = np.mean(data, axis=0)
    data_centrada = data - media

    # PCA usando SVD
    U, S, Vt = svd(data_centrada, full_matrices=False)
    pca_1 = U[:, 0] * S[0]
    pca_2 = U[:, 1] * S[1]

    # Cálculo de varianza explicada
    varianza_explicada = (S ** 2) / np.sum(S ** 2)
    varianza_pc1 = varianza_explicada[0] * 100
    varianza_pc2 = varianza_explicada[1] * 100

    # Asignar colores según la condición
    colores = ['red'] * len(muestras_condicion) + ['blue'] * len(muestras_control)

    # Gráfico de PCA con colores y varianza
    plt.figure(figsize=(8, 6))
    plt.scatter(pca_1, pca_2, c=colores, alpha=0.7)
    plt.xlabel(f"Componente Principal 1 ({varianza_pc1:.2f}%)")
    plt.ylabel(f"Componente Principal 2 ({varianza_pc2:.2f}%)")
    plt.title("Análisis de Componentes Principales (PCA)")
    plt.legend(["Condición", "Control"])
    plt.show()

    # Cálculo de diferencias en expresión (logFC y p-valor)
    media_condicion = df[muestras_condicion].mean(axis=1)
    media_control = df[muestras_control].mean(axis=1)
    logFC = np.log2((media_condicion + 1) / (media_control + 1))

    pvalores = [stats.ttest_ind(df.loc[gen, muestras_condicion], df.loc[gen, muestras_control], equal_var=False).pvalue
                for gen in df.index]
    pvalores = np.array(pvalores)
    log_pvalores = -np.log10(pvalores)

    # Asignar colores según la expresión diferencial
    colores_volcano = np.array(['gray'] * len(logFC))  # Por defecto, genes no significativos en gris
    colores_volcano[(pvalores < umbral_pvalor) & (logFC > umbral_logfc)] = 'red'  # Sobreexpresados
    colores_volcano[(pvalores < umbral_pvalor) & (logFC < -umbral_logfc)] = 'blue'  # Infraexpresados

    # Volcano Plot
    plt.figure(figsize=(8, 6))
    plt.scatter(logFC, log_pvalores, color=colores_volcano, alpha=0.7)
    plt.xlabel("log2 Fold Change")
    plt.ylabel("-log10 P-valor")
    plt.title("Volcano Plot de Expresión Génica")

    # Resaltar genes significativos
    significativos = (pvalores < umbral_pvalor) & (np.abs(logFC) > umbral_logfc)
    plt.scatter(logFC[significativos], log_pvalores[significativos], color='red', alpha=0.7)

    # Etiquetar genes significativos en el plot
    for gene_id, x, y in zip(df.index[significativos], logFC[significativos], log_pvalores[significativos]):
        plt.text(x, y, gene_id, fontsize=8, ha='right', va='bottom', color='black')

    plt.axhline(-np.log10(umbral_pvalor), color='blue', linestyle='dashed', label=f'p < {umbral_pvalor}')
    plt.axvline(-umbral_logfc, color='green', linestyle='dashed', label=f'logFC < {-umbral_logfc}')
    plt.axvline(umbral_logfc, color='green', linestyle='dashed', label=f'logFC > {umbral_logfc}')
    plt.legend()
    plt.show()


archivo_preprocesado = "datos_preprocesados.csv"
rango_condicion = (0,22)
rango_control = (23,33)

deg = analizar_expresion_genica(archivo_preprocesado, rango_condicion, rango_control,
                                umbral_pvalor=0.05, umbral_logfc=0.5)