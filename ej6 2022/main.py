from menu import menuu
if __name__=='__main__':
    numeroV=int(input("ingrese el numero de viajero "))
    m=menuu()
    while(numeroV!=0):
        print("seleccione una opcion")
        print("a.consultar millas")
        print("b.acumular millas")
        print("c.canjear millas")
        print("0.salir")
        m.opcion4(numeroV)
        op=input('')
        m.opcion(op,numeroV)
        numeroV=int(input("ingrese el numero de viajero "))