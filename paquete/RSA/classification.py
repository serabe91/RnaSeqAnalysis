import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve, auc
import seaborn as sns
import matplotlib.pyplot as plt


def clasificar_condicion(archivo_preprocesado, target_column, rango_positivo, modelo_tipo="logistic", test_size=0.2,
                         random_state=42, n_neighbors=5):
    """
    Entrena un modelo de clasificación (Regresión Logística o KNN) para predecir una condición biológica.
    """
    # Cargar el archivo CSV
    df = pd.read_csv(archivo_preprocesado, index_col=0)
    df = df.T  # Transponer la matriz
    df[target_column] = 0  # Crear la columna de etiquetas
    inicio, fin = rango_positivo
    df.iloc[inicio:fin, -1] = 1  # Etiquetar muestras positivas

    # Separar características y etiquetas
    X = df.drop(columns=[target_column])
    y = df[target_column]

    # División de datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    # Información sobre los datos
    print(f"\n Dataset: {len(y)} muestras")
    print(f" Train: {len(y_train)}, Test: {len(y_test)}")
    print("\n Distribución de clases:")
    print("Train:", y_train.value_counts(normalize=True).to_dict())
    print("Test:", y_test.value_counts(normalize=True).to_dict())

    # Seleccionar modelo
    if modelo_tipo == "logistic":
        modelo = LogisticRegression(random_state=random_state, max_iter=1000)
    elif modelo_tipo == "knn":
        modelo = KNeighborsClassifier(n_neighbors=n_neighbors)
    else:
        raise ValueError(" Modelo no válido. Usa 'logistic' o 'knn'.")

    # Entrenar modelo
    modelo.fit(X_train, y_train)
    y_pred = modelo.predict(X_test)
    y_prob = modelo.predict_proba(X_test)[:, 1] if modelo_tipo == "logistic" else None

    # Evaluación del modelo
    train_score = modelo.score(X_train, y_train)
    test_score = modelo.score(X_test, y_test)
    print(f"\n Accuracy en entrenamiento: {train_score:.4f}")
    print(f" Accuracy en prueba: {test_score:.4f}")
    print("\n Reporte de clasificación:")
    print(classification_report(y_test, y_pred))

    # Matriz de Confusión
    cm = confusion_matrix(y_test, y_pred)
    print("\n Matriz de Confusión:")
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=["Negativo", "Positivo"],
                yticklabels=["Negativo", "Positivo"])
    plt.xlabel("Predicción")
    plt.ylabel("Valor Real")
    plt.title(f"Matriz de Confusión - {modelo_tipo.upper()}")
    plt.show()

    # Curva ROC (solo para Regresión Logística)
    if modelo_tipo == "logistic" and y_prob is not None:
        fpr, tpr, _ = roc_curve(y_test, y_prob)
        roc_auc = auc(fpr, tpr)
        plt.figure(figsize=(6, 4))
        plt.plot(fpr, tpr, color='blue', lw=2, label=f'AUC = {roc_auc:.2f}')
        plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
        plt.xlabel("Falsos Positivos")
        plt.ylabel("Verdaderos Positivos")
        plt.title("Curva ROC")
        plt.legend()
        plt.show()

    # Importancia de Variables (Regresión Logística)
    if modelo_tipo == "logistic":
        importancia = pd.DataFrame({"Feature": X.columns, "Coeficiente": modelo.coef_[0]})
        importancia = importancia.sort_values(by="Coeficiente", ascending=False)
        print("\n Importancia de las variables (Top 10):")
        print(importancia.head(10))


    return modelo, y_pred, y_test


# Definir el rango de muestras positivas
rango_positivo = (1, 22)  # Ajusta según tu dataset

# # Ejecutar con Regresión Logística
# modelo_log, y_pred_log, y_test_log = clasificar_condicion(
#     archivo_preprocesado="datos_preprocesados.csv",
#     target_column="condicion_biologica",
#     rango_positivo=rango_positivo,
#     modelo_tipo="logistic"
# )

# Ejecutar con KNN (k=5)
modelo_knn, y_pred_knn, y_test_knn = clasificar_condicion(
    archivo_preprocesado="datos_preprocesados.csv",
    target_column="condicion_biologica",
    rango_positivo=rango_positivo,
    modelo_tipo="knn",
    n_neighbors=5
)
