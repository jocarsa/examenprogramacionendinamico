import sys

mantenimientos = ['productos','clientes','fechas']
modelodedatos = ['1','2','3']

productos = ['nombre','descripcion','precio','peso','medidas']
clientes = ['nombre','email','telefono']
fechas = ['fecha','pedido']

def menuprincipal():
    print("Escoge un mantenimiento:")
    for indice,opcion in enumerate(mantenimientos):
        print(indice,opcion)
    opcion = input("Escoge una opcion")
    indice = int(opcion)
    modelodedatos = globals()[mantenimientos[indice]]
    menu(modelodedatos,mantenimientos[indice])    

def menu(modelodedatos,opcionseleccionada):
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
        archivo = open(opcionseleccionada+".txt",'r')
        for linea in archivo:
            print(linea)
        archivo.close()
    elif opcion == "2":
        print("Buscamos registros")
        termino = input("Introduce el termino que buscar: ")
        archivo = open(opcionseleccionada+".txt",'r')
        for linea in archivo:
            if termino in linea:
                print(linea)
        archivo.close()
    elif opcion == "3":
        print("Insertamos registros")
        cadena = ""
        for entidad in modelodedatos:
            cadena += input("Introduce "+entidad+": ")+","
        cadena += "\n"
        print("Guardamos")
        archivo = open(opcionseleccionada+".txt",'a')
        archivo.write(cadena)
        archivo.close()
    elif opcion == "4":
        print("Actualizamos registros")
        termino = input("Introduce el termino que actualizar: ")
        archivo = open(opcionseleccionada+".txt",'r')
        contenido = ""
        for linea in archivo:
            if not termino in linea:
                contenido += linea
            else:
                for entidad in modelodedatos:
                    contenido += input("Introduce "+entidad+": ")+","
                contenido += "\n"
        archivo.close()
        archivo = open(opcionseleccionada+".txt",'w')
        archivo.write(contenido)
        archivo.close()
    elif opcion == "5":
        print("Eliminamos registros")
        termino = input("Introduce el termino que eliminar: ")
        archivo = open(opcionseleccionada+".txt",'r')
        contenido = ""
        for linea in archivo:
            if not termino in linea:
                contenido += linea
        archivo.close()
        archivo = open(opcionseleccionada+".txt",'w')
        archivo.write(contenido)
        archivo.close()
    elif opcion == "6":
        print("Salimos")
        sys.exit()

    menuprincipal()

menuprincipal()
