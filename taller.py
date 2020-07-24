from contribucion import Contribucion

class Taller(Contribucion):
    def __init__(self, idNum, titulo, idAutor, calificacion, capacidadMaxima, duracion):
        super().__init__(idNum, titulo, idAutor, calificacion)
        self._capacidadMaxima = capacidadMaxima
        self._duracion = duracion
    

    #capacidad máxima getter
    @property
    def capacidadMaxima(self):
        return self._capacidadMaxima

    #capacidad máxima setter
    @capacidadMaxima.setter
    def capacidadMaxima(self, capacidad):
        self._capacidadMaxima = capacidad
    
    #duración getter
    @property
    def duracion(self):
        return self._duracion

    #duracion setter
    @duracion.setter
    def set_duracion(self, duracion):
        self._duracion = duracion