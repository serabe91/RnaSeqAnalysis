# `analizar_expresion_genica`

## Descripción

Este módulo proporciona la función `analizar_expresion_genica`, que realiza un análisis de expresión génica utilizando:

- **Análisis de Componentes Principales (PCA)** para la exploración de datos.
- **Volcano Plot** para visualizar genes diferencialmente expresados.

## Dependencias

Para ejecutar este módulo, se requieren las siguientes bibliotecas:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.linalg import svd
```

Puedes instalarlas usando:
```sh
pip install numpy pandas matplotlib scipy
```

## Funciones

### `analizar_expresion_genica(archivo_preprocesado, rango_condicion, rango_control, umbral_pvalor=0.05, umbral_logfc=1.0)`

#### Descripción
Esta función toma un conjunto de datos de expresión génica preprocesado y realiza dos análisis principales:
1. **PCA**: Reduce la dimensionalidad de los datos y visualiza la variación en función de los principales componentes.
2. **Volcano Plot**: Evalúa diferencias en expresión génica entre dos grupos (condición y control) usando log Fold Change (logFC) y pruebas estadísticas.

#### Parámetros

| Nombre             | Tipo       | Descripción |
|--------------------|-----------|-------------|
| `archivo_preprocesado` | `str`  | Ruta del archivo CSV con datos preprocesados. |
| `rango_condicion`  | `tuple`   | Rango de columnas que pertenecen a la condición biológica (ej. `(0,4)`). |
| `rango_control`    | `tuple`   | Rango de columnas que pertenecen al grupo control (ej. `(5,9)`). |
| `umbral_pvalor`    | `float`   | Umbral de significancia estadística para el Volcano Plot (por defecto `0.05`). |
| `umbral_logfc`     | `float`   | Umbral de cambio en la expresión génica (log Fold Change) para el Volcano Plot (por defecto `1.0`). |

#### Retorno
- **Gráficos:** Se generan dos visualizaciones interactivas:
  - **PCA Plot**: Representación de las muestras en el espacio de componentes principales.
  - **Volcano Plot**: Identificación de genes diferencialmente expresados.

#### Ejemplo de Uso

```python
from mipaquete.analisis import analizar_expresion_genica

# Analizar datos de expresión génica
analizar_expresion_genica("datos_preprocesados.csv", rango_condicion=(0, 4), rango_control=(5, 9))
```

#### Salida Esperada
- Un **gráfico PCA**, donde los puntos representan muestras coloreadas según su grupo.
- Un **Volcano Plot**, donde los genes diferencialmente expresados aparecen resaltados.

## Notas Adicionales
- Asegúrate de que el archivo CSV **tenga genes en las filas y muestras en las columnas**.
- El PCA permite explorar si las muestras se agrupan según sus condiciones experimentales.
- Los genes sobreexpresados se muestran en **rojo**, los infraexpresados en **azul** y los no significativos en **gris**.

---

© 2025 - Proyecto de Análisis de Expresión Génica

