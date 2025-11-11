"""
Módulo de la Clase Inventario

Define la clase Inventario, gestora de existencias de todos los ingredientes. 
Incluye los métodos para actualizar stock, verificar disponibilidad para una venta 
y mantener la lista de ingredientes.
"""

from ingrediente import Ingrediente

class Inventario:
    """
    Clase gestora del Inventario. Mantiene el stock (cantidad) de cada ingrediente 
    y la lista maestra de todos los objetos Ingrediente registrados.
    """
    def __init__(self):
        self.ingredientes = {}  # {nombre: (ingredient, existencia)}

     def buscar_existencia(self, nombre):
        """
        Devuelve la cantidad disponible de un ingrediente.
        """
        return self.ingredientes.get(nombre, 0)

    def listar_existencias(self):
        """
        Muestra todas las existencias actuales.
        """
        for nombre, cantidad in self.ingredientes.items():
            print(f"{nombre}: {cantidad}")
