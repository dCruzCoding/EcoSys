import random

# ---------------------- Clase Configuración ----------------------
# Gestiona información referente a la configuración básica de los tamaños en la simulación (dimensiones y límite de individuos)
class Config:
    def __init__(self, size):
        # Definir el tamaño de la cuadrícula y el límite máximo de individuos
        if size == "pequeño":
            self.grid_width = 15
            self.grid_height = 15
            self.max_individuals = 50  # Límite para tamaño pequeño
        elif size == "medio":
            self.grid_width = 20
            self.grid_height = 20
            self.max_individuals = 100  # Límite para tamaño medio
        elif size == "grande":
            self.grid_width = 25
            self.grid_height = 25
            self.max_individuals = 150  # Límite para tamaño grande

        # Tamaño de cada celda y dimensiones de la pantalla
        self.cell_size = 30
        self.screen_width = self.grid_width * self.cell_size
        self.screen_height = self.grid_height * self.cell_size


# ---------------------- Clase Estadistica ----------------------
# Se encarga de llevar un conteo TOTAL de eventos clave en la simulación
class Stats:
    def __init__(self):
        self.reproductions = 0
        self.conflicts = 0
        self.deaths = 0

    def add_reproduction(self):
        self.reproductions += 1

    def add_conflict(self, quantity):
        self.conflicts += quantity

    def add_death(self, quantity):
        self.deaths += quantity

    def get_totals(self):
        return self.reproductions, self.conflicts, self.deaths


# ---------------------- Clase Individuo  ----------------------
# Representa un 'ser' dentro del sistema
class Individual:
    def __init__(self, x, y, age=0, is_child=False, nature=None):
        self.x = x  # Posicion X
        self.y = y  # Posiciion Y
        self.age = age  # Edad del individuo
        self.is_child = is_child  # Para distinguir si es un individuo hijo
        self.nature = nature if nature else self.assign_nature()  # Solo asigna si no se proporciona

    def move(self, grid_width, grid_height):   # que le pase estos argumentos para no tener q ponerlo aqui
        """ Mueve al individuo en una dirección aleatoria dentro de la cuadrícula """
        movements = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                       (0, 1), (1, -1), (1, 0), (1, 1)]
        dx, dy = random.choice(movements)
        self.x = (self.x + dx) % grid_width
        self.y = (self.y + dy) % grid_height

    def grow(self):
        """
        Incrementa la edad del individuo y lo convierte en adulto si es un hijo y tiene 8 años.
        Devuelve True si el individuo ha crecido (ha pasado de ser hijo a adulto en este turno).
        """
        self.age += 1  # Incrementar la edad en 1 año por iteración
        has_grown = False
        if self.is_child and self.age >= 8:  # Si es un hijo y tiene 8 años o más
            self.is_child = False  # Se convierte en adulto
            has_grown = True  # Indica que ha crecido
        return has_grown

    def assign_nature(self):
        # Probabilidad para los tipos de individuos
        prob = random.random()
        if prob < 0.33:
            return 'HOSTIL'
        elif prob < 0.66:
            return 'ALIADO'
        else:
            return 'RANDOM'


# ---------------------- Clase PoderJugador ----------------------
# Gestiona los parámetros de los poderes y habilidades disponibles para el jugador
class PlayerPower:
    def __init__(self):
        self.cooldown = 0  # Tiempo restante de cooldown
        self.duration = 0  # Tiempo restante de duración del poder
        self.active = False  # Indica si el poder está activo

    def activate(self):
        """Activa el poder si no está en cooldown."""
        if self.cooldown == 0:
            self.active = True
            self.duration = 4  # Duración del poder (4 iteraciones)
            self.cooldown = 10  # Cooldown del poder (10 iteraciones)

    def update(self):
        """Actualiza el estado del poder (duración y cooldown)."""
        if self.active:
            self.duration -= 1
            if self.duration <= 0:
                self.active = False
        if self.cooldown > 0:
            self.cooldown -= 1

    def is_active(self):
        """Devuelve True si el poder está activo."""
        return self.active

    def is_ready(self):
        """Devuelve True si el poder está listo para usarse."""
        return self.cooldown == 0