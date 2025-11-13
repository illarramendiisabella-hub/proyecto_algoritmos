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
        # Diccionario para guardar las cantidades de cada ingrediente
        self.stock = {}

    def mostrar_todo(self):
        """
        Muestra todos los ingredientes y sus cantidades.
        """
        if not self.stock:
            print("El inventario está vacío.")
        else:
            for nombre, cantidad in self.stock.items():
                print(f"{nombre}: {cantidad}")

    def buscar_ingrediente(self, nombre):
        """
        Muestra la cantidad disponible de un ingrediente específico.

        Parámetros:
            nombre (str): Nombre del ingrediente.
        """
        cantidad = self.stock.get(nombre)
        if cantidad is None:
            print(f"No se encontró el ingrediente '{nombre}'.")
        else:
            print(f"{nombre}: {cantidad}")

    def listar_por_categoria(self, categoria, gestor_ingredientes):
        """
        Muestra todos los ingredientes de una categoría y sus cantidades.
        Parámetros:
            categoria (str): Categoría a buscar.
            gestor_ingredientes (GestorIngredientes): Para acceder a los ingredientes registrados.
        """
        encontrados = False
        for ing in gestor_ingredientes.ingredientes:
            if ing.categoria == categoria:
                cantidad = self.stock.get(ing.nombre, 0)
                print(f"{ing.nombre}: {cantidad}")
                encontrados = True
        if not encontrados:
            print(f"No hay ingredientes registrados en la categoría '{categoria}'.")

    def actualizar_existencia(self, nombre, cantidad):
        """
        Actualiza la cantidad de un ingrediente. Si no existe, lo ignora.
        Parámetros:
            nombre (str): Nombre del ingrediente.
            cantidad (int): Nueva cantidad a establecer.
        """
        if nombre in self.stock:
            self.stock[nombre] = cantidad
            print(f"Cantidad de '{nombre}' actualizada a {cantidad}.")
        else:
            print(f"El ingrediente '{nombre}' no está en el inventario.")

    def agregar_ingrediente(self, nombre, cantidad):
        """
        Agrega una nueva entrada al inventario o suma a la existente.

        Parámetros:
            nombre (str): Nombre del ingrediente.
            cantidad (int): Cantidad a agregar.
        """
        if nombre in self.stock:
            self.stock[nombre] += cantidad
        else:
            self.stock[nombre] = cantidad
        print(f"Se agregó {cantidad} unidades de '{nombre}' al inventario.")
