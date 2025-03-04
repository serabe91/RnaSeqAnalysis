import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def predecir_nuevas_muestras(archivo_nuevas_muestras, modelo, modelo_tipo="logistic", columna_etiqueta="Etiqueta_Real"):
    """
    Usa un modelo entrenado para predecir nuevas muestras y evalúa la precisión si hay etiquetas reales.

    Parámetros:
    - archivo_nuevas_muestras: str, ruta del CSV con las nuevas muestras (genes en columnas, muestras en filas).
    - modelo: Modelo entrenado (Regresión Logística o KNN).
    - modelo_tipo: str, "logistic" o "knn", indicando el tipo de modelo usado.
    - columna_etiqueta: str, nombre de la columna con las etiquetas reales (opcional).

    Retorna:
    - DataFrame con predicciones y métricas de evaluación si hay etiquetas reales.
    """
    # Cargar las nuevas muestras
    df_nuevas = pd.read_csv(archivo_nuevas_muestras, index_col=0)

    # Verificar si el archivo tiene etiquetas reales
    if columna_etiqueta in df_nuevas.columns:
        y_real = df_nuevas[columna_etiqueta]  # Guardar etiquetas reales
        df_nuevas = df_nuevas.drop(columns=[columna_etiqueta])  # Eliminar la columna antes de predecir
    else:
        y_real = None  # Si no hay etiquetas, no se puede evaluar el modelo

    # Hacer predicciones
    y_pred = modelo.predict(df_nuevas)

    # Si el modelo es Regresión Logística, obtener probabilidades
    if modelo_tipo == "logistic":
        y_prob = modelo.predict_proba(df_nuevas)[:, 1]
    else:
        y_prob = None  # KNN no da probabilidades de pertenencia

    # Crear DataFrame con resultados
    resultados = df_nuevas.copy()
    resultados["Predicción"] = y_pred
    if y_real is not None:
        resultados["Etiqueta Real"] = y_real  # Agregar etiquetas reales para comparación
    if y_prob is not None:
        resultados["Probabilidad (Positivo)"] = y_prob

    # Mostrar resultados en consola
    print("\n Predicciones para nuevas muestras:")
    print(resultados[["Predicción"]])

    # Evaluación si hay etiquetas reales
    if y_real is not None:
        accuracy = accuracy_score(y_real, y_pred)
        print(f"\n Precisión del modelo en nuevas muestras: {accuracy:.4f}\n")
        print(" Reporte de clasificación:")
        print(classification_report(y_real, y_pred))

        # 📌 Matriz de Confusión
        cm = confusion_matrix(y_real, y_pred)
        plt.figure(figsize=(6, 4))
        sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Negativo", "Positivo"], yticklabels=["Negativo", "Positivo"])
        plt.xlabel("Predicción")
        plt.ylabel("Valor Real")
        plt.title("Matriz de Confusión - Nuevas Muestras")
        plt.show()

    # Gráfico de barras de las predicciones
    plt.figure(figsize=(8, 5))
    sns.countplot(x=y_pred, palette="coolwarm")
    plt.xticks([0, 1], ["Negativo", "Positivo"])
    plt.xlabel("Clase Predicha")
    plt.ylabel("Cantidad de Muestras")
    plt.title("Distribución de Predicciones")
    plt.show()

    # Histograma de probabilidades (si aplica)
    if y_prob is not None:
        plt.figure(figsize=(8, 5))
        sns.histplot(y_prob, bins=10, kde=True, color='blue')
        plt.xlabel("Probabilidad de ser Positivo")
        plt.ylabel("Frecuencia")
        plt.title("Distribución de Probabilidades (Regresión Logística)")
        plt.show()

    return resultados
