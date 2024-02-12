modelodedatos = ['nombre','descripcion','precio','peso','medidas']

def menu():
    print("Escoge una opcion")
    print("1.-Listar registros")
    print("2.-Buscar registros")
    print("3.-Insertar registros")
    print("4.-Actualizar registros")
    print("5.-Eliminar registros")
    print("6.-Salir")
    opcion = input("Opción escogida:")
    if opcion == "1":
        print("Listamos registros")
        archivo = open("datos.txt",'r')
        for linea in archivo:
            print(linea)
        archivo.close()
    elif opcion == "2":
        print("Buscamos registros")
    elif opcion == "3":
        print("Insertamos registros")
        cadena = ""
        for entidad in modelodedatos:
            cadena += input("Introduce "+entidad+": ")+","
        cadena += "\n"
        print("Guardamos")
        archivo = open("datos.txt",'a')
        archivo.write(cadena)
        archivo.close()
    elif opcion == "4":
        print("Actualizamos registros")
    elif opcion == "5":
        print("Eliminamos registros")
    elif opcion == "6":
        print("Salimos")

    menu()

menu()
