class Contribucion:
    """ Clase Contribución """
    def __init__(self, idNum, titulo , idAutor , calificacion):
        self._idNum = idNum
        self._titulo = titulo
        self._idAutor = idAutor
        self._calificacion = calificacion

    
    #id getter
    @property
    def idNum(self):
        return self._idNum

    #id setter
    @idNum.setter
    def set_id(self, idNum):
        self._idNum = idNum
       

    #titulo getter
    @property
    def titulo(self):
        return self._titulo

    #titulo setter
    @titulo.setter
    def set_titulo(self, titulo):
        self._titulo = titulo
        
    #calificación getter
    @property
    def calificacion(self):
        return self._calificacion

    #calificación setter
    @titulo.setter
    def set_calificacion(self, calificacion):
        self._calificacion = calificacion

    #actualizarAutor actualiza el autor de la contribucion de acuerdo al nuevo parametro idAutor   
    def actualizarAutor(self, nuevoAutor):
        self._idAutor = nuevoAutor