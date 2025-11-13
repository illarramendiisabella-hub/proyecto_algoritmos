from ingrediente import Ingrediente, Ingrediente_longitud, Acompanante
class Hotdog:
    """
    Representa una receta específica de Hot Dog en el menú. 
    Contiene referencias a los objetos Ingrediente que la componen.
    """
    def __init__(self, nombre, precio, pan, salchicha, toppings, salsas, acompanante = None):
        self.nombre = nombre
        self.precio = precio
        self.pan = pan
        self.salchicha = salchicha
        self.toppings = toppings  
        self.salsas = salsas      
        self.acompanante = acompanante

    def ingredientes_totales(self):
        """
        Devuelve una lista con todos los ingredientes usados en el hot dog.
        """
        ingredientes = [self.pan, self.salchicha] + self.toppings + self.salsas
        if self.acompanante:
            ingredientes.append(self.acompanante)
        return ingredientes
