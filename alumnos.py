class Alumnos():
    __Nombre=None
    __año=None
    __Divicion=None
    __cantI=None#inasistencias
    cantMI=5#inasistencis maximas
    cantTC=20#clases totales
    def __init__(self,nom,año,div,i):

        self.__Nombre=nom
        self.__año=año
        self.__Divicion=div
        self.__cantI=i
        #self.__cantMI=mi
    def getnom(self):
        return self.__Nombre
    def getI(self):
        return self.__cantI
    @classmethod
    def getMI(cls):
        return cls.cantMI
    @classmethod
    def gettc(cls,cant):
        print(cls.cantTC)
        cls.cantTC=cant
        print(cls.cantTC)
    def getaño(self):
        return self.__año
    def getd(self):
        return self.__Divicion
    