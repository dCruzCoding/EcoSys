import random

class Config:
    def __init__(self, tamaño):
        # Definir el tamaño de la cuadrícula y el límite máximo de individuos
        if tamaño == "pequeño":
            self.grid_width = 15
            self.grid_height = 15
            self.max_individuos = 50  # Límite para tamaño pequeño
        elif tamaño == "medio":
            self.grid_width = 20
            self.grid_height = 20
            self.max_individuos = 100  # Límite para tamaño medio
        elif tamaño == "grande":
            self.grid_width = 25
            self.grid_height = 25
            self.max_individuos = 150  # Límite para tamaño grande

        # Tamaño de cada celda y dimensiones de la pantalla
        self.cell_size = 30
        self.screen_width = self.grid_width * self.cell_size
        self.screen_height = self.grid_height * self.cell_size


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
    


# ---------------------- Clase Individuo  ----------------------
# Representa un 'ser' dentro del sistema

class Individuo:
    def __init__(self, x, y, age=0, is_child=False, tipo=None):
        self.x = x  # Posicion X
        self.y = y  # Posiciion Y
        self.age = age  # Edad del individuo
        self.is_child = is_child  # Para distinguir si es un individuo hijo
        self.tipo = tipo if tipo else self.asignar_tipo()  # Solo asigna si no se proporciona

    def move(self, grid_width, grid_height):   # que le pase estos argumentos para no tener q ponerlo aqui
        """ Mueve al individuo en una dirección aleatoria dentro de la cuadrícula """
        movimientos = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                       (0, 1), (1, -1), (1, 0), (1, 1)]
        dx, dy = random.choice(movimientos)
        self.x = (self.x + dx) % grid_width
        self.y = (self.y + dy) % grid_height

    def crecer(self):
        """
        Incrementa la edad del individuo y lo convierte en adulto si es un hijo y tiene 8 años.
        Devuelve True si el individuo ha crecido (ha pasado de ser hijo a adulto en este turno).
        """
        self.age += 1  # Incrementar la edad en 1 año por iteración
        ha_crecido = False
        if self.is_child and self.age >= 8:  # Si es un hijo y tiene 8 años o más
            self.is_child = False  # Se convierte en adulto
            ha_crecido = True  # Indica que ha crecido
        return ha_crecido

    def asignar_tipo(self):
        # Probabilidad para los tipos de individuos
        prob = random.random()
        if prob < 0.33:
            return 'HOSTIL'
        elif prob < 0.66:
            return 'ALIADO'
        else:
            return 'RANDOM'





class PoderJugador:
    def __init__(self):
        self.cooldown = 0  # Tiempo restante de cooldown
        self.duracion = 0  # Tiempo restante de duración del poder
        self.activo = False  # Indica si el poder está activo

    def activar(self):
        """Activa el poder si no está en cooldown."""
        if self.cooldown == 0:
            self.activo = True
            self.duracion = 4  # Duración del poder (4 iteraciones)
            self.cooldown = 10  # Cooldown del poder (10 iteraciones)

    def actualizar(self):
        """Actualiza el estado del poder (duración y cooldown)."""
        if self.activo:
            self.duracion -= 1
            if self.duracion <= 0:
                self.activo = False
        if self.cooldown > 0:
            self.cooldown -= 1

    def esta_activo(self):
        """Devuelve True si el poder está activo."""
        return self.activo

    def esta_listo(self):
        """Devuelve True si el poder está listo para usarse."""
        return self.cooldown == 0

