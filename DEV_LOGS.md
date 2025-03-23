# 📔 Diario de Desarrollo (DEV_LOG)

Este archivo documenta los errores, soluciones y decisiones tomadas durante el desarrollo del proyecto **EcoSys** a partir de la versión `ecoSys_v1.3`. Si deseas información sobre versiones anteriores, no dudes en contactarme.


***23/03/2025***
- Últimos retoques para lanzar la versión 2: 
  1. Traducción de nombres de funciones, variables y demás elementos al inglés. Los comentarios explicativos y los mensajes de impresión (prints) permanecen en español. Este es el formato estándar utilizado normalmente para facilitar la globalización.
  2. Reorganización del código principal, agrupando funciones por secciones o apartados.
- Durante esta jornada, descubrí que olvidé añadir que la simulación terminaría cuando se alcanzaran las iteraciones indicadas en el menú inicial. Esta funcionalidad ha sido añadida, aunque no está activa en el modo testing.

***18/03/2025***
- Toca investigar sobre el error que teníamos el otro día ('En el modo Simulación, muchos individuos desaparecen alrededor de la ronda 16-17 sin una razón aparente'). Para explorar la raíz del problema, he añadido prints que sirvan como 'log' del flujo. Me he dado cuenta que la lógica de la muerte por envejecimiento no estaba bien configurada en el modo simulación.
Tras configurarla bien, ahora compruebo que las 'desapariciones sin razon aparente' eran muerte por envejecimiento. Parece ser que hacía dos veces 'ind.age += 1' una en crecer() y otra en el flujo de procesar_interacciones_simulacion(). Borro esta última y solucionado.
- También he comprobado y corregido otros fallos: actualización clase Individuo (unificacion Individuo + Individuo_supervivencia), y control de cierre de ventanas a pygame.
---

## 📅 Registro de Cambios

### 🚀 **Versión 2**  | *ecoSys_v2*       (Fecha aproximada: 23/03/2025)
- **Cambios**:
  - Estandarización del idioma del código: traducción al inglés de funciones, variables y otros elementos. Los comentarios y mensajes de impresión (prints) permanecen en español.
  - Reorganización del código: tejora de la estructura del código para facilitar su mantenimiento y escalabilidad.
  - Corrección en simulation_mode(): se añadió la finalización de la partida cuando se alcanzan las iteraciones indicadas por el usuario, excepto en el modo testing.

### Versión 1.3 | *ecoSys_v1.3*       (Fecha aproximada: 13/03/2025 - 18/03/2025)
- **Cambios**:
  - Se rehizo el modo Simulación, integrando las funciones creadas para encapsular las funcionalidades principales.
  - Se integraron los modos Supervivencia y Simulación en un solo archivo.
  - Se mejoró la interfaz gráfica para adaptarse a diferentes tamaños de mapa.
  - Se añadió un modo Testing en el modo Simulación para facilitar la depuración.
  - Se cambió el nombre de 'MyOwnBioSist' / 'EcoSim' a **'EcoSys'**
  - Actualizada clase Individuo en clasesEcoSys 
  - Corregida lógica de muerte por envejecimiento a procesar_interacciones_simulacion()
  - Corregido error 'E001'.
  - Añadido control de cierre de ventana a pantalla_inicio(), input_screen_simulacion() y input_screen_supervivencia(). También requirió cambios en main()

- **Errores**:
  - ***E001***: 'En el modo Simulación, muchos individuos desaparecen alrededor de la ronda 16-17 sin una razón aparente'. **Solucion**: 'ind.age +=1' estaba duplicado (en crecer() y en flujo de procesar_interaciones_simulacion() y éste último ha sido eliminado).
- **Problema actual**: -
  - **Decisiones**: -

---

## 📝 Notas Adicionales

- **Contacto**: Si tienes preguntas o quieres más detalles sobre algún cambio, no dudes en contactarme a través de ***dcruzCoding@gmail.com***.

---

### ¡Gracias por seguir el desarrollo de EcoSys! 🚀