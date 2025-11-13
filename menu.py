from hotdog import Hotdog
from inventario import Inventario

class GestorMenu:
    """
    Administra los hot dogs del menú.
    """
    def __init__(self):
        self.hotdogs = []  # lista de HotDog

    def listar_hotdogs(self):
        """
        Muestra todos los hot dogs registrados.
        """
        if not self.hotdogs:
            print("No hay hot dogs en el menú.")
        else:
            for hd in self.hotdogs:
                print(f"- {hd.nombre}")
                
    def verificar_inventario(self, hotdog, inventario):
        """
        Verifica si hay suficiente inventario para preparar el hot dog.
        Parámetros:
            hotdog (HotDog): Hot dog a verificar.
            inventario (Inventario): Inventario actual.
        Retorna:
            bool: True si hay suficiente inventario, False si falta algo.
        """
        for ingrediente in hotdog.ingredientes_totales():
            if inventario.stock.get(ingrediente, 0) <= 0:
                print(f"No hay suficiente de '{ingrediente}'")
                return False
        return True

    def agregar_hotdog(self, hotdog, gestor_ingredientes, inventario):
        """
        Agrega un nuevo hot dog al menú, validando ingredientes y longitudes.

        Parámetros:
            hotdog (HotDog): Hot dog a agregar.
            gestor_ingredientes (GestorIngredientes): Para validar ingredientes.
            inventario (Inventario): Para advertir si falta algo.
        """
        # Validar que todos los ingredientes existan
        nombres_validos = [ing.nombre for ing in gestor_ingredientes.ingredientes]
        for ing in hotdog.ingredientes_totales():
            if ing not in nombres_validos:
                print(f"Ingrediente '{ing}' no está registrado.")
                return

        # Validar longitud pan y salchicha (simulado por coincidencia de tipo)
        pan = next((i for i in gestor_ingredientes.ingredientes if i.nombre == hotdog.pan), None)
        sal = next((i for i in gestor_ingredientes.ingredientes if i.nombre == hotdog.salchicha), None)
        if pan and sal and pan.tipo != sal.tipo:
            print("⚠️ El pan y la salchicha tienen longitudes diferentes.")
            confirmar = input("¿Deseas continuar de todos modos? (s/n): ")
            if confirmar.lower() != "s":
                print("Hot dog no agregado.")
                return
                
        # Advertir si falta inventario
        for ing in hotdog.ingredientes_totales():
            if inventario.stock.get(ing, 0) <= 0:
                print(f"⚠️ No hay inventario de '{ing}'.")

        self.hotdogs.append(hotdog)
        print(f"Hot dog '{hotdog.nombre}' agregado al menú.")

    def eliminar_hotdog(self, nombre, inventario):
        """
        Elimina un hot dog del menú, confirmando si aún hay inventario.
        Parámetros:
            nombre (str): Nombre del hot dog a eliminar.
            inventario (Inventario): Para verificar si aún puede venderse.
        """
        for hd in self.hotdogs:
            if hd.nombre == nombre:
                puede_venderse = self.verificar_inventario(hd, inventario)
                if puede_venderse:
                    confirmar = input(f"'{nombre}' aún puede venderse. ¿Eliminarlo igual? (s/n): ")
                    if confirmar.lower() != "s":
                        print("No se eliminó nada.")
                        return
                self.hotdogs.remove(hd)
                print(f"Hot dog '{nombre}' eliminado.")
                return
        print(f"No se encontró el hot dog '{nombre}'.")

     def ingredientes_en_uso(self):
        """
        Devuelve un conjunto con todos los ingredientes usados en el menú.
        """
        usados = set()
        for hd in self.hotdogs:
            usados.update(hd.ingredientes_totales())
        return usados

     def eliminar_hotdogs_con_ingrediente(self, nombre_ingrediente):
        """
        Elimina todos los hot dogs que usan un ingrediente específico.

        Parámetros:
            nombre_ingrediente (str): Ingrediente a buscar.
        """
        self.hotdogs = [hd for hd in self.hotdogs if nombre_ingrediente not in hd.ingredientes_totales()]
        print(f"Se eliminaron los hot dogs que usaban '{nombre_ingrediente}'.")
