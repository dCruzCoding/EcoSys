
#       ____ _                           _        __  __        ___                 ____  _             _   ____    ____  
#      / ___| | __ _ ___  ___  ___    __| | ___  |  \/  |_   _ / _ \__      ___ __ | __ )(_) ___       / | |___ \  |___ \ 
#     | |   | |/ _` / __|/ _ \/ __|  / _` |/ _ \ | |\/| | | | | | | \ \ /\ / / '_ \|  _ \| |/ _ \      | |   __) |   __) |
#     | |___| | (_| \__ \  __/\__ \ | (_| |  __/ | |  | | |_| | |_| |\ V  V /| | | | |_) | | (_) |     | |_ / __/ _ / __/ 
#      \____|_|\__,_|___/\___||___/  \__,_|\___| |_|  |_|\__, |\___/  \_/\_/ |_| |_|____/|_|\___/      |_(_)_____(_)_____|
#                                                        |___/                                                            



import random

# ---------------------- Clase Estadistica ----------------------
# Se encarga de llevar un conteo TOTAL de eventos clave en la simulación

class Estadistica:
    def __init__(self):
        self.reproducciones = 0
        self.conflictos = 0
        self.muertes = 0

    def sumar_reproduccion(self):
        self.reproducciones += 1

    def sumar_conflicto(self, cantidad):
        self.conflictos += cantidad

    def sumar_muerte(self, cantidad):
        self.muertes += cantidad

    def obtener_totales(self):
        return self.reproducciones, self.conflictos, self.muertes



# ---------------------- Clase Individuo ----------------------
# Representa un 'ser' dentro de la simulación

class Individuo:
    def __init__(self, x, y, age=0, is_child=False, turnos_hijo=0):
        self.x = x  # Posicion X
        self.y = y  # Posiciion Y
        self.age = age  # Edad del individuo
        self.is_child = is_child  # Para distinguir si es un individuo hijo
        self.turnos_hijo = turnos_hijo  # Cuántos turnos lleva como hijo

    def move(self, grid_width, grid_height):
        """ Mueve al individuo en una dirección aleatoria dentro de la cuadrícula """
        movimientos = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                       (0, 1), (1, -1), (1, 0), (1, 1)]
        dx, dy = random.choice(movimientos)
        self.x = (self.x + dx) % grid_width
        self.y = (self.y + dy) % grid_height

    def es_rosa(self):
        """ Devuelve True si el individuo sigue en estado de niño (rosa) """
        return self.turnos_hijo > 0

    def crecer(self):
        """ Revisa el estado de niño hasta para convertirlo en adulto cuando pasen los turnos necesarios """
        if self.es_rosa():
            self.turnos_hijo -= 1
        elif self.turnos_hijo == 0 and self.is_child:
            self.is_child = False   # Se convierte en adulto si pasó el tiempo de hijo