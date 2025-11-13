import json

"""
Módulo de Clases de Ingredientes

Define la jerarquía de herencia para los diferentes tipos de ingredientes
del proyecto Hot Dog CCS: Ingrediente (base), Ingrediente_tamano 
(para Pan y Salchicha) y Acompanante.
"""

class Ingrediente:
    """
    Clase base para todos los ingredientes del sistema.
    """
    def __init__(self, id, nombre, categoria, tipo):
        self.id = id 
        self.nombre = nombre
        self.categoria = categoria
        self.tipo = tipo

    def to_dict(self):
        """Convierte el ingrediente a un diccionario para guardar en JSON."""
        return {
            "nombre": self.nombre,
            "categoria": self.categoria,
            "tipo": self.tipo
        }

    def __str__(self):
        return f"{self.categoria}, {self.nombre},  {self.tipo}"
    
class GestorIngredientes:
    """
    Administra la colección de ingredientes.
    """
    def __init__(self):
        self.ingredientes = []
        
    def cargar_desde_json(self, ruta):
        """Carga ingredientes desde un archivo JSON local."""
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    nuevo = Ingrediente(item["nombre"], item["categoria"], item["tipo"])
                    self.ingredientes.append(nuevo)
        except FileNotFoundError:
            print("No se encontró el archivo. Se iniciará con lista vacía.")

    def guardar_en_json(self, ruta):
        """Guarda los ingredientes actuales en un archivo JSON."""
        datos = [ing.to_dict() for ing in self.ingredientes]
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4)


     def agregar_ingrediente(self, nombre, categoria, tipo):
        """
        Agrega un nuevo ingrediente si no existe ya.

        Parámetros:
            nombre (str): Nombre del ingrediente.
            categoria (str): Categoría (pan, salchicha, salsa, etc.).
            tipo (str): Tipo dentro de la categoría.

        Retorna:
            bool: True si se agregó, False si ya existía.
        """
        for ing in self.ingredientes:
            if ing.nombre == nombre:
                print("Ese ingrediente ya existe.")
                return False

        nuevo = Ingrediente(nombre, categoria, tipo)
        self.ingredientes.append(nuevo)
        print("Ingrediente agregado correctamente.")
        return True

    def listar_por_categoria(self, categoria):
        """
        Muestra todos los ingredientes de una categoría.

        Parámetros:
            categoria (str): Categoría a buscar.
        """
        for ing in self.ingredientes:
            if ing.categoria == categoria:
                print(ing)

    def listar_por_tipo(self, categoria, tipo):
        """
        Muestra ingredientes de una categoría y tipo específico.

        Parámetros:
            categoria (str): Categoría a buscar.
            tipo (str): Tipo dentro de la categoría.
        """
        for ing in self.ingredientes:
            if ing.categoria == categoria and ing.tipo == tipo:
                print(ing)

    def eliminar_ingrediente(self, nombre, menu):
        """
        Elimina un ingrediente. Si está en uso en el menú, pide confirmación.

        Parámetros:
            nombre (str): Nombre del ingrediente a eliminar.
            menu (Menu): Menú actual para verificar si el ingrediente está en uso.
        """
        en_uso = menu.ingredientes_en_uso()

        if nombre in en_uso:
            print(f"El ingrediente '{nombre}' está en uso.")
            respuesta = input("¿Eliminarlo junto con los hot dogs que lo usan? (s/n): ")
            if respuesta.lower() != "s":
                print("No se eliminó nada.")
                return

            menu.eliminar_hotdogs_con_ingrediente(nombre)

        self.ingredientes = [ing for ing in self.ingredientes if ing.nombre != nombre]
        print(f"Ingrediente '{nombre}' eliminado.")

     
