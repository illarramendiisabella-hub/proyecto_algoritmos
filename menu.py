from hotdog import Hotdog
class GestorMenu:
    """
    Administra los hot dogs del menú.
    """
    def __init__(self):
        self.menu = []  # lista de HotDog

    def agregar_hotdog(self, nombre, ingredientes, longitud_pan, longitud_salchicha, acompanante):
        if longitud_pan != longitud_salchicha:
            confirmar = input("Longitud del pan y la salchicha no coinciden. ¿Continuar? (s/n): ")
            if confirmar.lower() != "s":
                print("No se agregó el hot dog.")
                return
        self.menu.append(HotDog(nombre, ingredientes, longitud_pan, longitud_salchicha, acompanante))