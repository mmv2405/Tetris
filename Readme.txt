Integrantes: Misael Martin 

Se ésta desarrollando un juego de Tetris utilizando la biblioteca Pygame. 
El objetivo del juego es mover y rotar piezas de distintas formas que caen en una matriz,
con el fin de llenar líneas horizontales completas y obtener la mayor cantidad de puntos.

Estructura general del proyecto:

1.Importación de bibliotecas y definición de variables: Importas las bibliotecas necesarias, 
    como Pygame, y defines variables globales y colores que usarás en todo el proyecto.

2.Funciones y métodos: Creas funciones y métodos para manejar distintas acciones del juego, 
    como mover y rotar piezas, detectar colisiones, actualizar la pantalla y el puntaje, pausar
    y reanudar el juego, y verificar si se ha llegado al final del juego.

3.Bucle principal del juego: Implementas un bucle while que mantiene el juego en ejecución,
    donde se manejan eventos como el movimiento y rotación de las piezas, la detección de líneas llenas, 
    la actualización del puntaje y el manejo de eventos de teclado.

4.Pantalla de juego: Utilizas Pygame para crear una ventana de juego donde se muestra la matriz, 
    las piezas y el puntaje actual.

5.Eventos de teclado: Capturas eventos de teclado para permitir al jugador mover y rotar las piezas, pausar el juego y salir de la aplicación.


--------------------------------------------------------------------------------------------
Es imprescindible instalar la biblioteca Pygame antes de ejecutar el programa.
Asegúrese de mantener presionadas las teclas durante un breve periodo para garantizar que el programa registre correctamente los movimientos.
Controles del Juego

Flecha izquierda: Desplazar la pieza hacia la izquierda.
Flecha derecha: Desplazar la pieza hacia la derecha.
Flecha arriba: Rotar la pieza en sentido horario.
Flecha abajo: Descender la pieza un nivel.

Espacio: Hacer que la pieza descienda rápidamente hasta el fondo.

Tecla P: Pausar el juego.
Tecla R: Reanudar el juego en curso.
Tecla Q: Finalizar y cerrar el juego.