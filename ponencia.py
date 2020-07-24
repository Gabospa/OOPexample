from contribucion import Contribucion

class Ponenecia(Contribucion):
    def __init__(self, idNum, titulo, idAutor, calificacion, fechaPublicacion, ejeTematico):
        super().__init__(id, titulo, idAutor, calificacion)
        self._fechaPublicacion = fechaPublicacion
        self._ejeTematico = ejeTematico
    

    #fecha publicacion getter
    @property
    def fechaPublicacion(self):
        return self._fechaPublicacion

    #fecha publicacion setter
    @fechaPublicacion.setter
    def set_fechaPublicacion(self, fecha):
        self._fechaPublicacion = fecha
    
    #eje temático getter
    @property
    def ejeTematico(self):
        return self._ejeTematico

    #eje temático setter
    @ejeTematico.setter
    def set_ejeTematico(self, tema):
        self._ejeTematico = tema