
class Autor:
    """ Clase Autor """
    def __init__(self, idNum: int, nombre: str, universidad: str, email: str):
        self._idNum = idNum
        self._nombre = nombre
        self._universidad = universidad
        self._email = email
        self.contribuciones = []
         
    
    #id getter
    @property
    def idNum(self):
        return self._idNum

    #id setter
    @idNum.setter
    def set_id(self, idNum):
        self._id = idNum

    #nombre getter
    @property
    def nombre(self):
        return self._nombre

    #nombre setter
    @nombre.setter
    def set_nombre(self, name):
        self._nombre = name

    #universidad getter
    @property
    def universidad(self):
        return self._universidad

    #universidad setter
    @universidad.setter
    def set_universidad(self, university):
        self._universidad = university   

    #email getter
    @property
    def email(self):
        return self._email

    #email setter
    @email.setter
    def set_email(self, email):
        self._email = email  

    #verificarCalificacion verifica si la contribución pertenece al autor, si se cumple,
    #la agrega a su lista de contribuciones y retorna la calificacion obtenida
    def verificarCalificación(self, contribucion):
        if contribucion._idAutor._idNum == self.idNum:
            self.contribuciones.append(contribucion)
            self.cantPublicaciones = len(self.contribuciones)
            print(f'El autor obtuvo {contribucion.calificacion} en su contribución')
        else:
            return 'La contribucion no pertenece al autor'

    #calcularPromedio encuentra las calificaciones de las publicaciones disponibles para un autor y retorna el promedio
    def calcularPromedio(self):
        acumulado = 0
        for contribucion in self.contribuciones:
            acumulado += (contribucion.calificacion)
            self.promedioCalificacion = acumulado/self.cantPublicaciones
        print(f'El promedio de calificacion es {self.promedioCalificacion}')

    #identifica la calificacion maxima de las publicaciones actuales del autor
    def obtenerCalificacionMax(self):
        max = 0
        for contribucion in self.contribuciones:
            if contribucion.calificacion > max:
                max = contribucion.calificacion
        self.calificacionMaxima = max
        print(f'La calificacion máxima del autor es {self.calificacionMaxima}')