# Tarea 02: DCCumbia
* Nombre: Sebastian Yanez
* Usuario: Gurobiboi
## Consideraciones generales 

El programa funciona bien, sin embargo, no se implementaron varias cosas como: Drag and Drop pinguirines, botón Pausa, Cheatcodes y Flechas múltiples.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Mecánicas de DCCumbia: Hecha completa :white_check_mark:
    * Pasos de Baile: Hecha completa, excepto pasos múltiples
    * Tipos de Flechas: No se implementaron las flechas congelar
    * Combo: Hecha completa  :white_check_mark:
    * Dificultad: Todas las flechas se mueven a la misma velocidad siempre
    * Fin del Nivel: Hecha completa  :white_check_mark:
    * Fin del Juego: Hecha completa  :white_check_mark:
* Interfaz gráfica: Hecha completa  :white_check_mark:
* Interacción del Usuario con DCCumbia:
    * Click: Hecha completa  :white_check_mark:
    * Atrapar Flechas: Hecha completa  :white_check_mark:
    * Movimiento pinguirines: No vuelve a la posición neutral al bailar. Además, sólo hay 1 pinguirin siempre (No se implemento D&D)
    * Pausa: No implementado :x:
    * Cheatcodes: No implementado :x:
    * Drag and Drop: No implementado :x:
* Archivos:
    * Sprites :white_check_mark:
    * Songs :white_check_mark:
    * ranking.txt :white_check_mark:
    * parametros.py :white_check_mark:
* Bonus: No se implementó ningún bonus :x:

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```archivo.py```. No se debe crear ningún archivo adicional.

## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```PyQt5```: Para QWidget, QApplication, QLabel, QThreads, QTimer, entre otros.
2. ``random``: para randint y choice

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

#### BackEnd (``/backend/``)
1. ```game_window```: Contiene a ```CurrentGame```, ```CurrentSong``` y maneja todo el backend de la ventana de juego. 
#### Frontend(``/frontend/``)
2. ```game_window```: Contiene a ```GameWindow``` y tiene el frontend de la ventaja de juego. No considera las flechas de la zona de ritmo, las cuales fuera implementadas del módulo rythm_zone
3. ```rythm_zone```: Contiene a ```RythmZone```, ``DanceMove`` y tiene el frontend de las flechas en la clase DanceMove. Mueve flechas y verifica visualmente que cuando se apreta una tecla haya una flecha en el lugar indicado.
3. ```rankings_window```: Contiene a ```RankingsWindow``` y tiene el frontend de la ventaja de rankings.
4. ```start_window```: Contiene a ```StartWindow``` y tiene el frontend de la ventaja de inicio.
5. ```summary_window```: Contiene a ```SummaryWindow``` y tiene el frontend de la ventaja de rankings.

Para el backend, no se hizo un archivo para la ventana de inicio debido a que la ventana era prácticamente sólo frontend. Para la ventana de rankings, el backend es el archivo ``rankings.txt`` y para la ventana de resumen, el backend se diseñó en conjunto con el backend del juego en el módulo game_window del backend.
## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

* La canción comienza cuándo empiezan a caer las flechas, y no cuando las flechas llegan a la zona de activación
* El largo de las ventanas no se moverá


## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. \<link de código>: este hace \<lo que hace> y está implementado en el archivo <nombre.py> en las líneas <número de líneas> y hace <explicación breve de que hace>
