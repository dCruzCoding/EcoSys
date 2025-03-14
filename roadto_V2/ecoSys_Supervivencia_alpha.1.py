import pygame
import random as rd
import clasesEcoSys as clase
import os


# ---------------------- Parámetros globales ----------------------

# Definir diccionario con los colores que vamos a utilizar
COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'BLUE': (0, 0, 200),  # Azul oscuro para adultos
    'LIGHT_BLUE': (173, 216, 230),  # Azul claro para hijos
    'INDIGO': (0, 128, 255),  # Color añil para crecimiento
    'PINK': (255, 0, 255),
    'DARK_RED': (178, 34, 34),
    'RED': (255, 0, 0),  
    'GREEN': (0, 255, 0),  
    'GRAY': (200, 200, 200)
}

# ---------------------- Funciones de Configuración ----------------------

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


def seleccionar_tamaño():
    """Pide al usuario que seleccione un tamaño para el tablero de juego."""
    print("Selecciona el tamaño:")
    print("1 - Pequeño (15x15)")
    print("2 - Medio (20x20)")
    print("3 - Grande (25x25)")
    opcion = input("Ingresa el número del tamaño: ")

    if opcion == "1":
        return "pequeño"
    elif opcion == "2":
        return "medio"
    elif opcion == "3":
        return "grande"
    else:
        print("Opción no válida. Usando tamaño medio por defecto.")
        return "medio"


# ---------------------- Funciones de dibujo ----------------------

def draw_grid(screen, config):
    """ 
    Dibuja la cuadrícula de la simulación
    :param screen: Superficie de Pygame donde se dibuja.
       """
    for x in range(0, config.screen_width, config.cell_size):
        pygame.draw.line(screen, COLORS['GRAY'], (x, 0), (x, config.screen_height))
    for y in range(0, config.screen_height, config.cell_size):
        pygame.draw.line(screen, COLORS['GRAY'], (0, y), (config.screen_width, y))

def draw_individuos(screen, jugador, individuos, config):
    """
    Dibuja los individuos en la cuadrícula.
    :param screen: Superficie de Pygame donde se dibuja.
    :param individuos: Lista de individuos a dibujar.
    """
    for ind in individuos:
        if ind == jugador:
            color = COLORS['GREEN']  # Jugador
        elif ind.is_child:
            color = COLORS['LIGHT_BLUE']  # Hijos (azul claro)
        else:
            color = COLORS['BLUE']  # Adultos
        pygame.draw.circle(screen, color,
                           (ind.x * config.cell_size + config.cell_size // 2, ind.y * config.cell_size + config.cell_size // 2),
                           config.cell_size // 3)


def draw_interacciones(screen, interacciones, config):
    """
    Dibuja las celdas con interacciones (conflictos, reproducciones, muertes por envejecimiento y crecimiento).
    :param screen: Superficie de Pygame donde se dibuja.
    :param interacciones: Diccionario con las interacciones por celda.
    """
    cell_size = config.cell_size
    for pos, tipo in interacciones.items():
        if tipo == 'CONFLICTO':
            pygame.draw.rect(screen, COLORS['RED'],
                             (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))
        elif tipo == 'REPRODUCCION':
            pygame.draw.rect(screen, COLORS['PINK'],
                             (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))
        elif tipo == 'MUERTE':  # Muerte por envejecimiento (celda en negro)
            pygame.draw.rect(screen, COLORS['BLACK'],
                             (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))
        elif tipo == 'CRECIMIENTO':  # Crecimiento de hijo a adulto (celda en añil)
            pygame.draw.rect(screen, COLORS['INDIGO'],  
                             (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))


def draw_stats(screen, iteracion, vivos, estadistica):
    """ Dibuja las estadísticas en pantalla """
    font = pygame.font.SysFont(None, 30)
    reproducciones, conflictos, muertes = estadistica.obtener_totales()
    text = f"Iteración: {iteracion} | Vivos: {vivos} | Rep: {reproducciones} | Conf: {conflictos} | Muerte: {muertes}"
    text_surface = font.render(text, True, COLORS['BLACK'])
    screen.blit(text_surface, (10, 10))


def draw_exit_button(screen, config):
    """
    Dibuja el botón de salida en la esquina inferior derecha de la pantalla.
    :param screen: Superficie de Pygame donde se dibuja.
    :param config: Instancia de Config para obtener las dimensiones de la pantalla.
    """
    # Configuración del botón (constantes)
    button_color = COLORS['DARK_RED']  # Color del botón
    button_radius = 12  # Tamaño (radio del botón circular)
    button_center = (config.screen_width - 25, config.screen_height - 25)  # Posición (esquina inferior derecha)

    # Dibujar el botón
    pygame.draw.circle(screen, button_color, button_center, button_radius)

    # Dibujar la "X" en el botón
    font = pygame.font.SysFont(None, 15)
    text_surface = font.render("x", True, COLORS['WHITE'])
    text_rect = text_surface.get_rect(center=button_center)
    screen.blit(text_surface, text_rect)

# ---------------------- Funciones de control del juego ----------------------

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


def check_button_click(pos, config):
    """
    Verifica si se hizo clic en el botón de salida.
    :param pos: Posición del clic del ratón (tupla x, y).
    :param config: Instancia de Config para obtener las dimensiones de la pantalla.
    :return: True si el clic fue dentro del botón, False en caso contrario.
    """
    button_radius = 12  # Tamaño (radio del botón circular)
    button_center = (config.screen_width - 25, config.screen_height - 25)  # Posición (esquina inferior derecha)

    # Calcular la distancia entre el clic y el centro del botón
    distance = ((pos[0] - button_center[0]) ** 2 + (pos[1] - button_center[1]) ** 2) ** 0.5
    return distance <= button_radius



# ---------------------- Funciones del fujo del juego ----------------------
def manejar_movimiento(event):
    """Procesa el evento de teclado y devuelve el movimiento correspondiente."""
    movimiento = [0, 0]
    if event.key == pygame.K_LEFT:
        movimiento[0] = -1
    elif event.key == pygame.K_RIGHT:
        movimiento[0] = 1
    elif event.key == pygame.K_UP:
        movimiento[1] = -1
    elif event.key == pygame.K_DOWN:
        movimiento[1] = 1
    return movimiento


def actualizar_posiciones(jugador, individuos, movimiento, grid_width, grid_height):
    """Actualiza las posiciones del jugador y los demás individuos."""
    # Mover al jugador
    jugador.x += movimiento[0]
    jugador.y += movimiento[1]
    jugador.x = max(0, min(jugador.x, grid_width - 1))
    jugador.y = max(0, min(jugador.y, grid_height - 1))

    # Mover automáticamente el resto de los individuos
    for ind in individuos:
        if ind != jugador:
            ind.move(grid_width, grid_height)


def procesar_interacciones(jugador, individuos, estadistica, interacciones, contador_prints):
    """Procesa las interacciones entre los individuos y actualiza las estadísticas."""
    celdas = {}
    for ind in individuos:
        pos = (ind.x, ind.y)
        if pos not in celdas:
            celdas[pos] = []
        celdas[pos].append(ind)

    nuevos_individuos = []
    for pos, inds in celdas.items():
        if len(inds) > 1:

            # Procesar interacciones con el jugador
            if jugador in inds:
                for ind in inds:
                    if ind != jugador:
                        if ind.tipo == 'RANDOM':
                            tipo_individuo = rd.choice(['HOSTIL', 'ALIADO'])
                        else:
                            tipo_individuo = ind.tipo

                        if tipo_individuo == 'HOSTIL':
                            print(f"¡El jugador ha sido atacado por un hostil en {pos}!")
                            contador_prints += 1
                            estadistica.sumar_conflicto(1)
                            interacciones[pos] = 'CONFLICTO'
                            return False, contador_prints  # El jugador muere
                        elif tipo_individuo == 'ALIADO' and not ind.is_child:  # Solo reproducirse con adultos
                            nuevo_hijo = clase.Individuo_Supervivencia(pos[0], pos[1], age=0, is_child=True)
                            nuevos_individuos.append(nuevo_hijo)
                            estadistica.sumar_reproduccion()
                            interacciones[pos] = 'REPRODUCCION'
                            print(f"¡El jugador se ha reproducido en {pos}!")
                            contador_prints += 1

            else:
                # Procesar interacciones entre otros individuos
                for i, ind1 in enumerate(inds):
                    for ind2 in inds[i+1:]:
                        if ind1.tipo == 'RANDOM':
                            tipo_ind1 = rd.choice(['HOSTIL', 'ALIADO'])
                        else:
                            tipo_ind1 = ind1.tipo
                        if ind2.tipo == 'RANDOM':
                            tipo_ind2 = rd.choice(['HOSTIL', 'ALIADO'])
                        else:
                            tipo_ind2 = ind2.tipo





                        if tipo_ind1 == 'HOSTIL' and tipo_ind2 == 'HOSTIL':
                            print(f"¡Conflicto entre dos hostiles en {pos}!")
                            contador_prints += 1
                            estadistica.sumar_conflicto(1)
                            interacciones[pos] = 'CONFLICTO'
                            inds.remove(rd.choice([ind1, ind2]))






                        # Reproducción (No puede haber reproducción con un HIJO)
                        elif tipo_ind1 == 'ALIADO' and tipo_ind2 == 'ALIADO' and not ind1.is_child and not ind2.is_child:
                            nuevo_hijo = clase.Individuo_Supervivencia(pos[0], pos[1], age=0, is_child=True)
                            nuevos_individuos.append(nuevo_hijo)
                            estadistica.sumar_reproduccion()
                            interacciones[pos] = 'REPRODUCCION'
                            print(f"¡Reproducción entre dos aliados en {pos}!")
                            contador_prints += 1



                        # Si se encuentran uno ALIADO y HOSTIL, lo que ocurrirá es random
                        else:
                            if rd.choice([True, False]):
                                if tipo_ind1 == 'HOSTIL':
                                    inds.remove(ind2)
                                else:
                                    inds.remove(ind1)
                                estadistica.sumar_conflicto(1)
                                interacciones[pos] = 'CONFLICTO'
                                print(f"¡Conflicto entre un hostil y un aliado en {pos}!")
                                contador_prints += 1
                            else:
                                # No se reproducirá si uno de los dos es HIJO
                                if not ind1.is_child and not ind2.is_child:
                                    nuevo_hijo = clase.Individuo_Supervivencia(pos[0], pos[1], age=0, is_child=True)
                                    nuevos_individuos.append(nuevo_hijo)
                                    estadistica.sumar_reproduccion()
                                    interacciones[pos] = 'REPRODUCCION'
                                    print(f"¡Reproducción entre un hostil y un aliado en {pos}!")
                                    contador_prints += 1
            nuevos_individuos.extend(inds)
        else:
            nuevos_individuos.extend(inds)

    # Actualizar crecimiento y envejecimiento
    for ind in nuevos_individuos:
        ha_crecido = ind.crecer()  # Llamar a crecer() y obtener si ha crecido
        if ha_crecido:  # Si el individuo ha crecido
            print(f"¡Un hijo ha crecido y se ha convertido en adulto en {(ind.x, ind.y)}!")
            contador_prints += 1
            interacciones[(ind.x, ind.y)] = 'CRECIMIENTO'  # Registrar crecimiento
        if ind.age >= 33:  # Verificar si muere de vejez
            print(f"{ind.nombre if hasattr(ind, 'nombre') else 'Un individuo'} ha muerto de viejo en {(ind.x, ind.y)}.")
            contador_prints += 1
            estadistica.sumar_muerte(1)
            interacciones[(ind.x, ind.y)] = 'MUERTE'  # Registrar muerte por envejecimiento

    individuos[:] = [ind for ind in nuevos_individuos if ind.age < 33]
    return jugador in individuos, contador_prints  # Devuelve True si el jugador sigue vivo y el contador de prints


def dibujar_simulacion(screen, jugador, individuos, estadistica, iteracion, interacciones, config):
    """Dibuja la simulación en la pantalla."""
    screen.fill(COLORS['WHITE'])
    draw_grid(screen, config)

    # Dibujar individuos
    draw_individuos(screen, jugador, individuos, config) 

    # Dibujar interacciones
    draw_interacciones(screen, interacciones, config) 

    # Dibujar estadísticas y botón de salida
    draw_stats(screen, iteracion, len(individuos), estadistica)
    draw_exit_button(screen, config) 

    pygame.display.flip()


def mostrar_fin_juego(screen, config):
    """Muestra el mensaje 'THE END' en la pantalla."""
    screen.fill(COLORS['WHITE'])
    draw_grid(screen, config)
    font = pygame.font.SysFont(None, 72)
    text_surface = font.render("THE END", True, COLORS['BLACK'])
    text_rect = text_surface.get_rect(center=(config.screen_width // 2, config.screen_height // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

    # Esperar a que el usuario pulse una tecla o cierre la ventana
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                waiting = False


def main():
    # Seleccionar el tamaño del tablero
    tamaño = seleccionar_tamaño()
    config = clase.Config(tamaño)

    # Iniciar la simulación con la configuración seleccionada
    print(f"Iniciando simulación en tamaño {tamaño} ({config.grid_width}x{config.grid_height})")
    simulacion_supervivencia(config)  # Pasar la configuración a la función de simulación


def simulacion_supervivencia(config):
    """Ejecuta la simulación en modo supervivencia."""
    try:
        num_individuos, _ = input_screen()
        pygame.init()
        screen = pygame.display.set_mode((config.screen_width, config.screen_height))
        pygame.display.set_caption("Simulación de Supervivencia")

        individuos = [clase.Individuo_Supervivencia(rd.randint(0, config.grid_width - 1),
                      rd.randint(0, config.grid_height - 1)) for _ in range(num_individuos)]
        jugador = individuos[0]
        jugador.age = -10
        estadistica = clase.Estadistica()

        running = True
        iteracion = 0
        interacciones = {}
        contador_prints = 0

        while running:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if check_button_click(event.pos, config):
                    running = False
            elif event.type == pygame.KEYDOWN:
                movimiento = manejar_movimiento(event)
                if movimiento != [0, 0]:
                    actualizar_posiciones(jugador, individuos, movimiento, config.grid_width, config.grid_height)
                    interacciones.clear()  # Limpiar interacciones de la ronda anterior
                    running, contador_prints = procesar_interacciones(jugador, individuos, estadistica, interacciones, contador_prints)
                    dibujar_simulacion(screen, jugador, individuos, estadistica, iteracion, interacciones, config)
                    iteracion += 1

                    # Limpiar la consola cada 3 rondas
                    if contador_prints >= 10:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        contador_prints = 0

        mostrar_fin_juego(screen, config)
        pygame.quit()

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        pygame.quit()



if __name__ == "__main__":
    main()