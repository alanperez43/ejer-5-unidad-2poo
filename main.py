from alumnos import Alumnos
from menu import Menu
from classlista import Lista
if __name__ == "__main__":
    lista=Lista()
    lista.CargarLista()
    
    #longitud=len(lista)
    #print(longitud)
    print("MENU")
    menu=Menu()
    op=None
    while(op!=4):
        print("|-----------------------------------------------------|")
        print("|1 para: Mostrar nombre y porcentaje                  |")
        print("|2 para: Modificar cantidad de Inacistencia Permitidas|")
        print("|3 para:test                                          |")
        print("|-----------------------------------------------------|")
        op=int(input("ingresar opcion: "))
        menu.opcion(op,lista)

