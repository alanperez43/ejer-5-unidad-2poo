from alumnos import Alumnos
import csv
class Lista():
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def CargarLista(self):
        archivo=open("archivo.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            self.__lista.append(Alumnos(fila[0],int(fila[1]),int(fila[2]),int(fila[3]),))
        archivo.close()
    def mostrar(self,a,d):
        print(a,d)
        print("{}      {}".format("Alumno","Porcentaje"))
        for i in range(len(self.__lista)):
            
            if((int(self.__lista[i].getaño()) == a) and int((self.__lista[i].getd()) == d)):
                print("Alumno cargado al archivo")
                p=(self.__lista[i].getI()*100/self.__lista[i].getMI())
                
                j=str(self.__lista[i].getnom())
                print("{}      {}%".format(j,p))
            