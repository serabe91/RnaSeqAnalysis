# `clasificar_condicion`

## Descripción

Este módulo proporciona la función `clasificar_condicion`, que entrena un modelo de clasificación para predecir una condición biológica en base a datos de expresión génica. Soporta dos modelos:

- **Regresión Logística**
- **K-Nearest Neighbors (KNN)**

## Dependencias

Para ejecutar este módulo, se requieren las siguientes bibliotecas:

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, roc_curve, auc
import seaborn as sns
import matplotlib.pyplot as plt
```

Puedes instalarlas usando:
```sh
pip install pandas scikit-learn seaborn matplotlib
```

## Funciones

### `clasificar_condicion(archivo_preprocesado, target_column, rango_positivo, modelo_tipo="logistic", test_size=0.2, random_state=42, n_neighbors=5)`

#### Descripción
Esta función entrena un modelo de clasificación binaria (Regresión Logística o KNN) para diferenciar entre dos condiciones biológicas en datos de expresión génica.

#### Parámetros

| Nombre             | Tipo       | Descripción |
|--------------------|-----------|-------------|
| `archivo_preprocesado` | `str`  | Ruta del archivo CSV con los datos de expresión preprocesados. |
| `target_column`    | `str`     | Nombre de la columna objetivo que representa la condición biológica. |
| `rango_positivo`   | `tuple`   | Rango de índices de muestras que pertenecen a la condición positiva (ej. `(1, 22)`). |
| `modelo_tipo`      | `str`     | Tipo de modelo a usar: `'logistic'` para Regresión Logística, `'knn'` para KNN (por defecto `'logistic'`). |
| `test_size`        | `float`   | Proporción de datos usados para prueba (por defecto `0.2`). |
| `random_state`     | `int`     | Semilla para reproducibilidad (por defecto `42`). |
| `n_neighbors`      | `int`     | Número de vecinos en KNN (por defecto `5`). |

#### Retorno
- **Modelo entrenado** (`sklearn model`)
- **Predicciones** (`numpy array`)
- **Valores reales** (`numpy array`)

#### Visualizaciones generadas
- **Matriz de Confusión**: Muestra el desempeño del clasificador.
- **Curva ROC** *(solo para Regresión Logística)*: Evalúa la calidad del modelo en clasificación binaria.
- **Importancia de variables** *(solo para Regresión Logística)*: Identifica los genes más relevantes en la predicción.

#### Ejemplo de Uso

```python
from mipaquete.clasificacion import clasificar_condicion

# Definir el rango de muestras positivas
datos = "datos_preprocesados.csv"
rango_positivo = (1, 22)

# Ejecutar con Regresión Logística
modelo_log, y_pred_log, y_test_log = clasificar_condicion(
    archivo_preprocesado=datos,
    target_column="condicion_biologica",
    rango_positivo=rango_positivo,
    modelo_tipo="logistic"
)
```

#### Salida Esperada
- **Matriz de Confusión** con la clasificación de muestras.
- **Curva ROC** mostrando el desempeño del modelo.
- **Importancia de Variables** destacando los genes más relevantes.

## Notas Adicionales
- **La matriz de expresión debe estar transpuesta**: genes en columnas y muestras en filas.
- **El modelo KNN no genera curva ROC ni importancia de variables**.
- **La Regresión Logística puede ayudar a interpretar la contribución de cada gen**.

---

© 2025 - Proyecto de Análisis de Expresión Génica

