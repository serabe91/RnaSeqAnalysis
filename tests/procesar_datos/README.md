Al ejecutar la función de la siguiente manera como ejemplo: 
```python
# Nombre del archivo de entrada con los datos brutos
archivo = "GSE133979_rawcounts_NCBI.tsv"

# Ejecutar la función de preprocesamiento
df_preprocesado = procesar_datos(archivo, umbral_expresion=5)
```
Teniendo en cuenta la documentación en la sección docs, tendremos como salida el archivo esperado que se encuentra adjunto con los datos de la matriz preprocesados.
