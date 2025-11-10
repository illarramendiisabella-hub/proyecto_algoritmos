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

    def validar_longitud(self):
        return self.pan.tipo == self.salchicha.tipo
    
    def ingredientes_totales(self):
        lista = [self.pan, self.salchicha] + self.toppings + self.salsas
        if self.acompanante:
            lista.append(self.acompanante)
        return lista