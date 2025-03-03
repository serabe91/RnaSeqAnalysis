# `procesar_datos`

## Descripción

Este módulo proporciona la función `procesar_datos`, que realiza el preprocesamiento de datos de expresión génica para su posterior análisis mediante Análisis de Componentes Principales (PCA). Incluye normalización, transformación logarítmica y filtrado de genes con baja expresión.

## Dependencias

Para ejecutar este módulo, se requieren las siguientes bibliotecas:

```python
import pandas as pd
import numpy as np
```

Puedes instalarlas usando:
```sh
pip install pandas numpy
```

## Funciones

### `procesar_datos(archivo, umbral_expresion=10)`

#### Descripción
Preprocesa datos de expresión génica para PCA mediante:
- **Normalización por CPM (Counts Per Million)**.
- **Transformación log2(CPM + 1)** para estabilizar la varianza.
- **Filtrado de genes** con baja expresión basado en un umbral.
- **Guardado de la matriz preprocesada** en un archivo CSV.

#### Parámetros
| Nombre            | Tipo   | Descripción |
|------------------|--------|-------------|
| `archivo`        | `str`  | Ruta del archivo CSV con los datos de expresión. |
| `umbral_expresion` | `int`  | Umbral de expresión mínima para conservar un gen (por defecto `10`). |

#### Retorno
- `pandas.DataFrame`: Matriz de datos preprocesados lista para PCA.

#### Ejemplo de Uso

```python
from mipaquete.modulo1 import procesar_datos

# Procesar datos desde un archivo CSV
resultado = procesar_datos("expresion_genica.csv", umbral_expresion=5)

# Ver las primeras filas
print(resultado.head())
```

#### Salida Esperada
```
               Muestra1   Muestra2   Muestra3
Gen1           2.345      3.123      1.987
Gen2           1.567      2.876      3.543
...
```

## Notas Adicionales
- Asegúrate de que el archivo de entrada sea un **CSV con tabulaciones (`\t`) como separador** y tenga **genes en las filas y muestras en las columnas**.
- La función **guarda automáticamente** el resultado como `datos_preprocesados.csv` en el directorio de trabajo.
- Puedes modificar el umbral de expresión según tus necesidades analíticas.

---

© 2025 - Proyecto de Análisis de Expresión Génica

