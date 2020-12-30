# Tarea 01: DCCumbre Olímpica :school_satchel:

## Consideraciones generales 

La tarea tiene todas las funcionalidades que se piden en el enunciado. Las consideraciones principales que hay que tener es en como se implementaron las funcionalidad, debido a que trabajé con ciertos supuestos que fueron invalidados durante el transcurso de la semana en algún issue. \

También quería decir que creo mi código no es muy eficiente, en general uso sólo lo que se enseñó en el curso para realizar cosas y creo que para algunas cosas podría haber investigado en internet. De todas formas, agradecería eternamente si el feedback puede incluir algo para mejorar la eficiencia. Estuve muchas horas haciendo esta tarea y creo que puede tener algo que ver con la forma en que codeo :(

### Cosas implementadas y no implementadas :white_check_mark: :x:

* Menús: :white_check_mark: 
* Consideración (:exclamation:): A la hora de elegir deportistas en menus (como por ejemplo, a la hora de fichar un deportista o elegir competidores) se debe usar el nombre considerando las mayus y minus.
    * Menu Principal: :white_check_mark:
    * Menu Entrenador: :white_check_mark: :exclamation:
    * Simular Competencias: :white_check_mark: :exclamation:
    * Mostrar Estado: :white_check_mark:
* Entidades :white_check_mark:
    * Delegaciones: Hecho completo :white_check_mark:
    * Deportistas: Hecho completo :white_check_mark:
    * Deportes: Hecho completo :white_check_mark:
    * Campeonato: Hecho completo :white_check_mark:
* Archivos
    * resultados.txt :white_check_mark:
    * parámetros :white_check_mark:

## Ejecución :computer:
El módulo principal de la tarea a ejecutar es   ```main.py```. No es necesario crear archivos adicionales


## Librerías :books:
### Librerías externas utilizadas
La lista de librerías externas que utilicé fue la siguiente:

1. ```random: choice() y uniform()```
2. ```abc: ABC y abstractmethod```

### Librerías propias
Por otro lado, los módulos que fueron creados fueron los siguientes:

1. ```menus```: Contiene a ```MenuInicio```, ```MenuPrincipal``` y ```MenuEntrenador```
2. ```campeonato```: Contiene ```Campeonato```, usada para simular campeonato
3. ```dia_competencia```: Contiene ```DiaCompetencia```, usada para simular cada día del campeonato
4. ```delegacion```: Contiene ```DelegacionIEEEsparta``` y ```DelegacionDCCrotona```
5. ```deportista```: Contiene ```Deportista```
6. ```deportes```: Contiene ```Deporte``` y como las clases heredadas de ```Deporte``` que representan cada deporte
7. ```tableros```: Contiene ```tablero_deportista()``` y ```tablero_delegacion()```, es llamada para imprimir estados del equipo y cada delegación y también mostrar deportistas disponibles.
8. ```parametros```: Contiene todos los parámetros de la simulación para evitar Hardcodeo

## Supuestos y consideraciones adicionales :thinking:
Los supuestos que realicé durante la tarea son los siguientes:

1. Los deportistas se lesionan alfinal de competir en un deporte y por lo tanto, la lesión tiene efecto para el próximo deporte. La verdad este supuesto lo hice después de ayudantía cuándo alguien preguntó algo similar, y entendí que esto era así. Me hace sentido también porque en general los deportistas terminan la competencia aún lesionados.

2. El entrenador de la delegación oponente no realiza acciones durante la simulación. Del enunciado dice que podemos nosotros elegir que hacer con el oponente, por lo que asumí que sólo el usuario realiza acciones como entrenador.

3. Cuando la delegación DCCrotona ocupa su habilidad especial, la medalla que gana es en un deporte (asumí Atletismo pero podría ser cualquiera) y todos los efectos que ganar una medalla se aplican normalmente, considerando también los del deportista (que se elige al azar para premiar)



-------

## Referencias de código externo :book:

Para realizar mi tarea saqué código de:
1. https://stackoverflow.com/questions/52952846/reading-from-text-file-with-namedtuple-entries : Leer el csv con namedtuple para adecuarse a los headers que se podrían mover.

