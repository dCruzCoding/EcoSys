'''Programa en Python que simula “vida artificial” en una cuadrícula. En este ejemplo:
- La cuadrícula tiene un tamaño fijo (por ejemplo, 20x20) y los individuos se mueven en las 8 direcciones (incluyendo las diagonales).
- El usuario define el número de individuos iniciales y el número de iteraciones.
- En cada iteración, cada individuo se mueve (con envolvimiento en los bordes), se agrupan los individuos por celda y, si hay más de uno en la misma celda, se produce:
  o Reproducción: Con cierta probabilidad (en este ejemplo, 0.3) se genera un nuevo individuo (hijo) en esa celda.
  o Conflicto (comerse entre sí): De entre los individuos que se han encontrado en esa celda se elige aleatoriamente uno que “sobrevive” (se asume que este se come a los otros).
- Finalmente, cada individuo envejece en 1 unidad de tiempo y cuando alcanza 100, muere (se elimina de la simulación).
Puedes ajustar parámetros (como el tamaño de la cuadrícula, la probabilidad de reproducción, etc.) según tus necesidades.

Cómo funciona el programa:

Inicialización:
- Se pide al usuario el número de individuos iniciales y el número de iteraciones.
- Se generan los individuos en posiciones aleatorias dentro de la cuadrícula de 20x20.

Bucle de simulación (iteraciones):
- Movimiento: Cada individuo se mueve aleatoriamente en una de las 8 direcciones. Si se sale de la cuadrícula, se utiliza el módulo para “envolver” la posición.
- Interacción:
  > Se agrupan los individuos por posición.
  o En las celdas donde hay más de un individuo, se evalúa la reproducción (con probabilidad definida) y luego se simula que ocurre un “combate” 
  en el que solo uno sobrevive (se “come” a los otros).
- Envejecimiento y muerte: Cada individuo incrementa su edad. Si su edad es 100 o mayor, el individuo muere y se elimina.
- Se muestra en pantalla el número de individuos vivos en cada iteración.

Terminación:
- La simulación finaliza cuando se han completado todas las iteraciones o cuando no quedan individuos vivos.

Este ejemplo es una base que puedes ampliar o modificar (por ejemplo, añadiendo más atributos, condiciones para la reproducción, energía, etc.)
para simular comportamientos más complejos en sistemas de vida artificial.'''




#.___  ___. ____    ____      ______   ____    __    ____ .__   __.    .______    __    ______        _______.____    ____  _______.___________. _______ .___  ___. 
#|   \/   | \   \  /   /     /  __  \  \   \  /  \  /   / |  \ |  |    |   _  \  |  |  /  __  \      /       |\   \  /   / /       |           ||   ____||   \/   | 
#|  \  /  |  \   \/   /     |  |  |  |  \   \/    \/   /  |   \|  |    |  |_)  | |  | |  |  |  |    |   (----` \   \/   / |   (----`---|  |----`|  |__   |  \  /  | 
#|  |\/|  |   \_    _/      |  |  |  |   \            /   |  . `  |    |   _  <  |  | |  |  |  |     \   \      \_    _/   \   \       |  |     |   __|  |  |\/|  | 
#|  |  |  |     |  |        |  `--'  |    \    /\    /    |  |\   |    |  |_)  | |  | |  `--'  | .----)   |       |  | .----)   |      |  |     |  |____ |  |  |  | 
#|__|  |__|     |__|         \______/      \__/  \__/     |__| \__|    |______/  |__|  \______/  |_______/        |__| |_______/       |__|     |_______||__|  |__| 
                                                                                                                                                                   

#            ____    ____  _______ .______      _______. __    ______   .__   __.     __       ___   
#            \   \  /   / |   ____||   _  \    /       ||  |  /  __  \  |  \ |  |    /_ |     / _ \  
#             \   \/   /  |  |__   |  |_)  |  |   (----`|  | |  |  |  | |   \|  |     | |    | | | | 
#              \      /   |   __|  |      /    \   \    |  | |  |  |  | |  . `  |     | |    | | | | 
#               \    /    |  |____ |  |\  \--.--)   |   |  | |  `--'  | |  |\   |     | |  __| |_| | 
#                \__/     |_______|| _| `.___|_____/    |__|  \______/  |__| \__|     |_| (__)\___/  
                                                                                                        



import random

# Parámetros globales
grid_width = 20    # ancho de cuadricula
grid_height = 20    # alto de cuadricula
reproduction_prob = 0.4   # prob de reproduccion al ocurrir encuentro

class Individuo:
    def __init__(self, x, y, age=0):
        self.x = x
        self.y = y
        self.age = age

    def move(self):
        '''
        Mueve el individuo en una de las 8 direcciones posibles randomly.
        Se utiliza el envolvimiento (modular) para que la posicion se mantenga
        dentro de la cuadrícula.
        '''
        # Lista con movimientos posibles: 8 direciones
        movimientos = [(-1,-1), (-1,0), (-1,1), (0,-1),    # (0,0) = ausencia de mov
                       (0,1), (1,-1), (1,0), (1,1)]
        dx, dy = random.choice(movimientos)
        self.x = (self.x + dx) % grid_width
        self.y = (self.y + dy) % grid_height

    def __repr__(self):
        return f"Nuevo inidivuo generado ({self.x}, {self.y}, age = {self.age})"
    

def main():
    # Solicitar parámetros al usuario para definir el entorno
    num_individuos = int(input("Introduce el número de individuos iniciales: "))
    num_iteraciones = int(input("Introduce el número de iteraciones: "))

    # Inicializar los individuos en posiciones aleatorias dentro de la cuadrícula
    individuos = []
    for _ in range(num_individuos):
        x = random.randint(0, grid_width -1)
        y = random.randint(0, grid_height - 1)
        individuos.append(Individuo(x,y))

    # Bucle principal de la simulación
    for iteracion in range(1, num_iteraciones + 1):
        # Mover individuo
        for ind in individuos:
            ind.move()

        # Agrupamos a los individuos según su posición en la cuadrícula
        celdas = {}
        for ind in individuos:
            pos = (ind.x, ind.y)
            if pos not in celdas:
                celdas[pos] = []
            celdas[pos].append(ind)

        nuevos_individuos = []
        # Procesamos las posibles interacciones en cada celda
        for pos, inds in celdas.items():
            if len(inds)>1:
                # Si hay al menos 2 individuos en una celda, se produce el encuentro; pueden ocurrir varias cosas:
                # Primera opcion: Reproducción (se genera nuevo individuo 'hijo')
                if random.random() < reproduction_prob:  # random() genera num de 0 a 1 -no inclusiv-
                    # Creamos nuevo individuo (hijo) en esa posición, con edad 0
                    nuevos_individuos.append(Individuo(pos[0],pos[1],age=0))
                # Segunda opcion: Conflicto  (se comen entre sí y solo uno sobrevive)
                superviviente = random.choice(inds)  # Al elegir en inds, sólo eliminará de los originales
                nuevos_individuos.append(superviviente)
            else:
                # Si solo hay un individuo en esa celda, se queda tranquilo
                nuevos_individuos.extend(inds)

                
        # Actualizamos lista de individuos de las iteraciones
        individuos = nuevos_individuos

        # Envejecimiento y eliminamos los que llegan a 100 iteraciones
        supervivientes = []
        for ind in individuos:
            ind.age += 1
            if ind.age < 100:
                supervivientes.append(ind)
        individuos = supervivientes

        # Nos muestra el núm de individuos vivos
        print(f"Iteración {iteracion} terminada: {len(individuos)} individuos vivos")

        
        # Cuando no queden vivos, terminamos
        if len(individuos) == 0:
            print("No quedan individuos vivos. Fin de la simulación")
            break

if __name__ == "__main__":
    main()
               