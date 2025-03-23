# 🌿 EcoSys: Simulación de Ecosistemas

EcoSys es un proyecto de simulación que modela la interacción entre individuos en un ecosistema virtual. El programa permite dos modos de juego: **Simulación** y **Supervivencia**, cada uno con diferentes reglas y objetivos. A continuación, se describe el funcionamiento general del programa y las características técnicas de la versión actual.


## 🌍 Descripción General

### ¿Qué es EcoSys?
EcoSys es una simulación que recrea un ecosistema virtual donde los individuos interactúan entre sí, pudiendo reproducirse, competir o morir. El objetivo del proyecto es explorar cómo las interacciones entre individuos afectan la dinámica de la población a lo largo del tiempo.

### 🎮 Modos de Juego
1. **🛡️ Modo Supervivencia**:
   - **🎯 Objetivo**: Sobrevivir el máximo número de rondas posible.
   - **⚙️ Mecánicas**:
     - Controlas a un jugador (🟢 verde) que debe evitar conflictos con individuos hostiles.
     - Para sobrevivir, intenta reproducirte con individuos aliados. Cada reproducción rejuvenece al jugador **10 años** (sin años negativos).
     - Usa un **✨ poder especial** para identificar a los individuos aliados (🌸 rosa) y hostiles (🔴 rojo) durante 4 rondas.
     - La población se regenera cada 40 iteraciones, añadiendo nuevos individuos al ecosistema.
   - **⏹️ Finalización**: El modo termina cuando el jugador muere (por conflicto o envejecimiento) o cuando el usuario cierra la ventana.
   - **🧪 Modo Testing**: Permite probar el código sin que el jugador muera, ideal para desarrollo y depuración.

2. **🧪 Modo Simulación**:
   - **🎯 Objetivo**: Observar cómo evoluciona el ecosistema bajo condiciones iniciales definidas por el usuario.
   - **⚙️ Mecánicas**:
     - El usuario define el tamaño del mapa, el número de individuos y el número de iteraciones.
     - Las iteraciones avanzan automáticamente, pero el programa se pausa cuando ocurre un evento (👶 reproducción, ⚔️ conflicto, 💀 muerte o 🌱 crecimiento).
     - Para continuar, el usuario debe presionar cualquier tecla.
   - **⏹️ Finalización**: El modo termina cuando se completan todas las iteraciones, no quedan individuos vivos o el usuario cierra la ventana.
   - **🧪 Modo Testing**: Permite avanzar manualmente las iteraciones, ideal para probar el comportamiento del ecosistema paso a paso.


## 💻 Funcionalidad y Características del Código (Versión Actual)

### 🛠️ Tecnologías Utilizadas
- **🧑‍💻 Lenguaje**: Python 3.x.
- **🎨 Librería gráfica**: `pygame` para la interfaz gráfica.
- **🎲 Módulos adicionales**: `random` para la generación de valores aleatorios y `os` para la limpieza de la consola.

### 🏗️ Estructura del Código
El código está organizado en clases y funciones principales:

#### 🧩 Clases Principales
- **`Individual`**:
  - Representa a un individuo en el ecosistema, con atributos como posición (`x`, `y`), edad (`age`), y tipo (`ALIADO`, `HOSTIL` o `RANDOM`).
- **`Stats`**:
  - Lleva un registro de las interacciones (👶 reproducciones, ⚔️ conflictos y 💀 muertes).
- **`Config`**:
  - Configura el tamaño del tablero y otros parámetros globales.
- **`PowerPlayer`**:
  - Gestiona el poder especial del jugador en modo Supervivencia.

#### 🛠️ Funciones Principales
- **`start_screen()`**: Muestra la pantalla inicial para seleccionar el modo de juego.
- **`survival_input_screen()`**: Permite configurar el tamaño del tablero y la dificultad en modo Supervivencia.
- **`simulation_input_screen()`**: Permite configurar el tamaño del tablero, el número de individuos y las iteraciones en modo Simulación.
- **`survival_mode()`**: Ejecuta el modo Supervivencia.
- **`simulation_mode()`**: Ejecuta el modo Simulación.
- **`draw_simulation()`**: Contiene las funciones de dibujo (`draw_grid()`, `draw_individuos()`, `draw_interacciones()`, etc.) que renderizan la simulación en la pantalla.
- ...

### 📋 Requisitos
- Python 3.x.
- Biblioteca `pygame` (instalable con `pip install pygame`).

### 🚀 Ejecución
Para ejecutar el programa, simplemente ejecuta el archivo principal.

Actualmente el archivo principal con la versión más reciente es -----> [**ecoSys_v2.py**](./Version2/ecoSys_v2.py)



## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el proyecto, sigue estos pasos:

- Haz un fork del repositorio.
- Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
- Realiza tus cambios y haz commit (git commit -m 'Añade nueva funcionalidad').
- Haz push a la rama (git push origin feature/nueva-funcionalidad).
- Abre un Pull Request y describe tus cambios.
- Las mejoras en la interfaz, la optimización del código y la adición de nuevas características son especialmente bienvenidas. ¡Gracias por tu interés en contribuir! 😊


## 📜 Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.
