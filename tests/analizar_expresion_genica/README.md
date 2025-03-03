Al ejecutar la función de la siguiente manera como ejemplo: 
```python
archivo_preprocesado = "datos_preprocesados.csv"
rango_condicion = (0,22)
rango_control = (23,33)

deg = analizar_expresion_genica(archivo_preprocesado, rango_condicion, rango_control, umbral_pvalor=0.05, umbral_logfc=0.5)
```
Teniendo en cuenta la documentación en la sección docs, tendremos como salida dos plots, uno con el PCA y otro con el Volcano Plot. 
Así como se muestra en los archivos adjuntos en esta carpeta.
