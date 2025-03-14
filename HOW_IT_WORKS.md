# Cómo funciona el programa

Este documento explica el funcionamiento del programa **EcoSim**, que simula un ecosistema virtual con dos modos de juego: **Supervivencia** y **Simulación**. A continuación, se describen los aspectos clave del programa.

---

## ▶️ Inicialización

1. **Selección del modo**:
   - Al iniciar, el usuario elige entre **Supervivencia** o **Simulación**.
   - En **Supervivencia**, se configura el tamaño del tablero y la dificultad (fácil, medio, difícil), que determina el número de individuos iniciales.
   - En **Simulación**, se define el tamaño del tablero, el número de individuos y el número de iteraciones.

2. **Generación de individuos**:
   - Los individuos se colocan aleatoriamente en la cuadrícula.
   - Cada individuo tiene atributos como posición (`x`, `y`), edad (`age`), y tipo (`ALIADO`, `HOSTIL` o `RANDOM`).

---

## 🔄 Bucle de simulación (iteraciones)

El programa ejecuta un bucle principal que simula la evolución del ecosistema. A continuación, se describen las acciones clave:

### 🚶‍♀️ Movimiento
- **Jugador (modo Supervivencia)**:
  - Se mueve con las teclas de dirección (`↑`, `↓`, `←`, `→`).
  - Si intenta salir de la cuadrícula, su posición se ajusta para permanecer dentro de los límites.
- **Individuos (ambos modos)**:
  - Se mueven aleatoriamente en una de las 8 direcciones posibles.
  - Si salen de la cuadrícula, su posición se ajusta utilizando el módulo para "envolver".

### 🤝 Interacción
- **Agrupación por posición**:
  - Si dos o más individuos están en la misma celda, interactúan.
- **Tipos de interacción**:
  - **Reproducción (👶)**:
    - Dos individuos aliados adultos pueden reproducirse, generando un hijo (azul claro).
    - Los hijos tardan 5 iteraciones en crecer y convertirse en adultos.
  - **Conflicto (⚔️)**:
    - Dos individuos hostiles entran en conflicto, resultando en la muerte de uno.
  - **Interacción aleatoria**:
    - Un aliado y un hostil pueden reproducirse o entrar en conflicto, dependiendo de un valor aleatorio.

### 👴 Envejecimiento y muerte
- Cada individuo envejece 1 año por iteración.
- Si un individuo alcanza los 33 años, muere y es eliminado.

### 🔄 Regeneración de población (modo Supervivencia)
- Cada 40 iteraciones, se regenera la mitad de los individuos iniciales en celdas vacías.

### 💥 Eventos especiales
- **Crecimiento de hijos**:
  - Cuando un hijo se convierte en adulto, su celda se marca en añil.
- **Muerte por envejecimiento**:
  - La celda de un individuo que muere por envejecimiento se marca en negro.

---

## 👁️ Visualización y control

### 🎨 Colores de los individuos
- **Verde**: Jugador (modo Supervivencia).
- **Azul**: Individuos adultos.
- **Azul claro**: Hijos (en crecimiento).
- **Rosa, Rojo o Gris (solo con el poder activo)**:
  - **Rosa**: Aliados.
  - **Rojo**: Hostiles.
  - **Gris**: Aleatorios (pueden ser aliados o hostiles).

### 📊 Estadísticas
- Se muestran en la parte superior de la pantalla:
  - Ronda actual.
  - Individuos vivos.
  - Reproducciones, conflictos y muertes.

### 💥 Poder del jugador (modo Supervivencia)
- Se activa con la barra espaciadora (`SPACE`).
- Dura **4 rondas** y muestra los tipos de individuos:
  - **Rosa**: Aliados.
  - **Rojo**: Hostiles.
  - **Gris**: Aleatorios.
- El estado del poder (activo, en cooldown o listo) se muestra en la esquina inferior derecha.

---

## 🎯 Objetivos y peculiaridades de cada modo

### 🛡️ Modo Supervivencia
- **Objetivo**: Sobrevivir el máximo número de rondas.
- **Mecánicas clave**:
  - Controlas al jugador (verde) y debes evitar conflictos con hostiles.
  - Reproducirte con aliados rejuvenece al jugador **10 años** (sin años negativos).
  - Usa el poder para identificar aliados (rosa) y hostiles (rojo).
  - La población se regenera cada 40 iteraciones.
- **Finalización**: El modo termina cuando el jugador muere o el usuario cierra la ventana.

### 🧪 Modo Simulación
- **Objetivo**: Observar la evolución del ecosistema.
- **Mecánicas clave**:
  - Define el tamaño del mapa, el número de individuos y las iteraciones.
  - Las iteraciones avanzan automáticamente, pero se pausan en eventos.
  - Para continuar, presiona cualquier tecla.
- **Finalización**: El modo termina al completar las iteraciones, no quedar individuos vivos o cerrar la ventana.

---

## 🛠️ Modo Testing

### 🛡️ Modo Supervivencia (Testing)
- **Jugador invulnerable**:
  - No muere por conflictos ni envejecimiento.
- **Mensaje**: Se muestra **"Modo Testing"** en la pantalla.

### 🧪 Modo Simulación (Testing)
- **Avance manual**:
  - Las iteraciones avanzan solo al presionar una tecla.
- **Sin límite de iteraciones**:
  - La simulación solo termina si no quedan individuos vivos o se cierra la ventana.
- **Mensaje**: Se muestra **"Modo Testing"** en la pantalla.

---

## 🏁 Finalización

La simulación termina cuando:
- **Modo Simulación**: Se completan las iteraciones o no quedan individuos vivos.
- **Modo Supervivencia**: El jugador muere o el usuario cierra la ventana.

Al finalizar, se muestra **"THE END"** en la pantalla, y el programa espera a que el usuario presione una tecla o cierre la ventana.

---

¡Espero que esta explicación te sea útil! Si tienes alguna pregunta, consulta el código o abre un issue en el repositorio.