import os 
import json
os.system("cls")

def cargar_json(url_archivo):
    with open(url_archivo, 'r') as archivo:
        return json.load(archivo)
    
def menu_geberal():
    os.system("cls")
    print("1. Crear empleado")
    print("2. Actualizar empleado")
    print("3. Eliminar empleado")
    print("4. Listar empleado")
    print("5. Salir")

def selecionar_opcio(max_opcion):
    opcion = 0
    while True:
        try:
            opcion = int(input("Seleccione una opcion >> "))
        except:
            pass
        if opcion < 1 or opcion > max_opcion:
            input("Opcion invalida, intente nuevamente >> ")
        else:
            return opcion


def iniciar_programa():
    while True:
        menu_geberal()
        opcion = selecionar_opcio(5)

        if opcion == 1:
            print("1. Crear empleado")
        elif opcion == 2:
            print("2. Actualizar empleado")
        elif opcion == 3:
            print("3. Eliminar empleado")
        elif opcion == 4:
            print("4. Listar empleado")
        elif opcion == 5:
            return

        input()

        empleado = cargar_json('empleado.json')
        print(empleado)

iniciar_programa()
