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

    def __str__(self):
        return f"{self.categoria}, {self.nombre},  {self.tipo}"
    
class GestorIngredientes:
    """
    Administra la colección de ingredientes.
    """
    def __init__(self):
        self.ingredientes = []

    def agregar(self, nombre, categoria, tipo):
        # Verifica si el ingrediente ya existe
        for ingrediente in self.ingredientes:
            if ingrediente.nombre == nombre and ingrediente.categoria == categoria and ingrediente.tipo == tipo:
                print("Ese ingrediente ya existe.")
                return
        nuevo = Ingrediente(nombre, categoria, tipo)
        self.ingredientes.append(nuevo)
        print(f"Ingrediente '{nombre}' {tipo} agregado a la categoría '{categoria}'.")

    def eliminar(self, nombre, categoria, tipo):
        encontrado = False
        nuevos_ingredientes = []
        for ingrediente in self.ingredientes:
            if ingrediente.nombre == nombre and ingrediente.categoria == categoria and ingrediente.tipo == tipo:
            encontrado = True
            else:
            nuevos_ingredientes.append(ing)
        if encontrado:
            self.ingredientes = nuevos_ingredientes
            print(f"Ingrediente '{nombre}' {tipo} eliminado de la categoría '{categoria}'.")
        else:
            print("El ingrediente no fue encontrado.")
              
    def listar(self, categoria):
        print(f"Ingredientes en la categoría '{categoria}':")
        for ingrediente in self.ingredientes:
            if ingrediente.categoria == categoria:
                print(f"{ingrediente.nombre} {ingrediente.tipo}")
