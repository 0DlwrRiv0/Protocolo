from ntpath import join
import os
from timeit import repeat
import itertools

def menu():
    print('''----------Menu----------
1. Nombre del protocolo
2. Agregar paso
3. Eliminar paso
4. Consulta los pasos existentes
5. Eliminar todo el protocolo
6. Salir 
-------------------------''')

protocolo = []
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

while True:
    menu()
    opc = int(input("¿Que quieres hacer?: "))
    if opc == 1:
        nombre= input("¿Cual es el nombre de tu protocolo?: ")
        print("------------------------")
        print("")
    elif opc == 2:
        a = input("Escriba el paso: ")
        protocolo.append(a)
        more = input ("¿Deseas escribir otro paso? si/no: ")
        if more == "si":
            pasos = int(input("¿Cuantos pasos vas a agregar?: "))
            for x in itertools.repeat(None, pasos):
                a = input("Escriba el paso: ")
                protocolo.append(a)
        elif more == "no":
            print("")
            menu() 
        else: 
            print("Opción indefinida")
            print("")
        print("------------------------")
        print("")
    elif opc == 3:
        elim = int(input("¿Que paso quieres eliminar? (la posicion inicial es 0): "))
        protocolo.pop(elim)
        print ("Se ha eliminado el paso",elim)
        print("------------------------")
        print("")
    elif opc == 4:
        union = list(zip(num, protocolo))
        for i in union:
            print(i)
        print("------------------------")
        print("")
    elif opc == 5:
        protocolo.clear()
        print("El protocolo ha sido eliminado")
        print("------------------------")
        print("")
    elif opc == 6:
        print("Hasta luego")
        break
    else:
        print("Escoja una opción valida")