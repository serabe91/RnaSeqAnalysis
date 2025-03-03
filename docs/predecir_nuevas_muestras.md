# `predecir_nuevas_muestras`

### Descripción
Este módulo permite utilizar un modelo de clasificación entrenado (Regresión Logística o KNN) para predecir nuevas muestras. Si las muestras incluyen etiquetas reales, también calcula la precisión del modelo y muestra métricas de evaluación.

### Dependencias
Este módulo requiere las siguientes bibliotecas:
- `pandas`
- `matplotlib.pyplot`
- `seaborn`
- `sklearn.metrics`

### Uso
```python
from predecir_nuevas_muestras import predecir_nuevas_muestras
modelo = ...  # Cargar modelo entrenado
resultados = predecir_nuevas_muestras("nuevas_muestras.csv", modelo, modelo_tipo="logistic")
```

### Parámetros
- `archivo_nuevas_muestras` (str): Ruta del CSV con las nuevas muestras (genes en columnas, muestras en filas).
- `modelo`: Modelo entrenado (Regresión Logística o KNN).
- `modelo_tipo` (str, opcional): Tipo de modelo utilizado ("logistic" o "knn"). Valor por defecto: "logistic".
- `columna_etiqueta` (str, opcional): Nombre de la columna con las etiquetas reales. Si no se proporciona, no se calcularán las métricas de evaluación.

### Retorno
- `DataFrame`: DataFrame con las predicciones y métricas de evaluación (si hay etiquetas reales).

### Salida y Visualizaciones
- Se imprimen las predicciones en consola.
- Si hay etiquetas reales, se muestra:
  - Precisión del modelo.
  - Reporte de clasificación (`precision`, `recall`, `f1-score`).
  - Matriz de confusión (gráfico de calor `seaborn`).
  - Distribución de predicciones (gráfico de barras `seaborn`).
  - Histograma de probabilidades si el modelo es de Regresión Logística.

### Ejemplo de Uso con Evaluación
```python
modelo_entrenado = ...  # Cargar modelo entrenado
resultados = predecir_nuevas_muestras("nuevas_muestras.csv", modelo_entrenado, modelo_tipo="logistic", columna_etiqueta="Etiqueta_Real")
```

### Notas
- Para modelos KNN, no se generará la distribución de probabilidades, ya que este método no calcula `predict_proba`.
- Si las muestras nuevas no tienen etiquetas, el script solo devolverá las predicciones sin métricas de evaluación.
- Esta función del paquete debe ser ejecutada en el mismo script que `clasificar_condicion`, ya que el modelo no es descargado en un directorio sino que es guardado en memoria para su uso inmediato.
