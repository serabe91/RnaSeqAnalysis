# __init__.py

# Importar funciones clave para que estén accesibles al importar el paquete
from .procesar_datos import procesar_datos
from .analizar_expresion import analizar_expresion_genica
from .clasificar_condicion import clasificar_condicion
from .predecir_nuevas import predecir_nuevas_muestras

# Qué funciones se exponen al importar el paquete
__all__ = [
    "procesar_datos",
    "analizar_expresion_genica",
    "clasificar_condicion",
    "predecir_nuevas_muestras",
]

# Metadatos del paquete
__version__ = "1.0.0"
__authors__ = "Sergio A. & Esteban G."
__emails__ = "sabello@unal.edu.co & esgarciap@unal.edu.co"
__license__ = "MIT"

