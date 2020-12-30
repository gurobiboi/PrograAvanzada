# Tarea 00: DCCombateNaval :school_satchel:


## Consideraciones generales :octocat:

El juego comienza al correr el archivo main.py y se implementaron todos los requerimientos pedidos. 
Las consideraciones son las siguientes:

* La bomba diamante no explota como debería para radios de explosión suficientemente grandes, desde n = 4 empieza a tener problemas al añadir celdas extras :sob:
* Cuando se dispara y se acierta, hundiendo un barco, se obliga al jugador a lanzar una bomba. 
No se le da la opción de retirase del juego hasta que tire una bomba y falle
* Cuando el oponente dispara, elige una celda al azar sin importar su estado (descubierta o no) y después checkea su celda
para verificar que el disparo es válido. De no ser válido, se intenta denuevo. Esto ocupa innecesariamente muchos recursos, puede ser
 un problema para tamaños de tablero muy grandes.
* La modularización no fue la deseada. Si bien se respeto un tamaño máximo de 400 líneas, 
se concentró mucho código en el archivo partida.py (237 líneas)
* No puse comentarios en el código para las funciones. Pensé que se hacía en el READme por lo que me habían dicho,
hasta que leí la parte final del readme cuando ya era muy tarde.

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Menu Principal: Hecho completo
* Menu de juego: Me faltó dar la opción de salir del juego en todo momento
* Tabla de puntuaciones: Hecho completo


## Ejecución :computer:
El módulo principal de la tarea a ejecutar es  ```main.py```. Los archivos ```menu_principal.py```, 
```parametros.py```, ```partida.py```, ```tablero.py``` y ```tabla_puntajes.py``` deben estar todos en la misma carpeta que
```main.py```


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```Random```: ```función() randint``` para asignar los barcos y el turno del oponente.

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```menu_principal```: Contiene a ```MenuInicio```. Utilizada para llamar al menu principal desde main.py y 
pedir que opción desea realizar al jugador mediante input(). Comienza la partida mediante iniciar_partida().
2. ```partida```: Contiene a ```Partida```. Utilizada para jugar una partida. Carga un tablero, asigna barcos, realiza los turnos de cada jugador mediante
turno_jugador() y turno_oponente(), selecciona coordenada de bombas y las explota mediante introducir_coordenada() y explosion_bomba() y termina la partida.

3. ```tabla_puntajes```: Contiene a ```TablaPuntajes```. Utilizada para anotar nuevos puntajes (agregar()) y leer los actuales al printear.
## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Una persona no puede lanzar una bomba a una celda descubierta, aunque nunca haya lanzado una bomba a esa celda.
Considere como válido este supuesto según mi experiencia jugando el juego y considerando que no es útil lanzar una bomba a una celda descubierta 
(Con la excepción que se está lanzando una bomba especial, pero no se consideró este caso para romper la regla)


## Referencias de código externo :book:

Use stackoverflow principalmente para darme una idea de realizar ciertas cosas.

Para realizar mi tarea saqué código de:
1. \<https://stackoverflow.com/questions/4803999/how-to-convert-a-file-into-a-dictionary>: me ayudó a leer los puntajes y nombres a un diccionario
2. \<https://stackoverflow.com/questions/11228812/print-a-dict-sorted-by-values>: me ayudó a ordenar los puntajes de mayor a menor.

