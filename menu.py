from alumnos import Alumnos
class Menu():
    __menu=None
    def __init__(self):
        self.__menu={
            1:self.op1,
            2:self.op2,
            3:self.op3,
        }
    def opcion(self,op,lista=[]):
        func=self.__menu.get(op,lambda:print("opcion no valida"))
        if(op<1 or op>3):
            func()
        else:
            func(lista)
    def op1(self,lista):
        a=input("Ingresar año del alumno: ")
        d=input("Ingresar division: ")
        while(any(chr.isdigit() for chr in a)== False and (any(chr.isdigit() for chr in d)== False)):
            print("ingreso mal de datos ")
            a=input("Ingresar año del alumno: ")
            d=input("Ingresar division: ")
        print(type(a),d)
        lista.mostrar(int(a),int(d))

    def op2(self,lista):
        m=input("Ingresar nueva cantidad maxima de inasistencias: ")
        while(any(chr.isdigit() for chr in m)==False):
            print("dato mal ingresado")
            m=input("Ingresar nueva cantidad maxima de inasistencias: ")
    
        Alumnos.gettc(int(m))
    def op3(self,lista):
        lista.mostrar(1,5)
        lista.mostrar(3,3)
        lista.mostrar(4,6)
        Alumnos.gettc(10)
        Alumnos.gettc(20)
        Alumnos.gettc(12)

