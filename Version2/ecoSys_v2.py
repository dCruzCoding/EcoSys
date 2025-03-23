



#        _____          _____                               _____ 
#       |  ___|        /  ___|                             / __  \
#       | |__  ___ ___ \ `--. _   _ ___     __   _____ _ __`' / /'
#       |  __|/ __/ _ \ `--. \ | | / __|    \ \ / / _ \ '__| / /  
#       | |__| (_| (_) /\__/ / |_| \__ \     \ V /  __/ |_ ./ /___
#       \____/\___\___/\____/ \__, |___/      \_/ \___|_(_)\_____/
#                              __/ |                              
#                             |___/                               


import pygame
import random as rd
import clasesEcoSys as classEco
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
    'GRAY': (200, 200, 200)}



# ------------------- Funciones de menú y configuración inicial -------------------

def start_screen():
    """Muestra la pantalla inicio con la selección del modo de juego (Simulación o Supervivencia)."""
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("EcoSys: Selección de Modo")
    font = pygame.font.Font(None, 24)
    
    # Título del programa
    title = font.render("EcoSys: Selecciona el Modo", True, COLORS['BLACK'])
    
    # Opciones de modo de juego
    modes = ["Simulacion", "Supervivencia"]
    selected_mode = 0
    
    running = True
    while running:
        screen.fill(COLORS['WHITE'])
        screen.blit(title, (50, 20))

        # Dibujar las opciones de modo de juego
        for i, mode in enumerate(modes):
            color = COLORS['BLUE'] if i == selected_mode else COLORS['BLACK']
            mode_text = font.render(f"{i+1}. {mode}", True, color)
            screen.blit(mode_text, (50, 60 + i * 30))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None  # Devuelve None si el usuario cierra la ventana
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.quit()
                    return modes[selected_mode]  # Devuelve el modo seleccionado
                elif event.key == pygame.K_UP:
                    selected_mode = (selected_mode - 1) % len(modes)
                elif event.key == pygame.K_DOWN:
                    selected_mode = (selected_mode + 1) % len(modes)

    # Si se sale del bucle porque el usuario cerró la ventana, terminamos el programa
    pygame.quit()
    return None

def survival_input_screen():
    """Muestra la pantalla para seleccionar el tamaño y la dificultad en modo Supervivencia."""
    try:
        pygame.init()
        screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("EcoSys: Parámetros de Supervivencia")
        font = pygame.font.Font(None, 24)
        
        # Título del programa
        title = font.render("Selecciona el tamaño y la dificultad", True, COLORS['BLACK'])
        
        # Opciones de tamaño
        sizes = ["Pequeño (15x15)", "Medio (20x20)", "Grande (25x25)"]
        selected_size = 0
        
        # Opciones de dificultad
        difficulties = ["Facil (15 individuos)", "Medio (25 individuos)", "Dificil (40 individuos)"]
        selected_difficulty = 0
        
        # Variable para alternar entre tamaño y dificultad
        selecting_size = True  # True será para SIZE
        
        running = True
        while running:
            screen.fill(COLORS['WHITE'])
            screen.blit(title, (50, 20))

            # Dibujar las opciones de tamaño
            for i, size in enumerate(sizes):
                color = COLORS['BLUE'] if i == selected_size and selecting_size else COLORS['BLACK']
                size_text = font.render(f"Tamaño {i+1}: {size}", True, color)
                screen.blit(size_text, (50, 60 + i * 30))

            # Dibujar las opciones de dificultad
            for i, difficulty in enumerate(difficulties):
                color = COLORS['BLUE'] if i == selected_difficulty and not selecting_size else COLORS['BLACK']
                difficulty_text = font.render(f"Dificultad {i+1}: {difficulty}", True, color)
                screen.blit(difficulty_text, (50, 150 + i * 30))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return None  # Evita errores en Jupyter al cerrar la ventana
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if selecting_size:
                            selecting_size = False  # Cambiar a selección de dificultad
                        else:
                            pygame.quit()
                            return sizes[selected_size][:-8], difficulties[selected_difficulty][:-15].strip()
                    elif event.key == pygame.K_UP:
                        if selecting_size:
                            selected_size = (selected_size - 1) % len(sizes)
                        else:
                            selected_difficulty = (selected_difficulty - 1) % len(difficulties)
                    elif event.key == pygame.K_DOWN:
                        if selecting_size:
                            selected_size = (selected_size + 1) % len(sizes)
                        else:
                            selected_difficulty = (selected_difficulty + 1) % len(difficulties)
    except Exception as err:
        print(err)

def simulation_input_screen():
    """ Pantalla de configuración para el modo SIMULACIÓN con selección de tamaño. """
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Configuración de la Simulación")
    font = pygame.font.Font(None, 24)
    
    sizes = ["Pequeño (15x15)", "Medio (20x20)", "Grande (25x25)"]
    selected_size = 0
    input_boxes = ["", ""]  # [Individuos, Iteraciones]
    selected_box = 0  

    cursor_visible = True
    cursor_timer = pygame.time.get_ticks()  
    selecting_size = True  

    running = True
    while running:
        screen.fill(COLORS['WHITE'])
        title = font.render("Selecciona el tamaño y los valores:", True, COLORS['BLACK'])
        screen.blit(title, (50, 20))
        
        if selecting_size:
            for i, size in enumerate(sizes):
                color = COLORS['BLUE'] if i == selected_size else COLORS['BLACK']
                size_text = font.render(f"Tamaño {i+1}: {size}", True, color)
                screen.blit(size_text, (50, 60 + i * 30))
        else:
            labels = ["Individuos: ", "Iteraciones: "]
            for i, label in enumerate(labels):
                text = input_boxes[i] + ("|" if cursor_visible and i == selected_box else "")
                txt_surface = font.render(label + text, True, COLORS['BLACK'])
                screen.blit(txt_surface, (50, 60 + i * 50)) 
        
        pygame.display.flip()

        if pygame.time.get_ticks() - cursor_timer > 500:
            cursor_visible = not cursor_visible
            cursor_timer = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return None  # Evita errores en Jupyter al cerrar la ventana

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if selecting_size:
                        selecting_size = False  
                    else:
                        if selected_box == 1 and input_boxes[0] and input_boxes[1]:   
                            pygame.quit()   
                            return sizes[selected_size][:-8], int(input_boxes[0]), int(input_boxes[1])   
                        selected_box = (selected_box + 1) % 2

                elif event.key == pygame.K_BACKSPACE and not selecting_size:
                    input_boxes[selected_box] = input_boxes[selected_box][:-1]  

                elif event.unicode.isdigit() and not selecting_size:
                    input_boxes[selected_box] += event.unicode  

                elif selecting_size:
                    if event.key == pygame.K_UP:
                        selected_size = (selected_size - 1) % len(sizes)
                    elif event.key == pygame.K_DOWN:
                        selected_size = (selected_size + 1) % len(sizes)



# ---------------------- Funciones de interfaz de usuario ----------------------

def show_temporary_message(screen, config, message, duration=1):
    """
    Muestra un mensaje temporal en la pantalla.
    """
    # Ajustar el tamaño de la fuente según el ancho de la pantalla
    font_size = max(32, min(42, int(config.screen_width / 20)))  # Tamaño entre 32 y 42, ajustado al ancho de la pantalla
    font = pygame.font.SysFont(None, font_size)
    
    # Renderizar el texto
    text_surface = font.render(message, True, COLORS['BLACK'])
    text_rect = text_surface.get_rect(center=(config.screen_width // 2, config.screen_height // 2))
    
    # Dibujar el mensaje
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

    # Esperar la duración del mensaje
    pygame.time.wait(int(duration * 1000))

def show_end_game(screen, config):
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

def draw_individuals(screen, player, individuals, config, power_active=False):
    """
    Dibuja los individuos en la cuadrícula.
    :param screen: Superficie de Pygame donde se dibuja.
    :param individuals: Lista de individuos a dibujar.
    :param power_active: Si el poder está activo, cambia los colores según el naturaleza de individuo.
    """
    for ind in individuals:
        if ind == player:
            color = COLORS['GREEN']  # Jugador
        elif power_active:
            if ind.nature == 'ALIADO':
                color = COLORS['PINK']  # Aliados
            elif ind.nature == 'HOSTIL':
                color = COLORS['RED']  # Hostiles
            else:
                color = COLORS['GRAY']  # Random
        elif ind.is_child:
            color = COLORS['LIGHT_BLUE']  # Hijos (azul claro)
        else:
            color = COLORS['BLUE']  # Adultos
        pygame.draw.circle(screen, color,
                           (ind.x * config.cell_size + config.cell_size // 2, ind.y * config.cell_size + config.cell_size // 2),
                           config.cell_size // 3)

def draw_interactions(screen, interactions, config):
    """
    Dibuja las celdas con interacciones (conflictos, reproducciones, muertes por envejecimiento y crecimiento).
    :param screen: Superficie de Pygame donde se dibuja.
    :param interactions: Diccionario con las interacciones por celda.
    """
    cell_size = config.cell_size
    for pos, nature in interactions.items():
        if nature == 'CONFLICTO':
            pygame.draw.rect(screen, COLORS['RED'],
                             (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))
        elif nature == 'REPRODUCCION':
            pygame.draw.rect(screen, COLORS['PINK'],
                             (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))
        elif nature == 'MUERTE':  # Muerte por envejecimiento (celda en negro)
            pygame.draw.rect(screen, COLORS['BLACK'],
                             (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))
        elif nature == 'CRECIMIENTO':  # Crecimiento de hijo a adulto (celda en añil)
            pygame.draw.rect(screen, COLORS['INDIGO'],  
                             (pos[0] * cell_size, pos[1] * cell_size, cell_size, cell_size))

def draw_stats(screen, iteration, alive, stats, player, config):
    """Dibuja las estadísticas en pantalla."""
    # Ajustar el tamaño de la fuente según el ancho de la pantalla
    font_size = max(24, min(36, int(config.screen_width / 20)))  # Tamaño entre 24 y 36, ajustado al ancho de la pantalla
    font = pygame.font.SysFont(None, font_size)
    
    # Obtener las estadísticas
    reproductions, conflicts, deaths = stats.get_totals()
    
    # Texto de las estadísticas generales (parte superior)
    text_stats = (
        f"Ronda: {iteration} | Vivos: {alive} | Rep: {reproductions} | "
        f"Conf: {conflicts} | Muerte: {deaths}"    )
       
    # Renderizar los textos
    text_surface_stats = font.render(text_stats, True, COLORS['BLACK'])
    
    # Obtener las dimensiones de la pantalla
    _, screen_height = screen.get_size()
    
    # Dibujar las estadísticas en la parte superior izquierda
    screen.blit(text_surface_stats, (10, 10))
    
    # Dibujar la vida del jugador solo si existe
    if player is not None:
        text_vida = f"Edad Jugador: {player.age}"
        text_surface_vida = font.render(text_vida, True, COLORS['BLACK'])
        screen.blit(text_surface_vida, (10, screen_height - 40))  # 40 es un margen para que no esté pegado al borde

def draw_simulation(screen, player, individuals, stats, iteration, interactions, config, power=None, mode="Supervivencia", testing_mode=False):
    """Dibuja la simulación en la pantalla."""
    screen.fill(COLORS['WHITE'])
    draw_grid(screen, config)

    # Dibujar individuos
    if mode == "Supervivencia":
        draw_individuals(screen, player, individuals, config, power.is_active() if power else False)
    else:
        draw_individuals(screen, None, individuals, config)  # No hay jugador en Simulación

    # Dibujar interacciones
    draw_interactions(screen, interactions, config) 

    # Dibujar estadísticas
    draw_stats(screen, iteration, len(individuals), stats, player, config)  # Pasar config aquí

    # Dibujar estado del poder (solo en modo Supervivencia)
    if mode == "Supervivencia" and power:
        draw_power_status(screen, config, power)

    # Dibujar cartelito de modo testing (si está activado)
    if testing_mode:
        font = pygame.font.SysFont(None, 24)
        text = font.render("Modo Testing", True, COLORS['RED'])
        
        # Hacer el texto un poco transparente
        text.set_alpha(150)  # Valor entre 0 (totalmente transparente) y 255 (opaco)

        # Centrar el texto en la pantalla
        text_rect = text.get_rect(center=(config.screen_width // 2, config.screen_height // 2))
        screen.blit(text, text_rect)


    pygame.display.flip()

def draw_power_status(screen, config, power):
    """Dibuja el estado del poder en la pantalla (parte inferior derecha)."""
    # Ajustar el tamaño de la fuente según el ancho de la pantalla
    font_size = max(24, min(36, int(config.screen_width / 20)))  # Tamaño entre 24 y 36, ajustado al ancho de la pantalla
    font = pygame.font.SysFont(None, font_size)
    
    # Texto y color según el estado del poder
    if power.is_active():
        text = "Poder activo"
        color = COLORS['GREEN']
    elif power.cooldown > 0:
        text = f"Cooldown: {power.cooldown}"
        color = COLORS['RED']
    else:
        text = "Poder listo (SPACE)"
        color = COLORS['BLUE']
    
    # Renderizar el texto
    text_surface = font.render(text, True, color)
    
    # Posición del texto (esquina inferior derecha)
    text_rect = text_surface.get_rect(
        bottomright=(config.screen_width - 10, config.screen_height - 10))  # Margen de 10 píxeles
    
    # Dibujar el texto en la pantalla
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
            elif event.type == pygame.KEYDOWN:
                paused = False  # Salir de la pausa si se presiona una tecla

def handle_movement(event):
    """Procesa el evento de teclado y devuelve el movimiento correspondiente."""
    movement = [0, 0]
    if event.key == pygame.K_LEFT:
        movement[0] = -1
    elif event.key == pygame.K_RIGHT:
        movement[0] = 1
    elif event.key == pygame.K_UP:
        movement[1] = -1
    elif event.key == pygame.K_DOWN:
        movement[1] = 1
    return movement

def update_positions(player, individuals, movement, grid_width, grid_height):
    """Actualiza las posiciones del jugador y los demás individuos."""
    # Mover al jugador
    player.x += movement[0]
    player.y += movement[1]
    player.x = max(0, min(player.x, grid_width - 1))
    player.y = max(0, min(player.y, grid_height - 1))

    # Mover automáticamente el resto de los individuos
    for ind in individuals:
        if ind != player:
            ind.move(grid_width, grid_height)



# ---------------------- Funciones del fujo del juego ----------------------

def process_survival_interactions(player, individuals, stats, interactions, print_counter, iteration, testing_mode=False):
    """
    Procesa las interacciones entre los individuos y actualiza las estadísticas.
    :param iteration: Número de la ronda actual.
    :param testing_mode: Si es True, el jugador es invencible.
    """
    cells = {}
    for ind in individuals:
        pos = (ind.x, ind.y)
        if pos not in cells:
            cells[pos] = []
        cells[pos].append(ind)

    new_individuals = []
    for pos, inds in cells.items():
        if len(inds) > 1:
            # Procesar interacciones con el jugador
            if player in inds:
                for ind in inds:
                    if ind != player:
                        if ind.nature == 'RANDOM':
                            individual_nature = rd.choice(['HOSTIL', 'ALIADO'])
                        else:
                            individual_nature = ind.nature

                        if individual_nature == 'HOSTIL' and not testing_mode:  # El jugador solo muere si no está en modo testing
                            print(f"Ronda {iteration}: ¡El jugador ha sido atacado por un hostil en {pos}!")
                            print_counter += 1
                            stats.add_conflict(1)
                            interactions[pos] = 'CONFLICTO'
                            return False, print_counter  # El jugador muere
                        elif individual_nature == 'ALIADO' and not ind.is_child:  # Solo reproducirse con adultos
                            new_child = classEco.Individual(pos[0], pos[1], age=0, is_child=True)
                            new_individuals.append(new_child)
                            stats.add_reproduction()
                            interactions[pos] = 'REPRODUCCION'
                            print(f"Ronda {iteration}: ¡El jugador se ha reproducido en {pos}!")
                            player.age = max(0, player.age - 10)  # Rejuvenecer al reproducirse
                            print_counter += 1

            # Procesar interacciones entre otros individuos (sin cambios)
            else:
                for i, ind1 in enumerate(inds):
                    for ind2 in inds[i+1:]:
                        if ind1.nature == 'RANDOM':
                            nature_ind1 = rd.choice(['HOSTIL', 'ALIADO'])
                        else:
                            nature_ind1 = ind1.nature
                        if ind2.nature == 'RANDOM':
                            nature_ind2 = rd.choice(['HOSTIL', 'ALIADO'])
                        else:
                            nature_ind2 = ind2.nature

                        if nature_ind1 == 'HOSTIL' and nature_ind2 == 'HOSTIL':
                            print(f"Ronda {iteration}: ¡Conflicto entre dos hostiles en {pos}!")
                            print_counter += 1
                            stats.add_conflict(1)
                            interactions[pos] = 'CONFLICTO'
                            inds.remove(rd.choice([ind1, ind2]))

                        elif nature_ind1 == 'ALIADO' and nature_ind2 == 'ALIADO' and not ind1.is_child and not ind2.is_child:
                            new_child = classEco.Individual(pos[0], pos[1], age=0, is_child=True)
                            new_individuals.append(new_child)
                            stats.add_reproduction()
                            interactions[pos] = 'REPRODUCCION'
                            print(f"Ronda {iteration}: ¡Reproducción entre dos aliados en {pos}!")
                            print_counter += 1

                        else:
                            if rd.choice([True, False]):
                                if nature_ind1 == 'HOSTIL':
                                    inds.remove(ind2)
                                else:
                                    inds.remove(ind1)
                                stats.add_conflict(1)
                                interactions[pos] = 'CONFLICTO'
                                print(f"Ronda {iteration}: ¡Conflicto entre un hostil y un aliado en {pos}!")
                                print_counter += 1
                            else:
                                if not ind1.is_child and not ind2.is_child:
                                    new_child = classEco.Individual(pos[0], pos[1], age=0, is_child=True)
                                    new_individuals.append(new_child)
                                    stats.add_reproduction()
                                    interactions[pos] = 'REPRODUCCION'
                                    print(f"Ronda {iteration}: ¡Reproducción entre un hostil y un aliado en {pos}!")
                                    print_counter += 1

            new_individuals.extend(inds)
        else:
            new_individuals.extend(inds)

        # Actualizar crecimiento y envejecimiento
    for ind in new_individuals:
        has_grown = ind.grow()
        if has_grown:
            print(f"Ronda {iteration}: ¡Un hijo ha crecido y se ha convertido en adulto en {(ind.x, ind.y)}!")
            print_counter += 1
            interactions[(ind.x, ind.y)] = 'CRECIMIENTO'

        # Verificar si el jugador muere de vejez
        if ind == player and ind.age >= 33:
            if not testing_mode:  # En modo normal, el jugador muere de vejez
                print(f"Ronda {iteration}: ¡El jugador ha muerto de viejo en {(ind.x, ind.y)}!")
                print_counter += 1
                stats.add_death(1)
                interactions[(ind.x, ind.y)] = 'MUERTE'
                return False, print_counter  # El jugador muere de vejez
            # En modo testing, el jugador no muere ni se elimina de la lista

    # Filtrar individuos muertos (excepto el jugador en modo testing)
    if testing_mode:
        individuals[:] = [ind for ind in new_individuals if ind.age < 33 or ind == player]
    else:
        individuals[:] = [ind for ind in new_individuals if ind.age < 33]

    return True, print_counter  # El jugador sigue vivo

def regenerate_population(individuals, grid_width, grid_height, initial_individuals, max_individuals, iteration):
    """
    Regenera una cantidad de individuos igual a la mitad de los individuos iniciales cada 40 iteraciones.
    """
    def generate_individuals(quantity):
        """Genera nuevos individuos en celdas vacías."""

        # Identificar las celdas vacías
        occupied_cells = {(ind.x, ind.y) for ind in individuals}
        empty_cells = [(x, y) for x in range(grid_width) for y in range(grid_height) if (x, y) not in occupied_cells]

        # Devuelve la generación de individuos en esas celdas vacías
        return [classEco.Individual(x, y) for x, y in rd.sample(empty_cells, min(quantity, len(empty_cells)))]

    if iteration % 40 == 0 and iteration > 0 and len(individuals) < max_individuals:
        quantity_to_regenerate = initial_individuals // 2  # La cantidad a regenerar es la mitad de los que empezaron el juego.
        regenerated_individuals = generate_individuals(quantity_to_regenerate)
        individuals.extend(regenerated_individuals)
        print(f"¡Se han regenerado {len(regenerated_individuals)} individuos en la iteración {iteration}!")

def process_simulation_interactions(individuals, stats, interactions, print_counter, iteration):
    """
    Procesa las interacciones entre los individuos en el modo Simulación.
    :return: True si la simulación debe continuar, False si no quedan individuos vivos.
    """
    cells = {}
    for ind in individuals:
        pos = (ind.x, ind.y)
        if pos not in cells:
            cells[pos] = []
        cells[pos].append(ind)

    new_individuals = []
    for pos, inds in cells.items():
        if len(inds) > 1:  # Si hay más de un individuo en la celda
            # Procesar interacciones entre individuos
            for i, ind1 in enumerate(inds):
                for ind2 in inds[i+1:]:
                    if ind1.nature == 'RANDOM':
                        nature_ind1 = rd.choice(['HOSTIL', 'ALIADO'])
                    else:
                        nature_ind1 = ind1.nature
                    if ind2.nature == 'RANDOM':
                        nature_ind2 = rd.choice(['HOSTIL', 'ALIADO'])
                    else:
                        nature_ind2 = ind2.nature

                    if nature_ind1 == 'HOSTIL' and nature_ind2 == 'HOSTIL':
                        print(f"Ronda {iteration}: ¡Conflicto entre dos hostiles en {pos}!")
                        print_counter += 1
                        stats.add_conflict(1)
                        interactions[pos] = 'CONFLICTO'
                        inds.remove(rd.choice([ind1, ind2]))  # Eliminar un individuo al azar

                    elif nature_ind1 == 'ALIADO' and nature_ind2 == 'ALIADO' and not ind1.is_child and not ind2.is_child:
                        new_child = classEco.Individual(pos[0], pos[1], age=0, is_child=True)
                        new_individuals.append(new_child)
                        stats.add_reproduction()
                        interactions[pos] = 'REPRODUCCION'
                        print(f"Ronda {iteration}: ¡Reproducción entre dos aliados en {pos}!")
                        print_counter += 1

                    else:
                        if rd.choice([True, False]):  # Conflicto o reproducción aleatoria
                            if nature_ind1 == 'HOSTIL':
                                inds.remove(ind2)
                            else:
                                inds.remove(ind1)
                            stats.add_conflict(1)
                            interactions[pos] = 'CONFLICTO'
                            print(f"Ronda {iteration}: ¡Conflicto entre un hostil y un aliado en {pos}!")
                            print_counter += 1
                        else:
                            if not ind1.is_child and not ind2.is_child:
                                new_child = classEco.Individual(pos[0], pos[1], age=0, is_child=True)
                                new_individuals.append(new_child)
                                stats.add_reproduction()
                                interactions[pos] = 'REPRODUCCION'
                                print(f"Ronda {iteration}: ¡Reproducción entre un hostil y un aliado en {pos}!")
                                print_counter += 1

            new_individuals.extend(inds)
        else:
            new_individuals.extend(inds)

    # Actualizar crecimiento y envejecimiento
    for ind in new_individuals:
        has_grown = ind.grow()
        if has_grown:
            print(f"Ronda {iteration}: ¡Un hijo ha crecido y se ha convertido en adulto en {(ind.x, ind.y)}!")
            print_counter += 1
            interactions[(ind.x, ind.y)] = 'CRECIMIENTO'

        # Verificar si el individuo muere de vejez
        if ind.age >= 33:
            print(f"Ronda {iteration}: ¡Un individuo ha muerto de viejo en {(ind.x, ind.y)}!")
            print_counter += 1
            stats.add_death(1)  # Registrar la muerte en las estadísticas
            interactions[(ind.x, ind.y)] = 'MUERTE'  # Marcar la celda como muerte

    # Filtrar individuos muertos por envejecimiento
    individuals[:] = [ind for ind in new_individuals if ind.age < 33]

    # Verificar si no quedan individuos vivos
    if len(individuals) == 0:
        print("No quedan individuos vivos. Fin de la simulación")
        return False, print_counter  # La simulación termina

    return True, print_counter  # La simulación continúa

def survival_mode(config, difficulty, testing_mode=False):
    """Ejecuta la simulación en modo supervivencia."""
    try:
        difficulties = {"facil": 15, "medio": 25, "dificil": 40}
        initial_individuals = difficulties.get(difficulty.lower(), None)
        pygame.init()
        screen = pygame.display.set_mode((config.screen_width, config.screen_height))
        pygame.display.set_caption("Simulación de Supervivencia" + (" (Modo Testing)" if testing_mode else ""))

        # Generar individuos iniciales
        individuals = [classEco.Individual(rd.randint(0, config.grid_width - 1),
                      rd.randint(0, config.grid_height - 1)) for _ in range(initial_individuals)]
        player = individuals[0]
        stats = classEco.Stats()

        # Crear una instancia del poder del jugador
        power = classEco.PlayerPower()

        running = True
        iteration = 0
        interactions = {}
        print_counter = 0

        while running:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and power.is_ready():
                    power.activate()
                    show_temporary_message(screen, config, "¡Poder activado!")  # Mostrar mensaje
                movement = handle_movement(event)
                if movement != [0, 0]:
                    update_positions(player, individuals, movement, config.grid_width, config.grid_height)
                    interactions.clear()
                    running, print_counter = process_survival_interactions(player, individuals, stats, interactions, print_counter, iteration, testing_mode)

                    # Regenerar población (si corresponde)
                    regenerate_population(individuals, config.grid_width, config.grid_height, initial_individuals, config.max_individuals, iteration)

                    # Actualizar el estado del poder
                    power.update()

                    draw_simulation(screen, player, individuals, stats, iteration, interactions, config, power, mode="Supervivencia", testing_mode=testing_mode)
                    iteration += 1

                    # Limpiar la consola cada 10 rondas
                    if print_counter >= 10:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print_counter = 0

        show_end_game(screen, config)
        pygame.quit()

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        pygame.quit()

def simulation_mode(size_election, num_individuals, num_iterations, testing_mode=False):
    """ Ejecuta la simulación en modo Simulacion con el tamaño seleccionado. """
    try:
        # Configurar el tamaño del tablero
        config = classEco.Config(size_election.lower())
        
        # Inicializar Pygame
        pygame.init()
        screen = pygame.display.set_mode((config.screen_width, config.screen_height))
        pygame.display.set_caption("Simulación de Individuos" + (" (Modo Testing)" if testing_mode else ""))
        clock = pygame.time.Clock()

        # Creación de individuos y objeto estadística
        individuals = [classEco.Individual(rd.randint(0, config.grid_width - 1),
                                       rd.randint(0, config.grid_height - 1)) for _ in range(num_individuals)]
        stats = classEco.Stats()

        # Bucle principal de la simulación
        running = True
        iteration = 0
        interactions = {}  # Diccionario para registrar interacciones
        print_counter = 0  # Contador para limpiar la consola

        while running:
            # Captura de acciones del usuario (pausa y cierre del programa)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Finaliza la simulación si se cierra la ventana
                elif event.type == pygame.KEYDOWN and testing_mode:
                    iteration += 1  # Incrementamos el número de iteración

                    # Movimiento de los individuos en la simulación
                    for ind in individuals:
                        ind.move(config.grid_width, config.grid_height)

                    # Procesar interacciones entre individuos
                    interactions.clear()  # Limpiar interacciones de la iteración anterior
                    running, print_counter = process_simulation_interactions(individuals, stats, interactions, print_counter, iteration)

                    # Dibujar la simulación
                    draw_simulation(screen, None, individuals, stats, iteration, interactions, config, mode="Simulacion", testing_mode=testing_mode)

                    # Limpiar la consola cada 10 rondas
                    if print_counter >= 10:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print_counter = 0

            # Si no está en modo testing, avanzar automáticamente
            if not testing_mode:
                iteration += 1  # Incrementamos el número de iteración

                # Movimiento de los individuos en la simulación
                for ind in individuals:
                    ind.move(config.grid_width, config.grid_height)

                # Procesar interacciones entre individuos
                interactions.clear()  # Limpiar interacciones de la iteración anterior
                running, print_counter = process_simulation_interactions(individuals, stats, interactions, print_counter, iteration)

                # Dibujar la simulación
                draw_simulation(screen, None, individuals, stats, iteration, interactions, config, mode="Simulacion", testing_mode=testing_mode)

                # Limpiar la consola cada 10 rondas
                if print_counter >= 10:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print_counter = 0

                # Pausar si hay interacciones importantes
                if interactions:
                    pause_for_event()

                # Verificar si no quedan individuos vivos
                if len(individuals) == 0:
                    print("No quedan individuos vivos. Fin de la simulación")
                    break

                # Verificar si se han completado todas las iteraciones
                if iteration >= num_iterations:
                    print(f"Se han completado las {num_iterations} iteraciones. Fin de la simulación")
                    break

                # Controlar la velocidad de la simulación
                clock.tick(3)  # 3 iteraciones por segundo

        show_end_game(screen, config)
        pygame.quit()

    except Exception as e:
        print(f"Ocurrió un error: {e}")
        pygame.quit()




# ---------------------- Función principal del programa  ----------------------

def main():
    mode = start_screen()  

    if mode is None:
        print("Saliendo del programa...")
        return  
    
    if mode == "Supervivencia":
        options = survival_input_screen()
        if options is None:
            print("Supervivencia cancelada.")
            return  # Evita errores si el usuario cierra la ventana
        size_election, difficulty = options
        config = classEco.Config(size_election.lower())
        print(f"Iniciando supervivencia en tamaño {size_election} ({config.grid_width}x{config.grid_height})")
        survival_mode(config, difficulty, testing_mode=True)  # Modo Supervivencia

    if mode == "Simulacion":
        options = simulation_input_screen()
        if options is None:
            print("Simulación cancelada.")
            return  # Evita errores si el usuario cierra la ventana
        size_election, num_individuals, num_iterations = options
        config = classEco.Config(size_election.lower())
        print(f"Iniciando simulación en tamaño {size_election} ({config.grid_width}x{config.grid_height}) con {num_individuals} individuos y {num_iterations} iteraciones")
        simulation_mode(size_election, num_individuals, num_iterations, testing_mode=False)  

    pygame.quit()



# Punto de entrada principal del programa
if __name__ == "__main__":
    main()