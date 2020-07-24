## Ejercicio 1

Implementar las clases y los metodos descritos en la siguente figura, que representa un congreso de computación.


### Descrición del codigo

Clases: Autor, Contribucion, Ponencia, Taller

Se ejecuta un programa 'main' para representar la interaccion de las clases.
Las siguientes son las pruebas ejecutadas:

1. Creacion de 1 Autor
2. Creacion de 3 Talleres y 1 Ponencia, asignadas al "autor1"
3. Se ejecuta el método de Autor, verificarCalificacion(), el cual recibe una Contribucion (taller o ponencia ) como parametro y verifica si efectivamente pertenece al autor. En caso afirmativo, agrega la contribución al "autor", actualiza el numero de publicaciones del autor y retorna la calificacion correspondiente a esa Contribución.
4. Se ejecuta el método de Autor, calcularPromedio(), el cual revisa las Contribuciones cargadas a un Autor y retorna el promedio de sus calificaciones, para este programa el promedio es 93.
5. Se ejecuta el método de Autor , obtenerCalificacionMax(), el cual retorna la calificacion máxima de las Contribuciones actuales del Autor, para este programa la calificación máxima es 100.
6. Se verifica el numero actual de publicaciones para "autor1", debe corresponder a 4.
7. Se imprime el nombre del autor del "taller1", se crea un "autor2", se corre el método actualizarAutor() de Contribución con "autor2" como parametro. Se imprime el nombre del autor de "taller1", debe mostrar la actualización.