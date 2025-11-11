"""
Módulo de la Clase SimuladorVentas

Define la clase SimuladorVentas, encargada de la simulación de un día de ventas 
de Hot Dogs, la verificación de inventario por orden de cliente y la generación 
del reporte final del día.
"""

import random 

class SimuladorVentas:
    def __init__(self, menu, inventario):
        """
        menu: instancia del menú de hot dogs y acompañantes
        inventario: instancia del inventario actual
        """
        self.menu = menu
        self.inventario = inventario
        self.ventas = []
        self.resultados = {
            'clientes_simulados': 0,
            'ventas_por_hotdog': {},
            'ingredientes_agotados': set(),
            'clientes_sin_servicio': 0
        }

   def simular_dia(self, num_clientes):
        """Simula la atención de num_clientes en el día."""
        self.resultados['clientes_simulados'] = num_clientes
        for _ in range(num_clientes):
            eleccion = self.menu.elegir_hotdog_random()  
            if not self.inventario.puede_preparar(eleccion):
                self.resultados['clientes_sin_servicio'] += 1
                continue
            self.inventario.consumir_ingredientes(eleccion)
            self.ventas.append(eleccion)
            self.resultados['ventas_por_hotdog'][eleccion] = self.resultados['ventas_por_hotdog'].get(eleccion, 0) + 1
            # Detectar ingredientes agotados
            for ing in eleccion.ingredientes:
                if self.inventario.consultar_cantidad(ing) == 0:
                    self.resultados['ingredientes_agotados'].add(ing)
