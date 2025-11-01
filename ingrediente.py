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
    def __init__(self, id, nombre, categoria, precio):
        self.id = id 
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio 

    def __str__(self):
        return f"{self.categoria}, {self.nombre} Costo: {self.precio}"
    
    def a_dict(self):
        """Retorna el objeto como un diccionario para guardar en JSON."""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'categoria': self.categoria,
            'precio_costo': self.precio

class Ingrediente_tamano(Ingrediente):
    """
    Clase para ingredientes que requieren una longitud para validación (Pan y Salchicha).
    Hereda de Ingrediente.
    """
    def __init__(self, id, nombre, categoria, tamano):
        super().__init__(id, nombre, categoria)
        self.tamano = tamano

    def __str__(self):
        return f"{self.categoria} : {self.nombre} ({self.tamano}cm)"
    
class Acompanante(Ingrediente):
    """
    Hereda de Ingrediente. 
    Representa los acompañantes que pueden ser vendidos por separado o incluidos en combos.
    """
    def __init__(self, id, nombre, categoria, combo: bool = False):
        super().__init__(id, nombre, categoria)
        self.combo = combo 

    def __str__(self):
        combo = " (Combo)" if self.combo else ""
        return f"{self.categoria} {self.nombre}{combo}"
