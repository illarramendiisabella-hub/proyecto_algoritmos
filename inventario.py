"""
Módulo de la Clase Inventario

Define la clase Inventario, gestora de existencias de todos los ingredientes. 
Incluye los métodos para actualizar stock, verificar disponibilidad para una venta 
y mantener la lista de ingredientes.
"""

from ingrediente import Ingrediente, Ingrediente_tamano, Acompanante

class Inventario:
    """
    Clase gestora del Inventario. Mantiene el stock (cantidad) de cada ingrediente 
    y la lista maestra de todos los objetos Ingrediente registrados.
    """
    def __init__(self):
        self.ingredientes: Dict[str, Ingrediente] = {}
        self.stock: Dict[str, int] = {}
        self.ingredientes_nuevos: List[str] = []