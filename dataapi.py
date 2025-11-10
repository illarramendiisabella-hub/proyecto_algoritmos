"""
Módulo de la Clase GestorDatos

Define la clase GestorDatos para manejar la persistencia del sistema:
1. Descarga de datos base desde el API de GitHub (usando requests).
2. Carga y guardado de datos locales en datos_locales.json.
"""
import requests
import json 
