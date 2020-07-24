from autor import Autor
from contribucion import Contribucion
from ponencia import Ponenecia
from taller import Taller


if __name__ == "__main__":
    autor1 = Autor(100,"Gabo", "Los Andes", "gabo@hey.com")
    taller1 = Taller(1, "Titulo1", autor1, 96, 200, 15)
    taller2 = Taller(2, "Titulo2", autor1, 100, 200, 15)
    ponencia3 = Ponenecia(3, "Titulo3", autor1, 80, "15/03", "Python")
    taller4 = Taller(4, "Titulo4", autor1, 96, 200, 15)
    autor1.verificarCalificación(taller1)
    autor1.verificarCalificación(taller2)
    autor1.verificarCalificación(ponencia3)
    autor1.verificarCalificación(taller4)
    autor1.calcularPromedio()
    autor1.obtenerCalificacionMax()
    print(autor1.cantPublicaciones)
    print(taller1._idAutor._nombre)
    autor2 = Autor(101, "Crisly", "Universidad", "crisly@hey.com")
    taller1.actualizarAutor(autor2)
    print(taller1._idAutor._nombre)

