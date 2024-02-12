modelodedatos = ['nombre','telefono','email']

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
        print("Listamos registros");
    elif opcion == "2":
        print("Buscamos registros")
    elif opcion == "3":
        print("Insertamos registros")
    elif opcion == "4":
        print("Actualizamos registros")
    elif opcion == "5":
        print("Eliminamos registros")
    elif opcion == "6":
        print("Salimos")

    menu()

menu()
