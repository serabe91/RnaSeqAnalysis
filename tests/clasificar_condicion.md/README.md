Al ejecutar la función de la siguiente manera como ejemplo: 
```python
# Definir el rango de muestras positivas
rango_positivo = (1, 22)  # Ajusta según tu dataset

# Ejecutar con Regresión Logística
modelo_log, y_pred_log, y_test_log = clasificar_condicion(
    archivo_preprocesado="datos_preprocesados.csv",
    target_column="condicion_biologica",
    rango_positivo=rango_positivo,
    modelo_tipo="logistic"
)

# Ejecutar con KNN (k=5)
modelo_knn, y_pred_knn, y_test_knn = clasificar_condicion(
    archivo_preprocesado="datos_preprocesados.csv",
    target_column="condicion_biologica",
    rango_positivo=rango_positivo,
    modelo_tipo="knn",
    n_neighbors=5
)

```
Teniendo en cuenta la documentación en la sección docs, tenemos dos opciones de modelo para la clasificación: "logístico" y "KNN". 
La salida del programa dependerá de cuál modelo se use. 
- Si se usa el modelo logístico, se obtendrán las salidas adjuntas en esta carpeta nombradas como: "ConfLog_ex" y "CurvaRocLog_ex", además de la siguiente información en consola:
```sh

 Dataset: 34 muestras
 Train: 27, Test: 7

 Distribución de clases:
Train: {1: 0.6296296296296297, 0: 0.37037037037037035}
Test: {1: 0.5714285714285714, 0: 0.42857142857142855}

 Accuracy en entrenamiento: 1.0000
 Accuracy en prueba: 0.7143

 Reporte de clasificación:
              precision    recall  f1-score   support

           0       0.67      0.67      0.67         3
           1       0.75      0.75      0.75         4

    accuracy                           0.71         7
   macro avg       0.71      0.71      0.71         7
weighted avg       0.71      0.71      0.71         7


 Matriz de Confusión:

 Importancia de las variables (Top 10):
     Feature  Coeficiente
5148      89     0.077917
24    163688     0.063527
281     6513     0.051252
3154  387066     0.050137
4709    5950     0.046532
6319  400258     0.045137
6587    5346     0.040154
2964    3107     0.039894
4530  220213     0.039448
2569    8507     0.039257
```
- Si se usa el modelo KNN, se obtendrán la salida adjunta en esta carpeta nombrada como: "ConfKNN_ex" y la siguiente información en consola:
```sh

Dataset: 34 muestras
 Train: 27, Test: 7

 Distribución de clases:
Train: {1: 0.6296296296296297, 0: 0.37037037037037035}
Test: {1: 0.5714285714285714, 0: 0.42857142857142855}

 Accuracy en entrenamiento: 0.7407
 Accuracy en prueba: 0.4286

 Reporte de clasificación:
              precision    recall  f1-score   support

           0       0.33      0.33      0.33         3
           1       0.50      0.50      0.50         4

    accuracy                           0.43         7
   macro avg       0.42      0.42      0.42         7
weighted avg       0.43      0.43      0.43         7

```
