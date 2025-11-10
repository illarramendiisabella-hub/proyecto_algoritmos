"""
Módulo de la Clase Inventario

Define la clase Inventario, gestora de existencias de todos los ingredientes. 
Incluye los métodos para actualizar stock, verificar disponibilidad para una venta 
y mantener la lista de ingredientes.
"""

from ingrediente import Ingrediente, Ingrediente_longitud, Acompanante

class Inventario:
    """
    Clase gestora del Inventario. Mantiene el stock (cantidad) de cada ingrediente 
    y la lista maestra de todos los objetos Ingrediente registrados.
    """
    def __init__(self):
        self.ingredientes = {}  # {nombre: (ingredient, existencia)}

    def anadir_ingrediente(self, ingrediente, cantidad):
        self.ingrediente[ingrediente.nombre] = (ingrediente, cantidad)

    def eliminar_ingrediente(self, nombre):
        return self.ingredientes.pop(nombre, None)

    def actualizar_stock(self, nombre, cantidad):
        if nombre in self.ingredientes:
            ing, _ = self.ingredientes[nombre]
            self.ingredientes[nombre] = (ing, cantidad)

    def listar_por_categoria(self, categoria):
        return [ing for ing, _ in self.ingredientes.values() if ing.categoria == categoria]