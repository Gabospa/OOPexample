## Ejercicio 1

Implementar las clases y los metodos descritos en la siguente figura, que representa un congreso de computación.


### Descripción del codigo

Clases: Autor, Contribucion, Ponencia, Taller

Las clases Ponencia y Taller se extienden de la Clase Contribución, y heredan sus metodos.
Las clases Autor y Contribucion tienen una relacion "one-to-many" pues un autor puede tener multiples Contribuciones. 

Se ejecuta un programa 'main' para representar la interaccion de las clases.
Las siguientes son las pruebas ejecutadas:

1. Creacion de 1 Autor
2. Creacion de 3 Talleres y 1 Ponencia, asignadas al "autor1"
3. Se ejecuta el método de Autor, verificarCalificacion(), el cual recibe una Contribucion (taller o ponencia ) como parametro y verifica si efectivamente pertenece al autor. En caso afirmativo, agrega la contribución al "autor", actualiza el numero de publicaciones del autor y retorna la calificacion correspondiente a esa Contribución.
4. Se ejecuta el método de Autor, calcularPromedio(), el cual revisa las Contribuciones cargadas a un Autor y retorna el promedio de sus calificaciones, para este programa el promedio es 93.
5. Se ejecuta el método de Autor , obtenerCalificacionMax(), el cual retorna la calificacion máxima de las Contribuciones actuales del Autor, para este programa la calificación máxima es 100.
6. Se verifica el numero actual de publicaciones para "autor1", debe corresponder a 4.
7. Se imprime el nombre del autor del "taller1", se crea un "autor2", se corre el método actualizarAutor() de Contribución con "autor2" como parametro. Se imprime el nombre del autor de "taller1", debe mostrar la actualización.

## Ejercicio 2

Desarrolle una solucion que requiera la implementación de una clase abstracta y una implementación de Interfase, posterior a esto compare ambas soluciones y explique escenarios posibles de cuando es necesario utilizar cada una en un proyecto.


### Respuesta

Se realiza un caso básico para Python con los archivps
- abstract.py
- interface2.py

Las clases abstractas y las interfases se emplean para implementar herencia y definir comportamientos de los objetos. Pero tienen las siguientes diferencias:
- Las clases Abstractas pueden tener constructores, las Interfases no.
- Las clases Abstractas pueden tener metodos abstractos y no abstractos, las Interfases solo metodos abstractos.
- En las clases Abstractas se puede definir los permisos de acceso (public, private), en Interfases todos los metodos son publicos.

Las Clases Abstractas e Interfases no se manejan de la misma forma en todos los lenguajes:

- En Java las clases Abstractas se implementan con el keyword "extend", y las Interfases con "implements".
- En Java las clases Abstractas no soportan herencia multiple, en cambio las Interfases si pueden hacerlo. 
- En Python solo existen las clases abstractas, no tiene Interface, ya que si soportan la herencia multiple.

*Como elegir cual utilizar?*

Abtract Clases:
- Si hay clases relacionadas que requieren compartir codigo, este se "extiende" de la clase Abstracta
- Si se requiere iniciar variables que despues podran ser accesadas y modificadas via metodos
- Si se requiere asignar permisos de acceso a los metodos

Interfases:
- Si la abstraccion es total, y todos los metodos deben ser definidos por las subclases
- En el caso de Java, si se requiere Herencia Multiple
- Si se quiere especificar los metodos requeridos, pero no es importante quien o como los implementara.
