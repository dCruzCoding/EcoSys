""" 👋 ¡Hola! Bienvenido a mi pequeño Ecosistema virtual 🌍🌐

Soy Daniel Cruz (dCruzCoding) y desarrollado un simulador de 'vida artificial', en un entorno físico limitado. 

A continuación te explico cómo funciona el programa:
    ▶️ Inicialización:
        Se le pide al usuario el número de individuos iniciales y el número de iteraciones.
        Se generan los individuos en posiciones aleatorias dentro de una cuadrícula fija.

    🔄 Bucle de simulación (iteraciones):
        🚶‍♀️ Movimiento: Cada individuo se mueve aleatoriamente en una de las 8 direcciones. Si se sale de la cuadrícula, 
        se utiliza el módulo para “envolver” la posición.

        Interacción:
            Se agrupan los individuos por posición.
            En las celdas donde hay más de un individuo, se utiliza un módulo random para generar un valor aleatorio
            de 0 a 1 que utilizaremos para comprobar qué acción se realizará; reproducción, conflicto, o nada.
            o	👶 Reproducción (probabilidad de 0.4): se genera un nuevo individuo (hijo) en esa celda.
                ¡OJO! Cada individuo hijo (representado de color rosa) tardará un total de 5 turnos (iteraciones) en
                crecer y convertirse en adulto. Hasta entonces NO podrá tener encuentros con otros individuos.
            o	⚔️ Conflicto (probabilidad de 0.5): uno de los individuos encontrados en la celda, muere y otro “sobrevive”.
            o	No es muy probable, pero también puede que no ocurra y ambos sigan tranquilos con su transcurso.
             
        Envejecimiento y muerte: Cada individuo incrementa su edad en cada iteración. Si la edad es 65 o mayor, el individuo 
        muere y se elimina.

        👁️ ¡OJO! Cada vez que haya un evento (reproducción, conflicto, crecimiento de hijo a adulto, o muerte por envejecimiento)
        se pausará el flujo del programa y el usuario deberá darle a cualquier tecla para continuar. Además, también se mostrará
        un mensaje (si no en el runtime del programa) con los individuos vivos y qué evento a ocurrido.
        
    Continuamente se mostrará en pantalla un contador con los individuos vivos y con las veces que se ha dado uno
    de los eventos anteriormente mencionados.

    🏁 La simulación finaliza cuando se han completado todas las iteraciones o cuando no quedan individuos vivos. El usuario
    también puede decidir finalizar el programa cerrando la ventana al botón de exit ('x').

    

🆕🌟 ¿Qué he añadido respecto al código base (version 1.0)? 🆕🌟

- Clase Estadistica para mejorar la organización de contadores totales. Añadidos contadores de eventos e individuos vivos.

- Imprimir unicamente cuando haya evento, mostrando información de qué iteración es y cuántos quedan vivos,
  y qué evento ocurrió y sus consecuencias.

- Añadir pantalla de visualizacion con pygame: tanto para pedir el input, como para mostrar la cuadrilla con 
la simulación del 'biosistema virtual'. Además, se marca cada evento con un color, se añade pausa tras evento  (para continuar,
cualquier interacción del usuario con el teclado vale), y boton para finalizar la ejecución en cualquier momento.

- Añadido 5 turnos para pasar de hijo a individuo adulto (hijo: representado como rosa en pantalla e invulnerable a encuentros)

- Eventos conflicto y reproducción excluyentes entre si: si ocurre uno no ocurre el otro.

- Añadida pequeña probabilidad de que no ocurra nada al tener un encuentro.

- Comentarios explicativos en el código.


🔝 POSIBLES MEJORAS: Añadir trazabilidad al runtime de la ejecución. Añadir try/except para controlar excepciones. 
Añadir validaciones para controlar errores (p.ej, en input). 
"""


#   .___  ___. ____    ____      ______   ____    __    ____ .__   __.    .______    __    ______        _______.____    ____  _______.___________. _______ .___  ___. 
#   |   \/   | \   \  /   /     /  __  \  \   \  /  \  /   / |  \ |  |    |   _  \  |  |  /  __  \      /       |\   \  /   / /       |           ||   ____||   \/   | 
#   |  \  /  |  \   \/   /     |  |  |  |  \   \/    \/   /  |   \|  |    |  |_)  | |  | |  |  |  |    |   (----` \   \/   / |   (----`---|  |----`|  |__   |  \  /  | 
#   |  |\/|  |   \_    _/      |  |  |  |   \            /   |  . `  |    |   _  <  |  | |  |  |  |     \   \      \_    _/   \   \       |  |     |   __|  |  |\/|  | 
#   |  |  |  |     |  |        |  `--'  |    \    /\    /    |  |\   |    |  |_)  | |  | |  `--'  | .----)   |       |  | .----)   |      |  |     |  |____ |  |  |  | 
#   |__|  |__|     |__|         \______/      \__/  \__/     |__| \__|    |______/  |__|  \______/  |_______/        |__| |_______/       |__|     |_______||__|  |__| 
                                                                                                                                                                   
# Versión 1.2 


import pygame
import random


# ---------------------- Parámetros globales ----------------------

# Definir el tamaño de la cuadrícula
grid_width = 20    # ancho de cuadrícula
grid_height = 20   # alto de cuadrícula
cell_size = 30     # tamaño de cada celda en píxeles

# Definir el tamaño de la pantalla de simulación en 'pygame'
screen_width = grid_width * cell_size  # ancho
screen_height = grid_height * cell_size  # alto

# Definir diccionario con los colores que vamos a utilizar
COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'BLUE': (0, 0, 255),
    'PINK': (255, 0, 255),
    'DARK_RED': (178, 34, 34),
    'RED': (255, 0, 0),  
    'GREEN': (0, 255, 0),  
    'GRAY': (200, 200, 200)
}


# ---------------------- Configuración del botón de salida ----------------------

button_color = COLORS['DARK_RED']
button_radius = 12 # Tamaño (Radio del botón circular)
button_center = (screen_width - 25, screen_height - 25)  # Posición (esquina inferior derecha)


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

    def move(self):
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


# ---------------------- Funciones de dibujo ----------------------

def draw_grid(screen):
    """ Dibuja la cuadrícula de la simulación """
    for x in range(0, screen_width, cell_size):
        pygame.draw.line(screen, COLORS['GRAY'], (x, 0), (x, screen_height))
    for y in range(0, screen_height, cell_size):
        pygame.draw.line(screen, COLORS['GRAY'], (0, y), (screen_width, y))

def draw_individuos(screen, individuos):
    """ Dibuja los individuos en la cuadrícula """
    for ind in individuos:
        color = COLORS['PINK'] if ind.es_rosa() else COLORS['BLUE']  # Rosa para niños, azul para adultos
        pygame.draw.circle(screen, color,
                           (ind.x * cell_size + cell_size // 2, ind.y * cell_size + cell_size // 2),
                           cell_size // 3)

def draw_stats(screen, iteracion, vivos, estadistica):
    """ Dibuja las estadísticas en pantalla """
    font = pygame.font.SysFont(None, 30)
    reproducciones, conflictos, muertes = estadistica.obtener_totales()
    text = f"Iteración: {iteracion} | Vivos: {vivos} | Rep: {reproducciones} | Conf: {conflictos} | Muerte: {muertes}"
    text_surface = font.render(text, True, COLORS['BLACK'])
    screen.blit(text_surface, (10, 10))

def draw_exit_button(screen):
    """ Dibuja el botón de salida """
    pygame.draw.circle(screen, button_color, button_center, button_radius)
    font = pygame.font.SysFont(None, 15)
    text_surface = font.render("x", True, COLORS['WHITE'])
    text_rect = text_surface.get_rect(center=button_center)
    screen.blit(text_surface, text_rect)

def pause_for_event():
    """ Añade una pausa en la simulación tras cada evento """
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:  # Detectar clic del ratón
                if check_button_click(event.pos):  # Revisar si el clic fue sobre el botón
                    pygame.quit()
                    exit()
            elif event.type == pygame.KEYDOWN:
                paused = False  # Salir de la pausa si se presiona una tecla

def check_button_click(pos):
    """ Verifica si se hizo clic en el botón de salida """
    distance = ((pos[0] - button_center[0]) ** 2 + (pos[1] - button_center[1]) ** 2) ** 0.5
    return distance <= button_radius

def input_screen():
    """ Añade una pantalla para pedir al usuario los inputs que se requieren """
    pygame.init()
    screen_inp = pygame.display.set_mode((300,200))
    pygame.display.set_caption("Configuración de la Simulación")
    font_inp = pygame.font.Font(None, 20)
    
    # Inicializamos las cajas de entrada (dos: "Individuos" e "Iteraciones")
    input_boxes = ["", ""]  # [Individuos, Iteraciones]
    selected_box = 0  # Establecemos que la caja seleccionada inicialmente sea la primera (índice 0)

    # Añadimos variables para controlar la visibilidad del cursor de texto ('|')
    cursor_visible = True
    cursor_timer = pygame.time.get_ticks()  

    # Bucle principal de la pantalla de entrada, se ejecuta hasta que el usuario decida salir o de los datos
    running = True
    while running:

        # Definimos parámetros del formato de la pantalla
        screen_inp.fill(COLORS['WHITE'])
        title = font_inp.render("Ingrese valores y presione Enter", True, COLORS['BLACK'])
        screen_inp.blit(title, (50, 50))
        
        labels = ["Individuos: ", "Iteraciones: "]

        # Dibujamos las etiquetas y el texto ingresado (y el cursor si está activo)
        for i, label in enumerate(labels):
            text = input_boxes[i] + ("|" if cursor_visible and i == selected_box else "")
            # Renderizamos el texto y lo dibujamos en la pantalla
            txt_surface = font_inp.render(label + text, True, COLORS['BLACK'])
            screen_inp.blit(txt_surface, (50, 80 + i * 50))  # Colocamos el texto en su lugar

        # Actualizamos la pantalla para que se vea lo que hemos dibujado 
        pygame.display.flip()

        # Si han pasado 500 ms desde el último parpadeo del cursor, lo cambiamos de visibilidad
        if pygame.time.get_ticks() - cursor_timer > 500:
            cursor_visible = not cursor_visible
            cursor_timer = pygame.time.get_ticks()
        
        # Comprobamos los eventos del teclado y el ratón
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()   # Cerrar Pygame si el usuario cierra la ventana
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Si presiona ENTER...

                    if selected_box == 1 and input_boxes[0] and input_boxes[1]:   # Si estamos en la 2d caja (Iteraciones) y ambas tienen texto
                        pygame.quit()   # Se cierra la pantalla
                        return int(input_boxes[0]), int(input_boxes[1])   # Devuelve los valores de ambos input
                    # Si no, cambiamos la selección entre las dos cajas
                    selected_box = (selected_box + 1) % 2

                elif event.key == pygame.K_BACKSPACE:  # Si presionamos backspace
                    input_boxes[selected_box] = input_boxes[selected_box][:-1]  # Eliminamos el último carácter de la caja seleccionada
                elif event.unicode.isdigit():  # Si se presiona un dígito
                    input_boxes[selected_box] += event.unicode   # Añadimos el dígito a la caja de texto seleccionada


# ---------------------- Función principal ----------------------

def main():
    """ Ejecuta la simulación """

    # Parámetros para la simulación
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Declaración por parte del usuario del nº de individuos e iteraciones para la simulación
    num_individuos, num_iteraciones = input_screen()
    

    # Creación de interfaz con 'pygame'
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    # Inicializamos 'pygame' para poder utilizarlo sin errores 
    pygame.init()
    pygame.display.init()

    # Creamos la interfaz
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Simulación de Individuos")
    clock = pygame.time.Clock()

    # Creación de individuos (tantos como indique el usuario) y objeto estadística
    individuos = [Individuo(random.randint(0, grid_width - 1), random.randint(0, grid_height - 1)) for _ in range(num_individuos)]
    estadistica = Estadistica()


    # Flujo principal de la simulación
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    running = True
    iteracion = 0

    # Bucle principal: finaliza cuando lo indica el usuario (running=false) o se hagan todas las iteraciones declaradas
    while running and iteracion < num_iteraciones:
        iteracion += 1  # Incrementamos el número de iteración

        # Inicializamos contadores para los eventos en cada iteración (y así indicarlo en el print de cada iteracion)
        reproducciones = 0  # Nuevos individuos por reproducción
        conflictos = 0  # Conflictos entre individuos
        muertes = 0  # Muertes por envejecimiento
        crecimiento = 0  # Hijos que pasan a adultos

        # Listas para registrar celdas con los eventos ocurridos
        celdas_reproduccion = []
        celdas_conflicto = []
        celdas_muerte = []

        # Captura de acciones del usuario (pausa y cierre del programa)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    # Finaliza la simulación si se cierra la ventana
            elif event.type == pygame.MOUSEBUTTONDOWN:      
                if check_button_click(event.pos):     # Verifica si se hace clic en el botón de salida
                    print("Simulación terminada por el usuario.")
                    running = False

        # Movimiento de los individuos en la simulación
        for ind in individuos:
            ind.move()

        # Agrupar individuos por posición en un diccionario
        celdas = {}
        for ind in individuos:
            pos = (ind.x, ind.y)  # Posición del individuo en la cuadrícula
            if pos not in celdas:
                celdas[pos] = []
            celdas[pos].append(ind)


        nuevos_individuos = []  # Lista temporal para la siguiente generación de individuos
        celdas_evento = []  # Lista de celdas donde ocurren eventos


        # Evaluación de eventos en cada celda ocupada
        for pos, inds in celdas.items():
            if len(inds) > 1:  # Si hay más de un individuo en la celda
                probabilidad = random.random()  # Generamos un número aleatorio
                if probabilidad <= 0.4:  # 40% de probabilidad de reproducción
                    nuevo_hijo = Individuo(pos[0], pos[1], age=0, is_child=True, turnos_hijo=6)
                    nuevos_individuos.append(nuevo_hijo)
                    reproducciones += 1
                    estadistica.sumar_reproduccion()
                    celdas_reproduccion.append(pos)  # Registrar celda donde ocurrió reproducción
                    celdas_evento.append(pos)
                elif probabilidad < 0.9:  # 50% de probabilidad de conflicto (0.4 < probabilidad < 0.9)
                    superviviente = random.choice(inds)  # Un individuo sobrevive
                    nuevos_individuos.append(superviviente)
                    conflictos += len(inds) - 1  # Se eliminan los demás
                    estadistica.sumar_conflicto(len(inds) - 1)
                    celdas_conflicto.append(pos)  # Registrar celda donde ocurrió conflicto
                    celdas_evento.append(pos)
            else:
                nuevos_individuos.extend(inds)  # Si solo hay un individuo, se mantiene


        # Actualizar crecimiento de individuos
        for ind in nuevos_individuos:
            ind.crecer()  # El hijo crece a adulto
            if ind.is_child and not ind.es_rosa():  # Si ha pasado de niño a adulto, lo consideramos un CRECIMIENTO
                crecimiento += 1

        # Incrementamos la edad de los individuos
        for ind in nuevos_individuos:
            ind.age += 1

        # Muertes por envejecimiento
        individuos_vivos = [ind for ind in nuevos_individuos if ind.age < 65]
        muertes = len(nuevos_individuos) - len(individuos_vivos)

        # Agregar celdas de muerte por envejecimiento a la lista
        for ind in nuevos_individuos:
            if ind.age >= 65:  # Si la edad es mayor o igual a 65
                celdas_muerte.append((ind.x, ind.y))  # Se agrega la celda a las muertes por envejecimiento

        # Si un individuo ha muerto, lo agregamos a las celdas de muerte
        if muertes > 0:
            estadistica.sumar_muerte(muertes)
            celdas_muerte.extend(celdas_evento)

        # Actualizar la lista de individuos 
        individuos = individuos_vivos


        # Crear la plantilla para dibujar la simulación 
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        screen.fill(COLORS['WHITE'])  # fondo blanco
        draw_grid(screen) # dibujamos la cuadrícula

        # Dibujar celdas de eventos con colores diferentes  (muerte viejo = negras, repro = verde, conflict = rojo)
        for pos in celdas_reproduccion:
            pygame.draw.rect(screen, COLORS['GREEN'], (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))
        for pos in celdas_conflicto:
            pygame.draw.rect(screen, COLORS['RED'], (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))
        for pos in celdas_muerte:
            pygame.draw.rect(screen, COLORS['BLACK'], (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))  

        # Dibujar los elementos de la interfaz: pantalla, estadisticas, boton de salida
        draw_individuos(screen, individuos)
        draw_stats(screen, iteracion, len(individuos), estadistica)  # Pasamos la estadística
        draw_exit_button(screen)  # Dibuja el botón de salida
        pygame.display.flip()
        clock.tick(3)

        # Añadir funcionalida de pausa tras evento
        if reproducciones > 0 or conflictos > 0 or muertes > 0:
            pause_for_event()

        # Imprimir los eventos
        if reproducciones > 0 or conflictos > 0 or muertes > 0 or crecimiento > 0:
            print(f"Iteración {iteracion} terminada: {len(individuos)} individuos vivos")
            if reproducciones > 0:
                print(f"  Reproducción: {reproducciones} nuevos individuos")
            if conflictos > 0:
                print(f"  Conflictos: {conflictos} individuo asesinado")
            if muertes > 0:
                print(f"  Muertes: {muertes} individuos muertos")
            if crecimiento > 0:
                print(f"  Crecimiento: {crecimiento} individuos pasaron a adultos")

        # Cuando no queden vivos, terminamos
        if len(individuos) == 0:
            print("No quedan individuos vivos. Fin de la simulación")
            break

    pygame.quit()

if __name__ == "__main__":
    main()