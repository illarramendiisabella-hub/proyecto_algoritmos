"""
Módulo de la Clase GestorDatos

Define la clase GestorDatos para manejar la persistencia del sistema:
1. Descarga de datos base desde el API de GitHub (usando requests).
2. Carga y guardado de datos locales en datos_locales.json.
"""
import requests
import json 

class GestorDatos:
    """
    Clase para manejar la carga de datos desde GitHub y desde archivos locales.
    """

    def __init__(self):
        self.url_api = "https://raw.githubusercontent.com/FernandoSapient/BPTSP05_2526-1/main/data.json"
        self.archivo_local = "data/local_data.json"

    def cargar_desde_api(self):
        """
        Descarga los datos JSON desde el repositorio de GitHub.
        """
        try:
            response = requests.get(self.url_api)
            if response.status_code == 200:
                print("Datos descargados desde GitHub.")
                return response.json()
            else:
                print("Error al descargar datos desde GitHub.")
                return []
        except Exception as e:
            print("Error de conexión:", e)
            return []

  def cargar_local(self):
        """
        Carga los datos locales guardados por el usuario.
        """
        try:
            with open(self.archivo_local, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            print("Archivo local no encontrado. Se usará solo la API.")
            return []

    def guardar_local(self, datos):
        """
        Guarda los datos nuevos en el archivo local.
        """
        with open(self.archivo_local, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)
