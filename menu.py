from ingrediente import Ingrediente, Ingrediente_tamano, Acompanante
class Hotdog:
    """
    Representa una receta específica de Hot Dog en el menú. 
    Contiene referencias a los objetos Ingrediente que la componen.
    """
    def __init__(self, name, precio, pan: Ingrediente_tamano
                 , sausage: Ingrediente_tamano, toppings: list[Ingrediente], salsas: list[Ingrediente]):
        pass