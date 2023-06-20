import numpy as np
from funcionesPython import *

rows = 10
columns = 10
# The order is always [rows][columns]
# [horizontal][vertical]

entradas = np.arange(1, rows * columns + 1).reshape(rows, columns).astype(str)

prices = np.array([50000, 100000, 200000])

ruts = np.empty(100, dtype=object)  # array con todos los ruts
nombres = np.empty(100, dtype=object)  # array con todos los ruts

compras = np.array([[0 for i in range(3)] for j in range(100)])  # i=ticket de cada precio j=cada persona
tickets_compras = np.array([[0 for i in range(3)] for j in range(100)])  # cantidad de tickets por tipo y persona

contadoresAsientos = [0, 0, 0]  # [0] normales [1] buenos [2] premium
datos_ingresados = [0, 0, 0, 0]  # [0]= index_ruts [1]= index_nombres [2]=index_compras b
asientos_comprados = []
asientos_persona = np.array([[0 for i in range(3)] for j in range(100)])

menu = True
while menu:
    # print(ruts)
    # print(nombres)
    # print(compras)
    print("---------Menú---------")
    print("1) Comprar asiento\n2) Ver datos de los clientes\n3) Ver asientos comprados y recaudación por clase de asiento.\n4) Salir\n")
    try:
        opcion = int(input("Su opción: "))
        if opcion == 1:
            rut = int(input("Por favor ingrese su RUT sin guión ni dígito verificador. Ejemplo: 12345678.\n"))
            if rut not in ruts and 1000000 < rut < 30000000:
                nombre = input("Por favor ingrese su nombre y apellido.\n")
                if len(nombre) > 6:
                    ruts[datos_ingresados[0]] = rut
                    nombres[datos_ingresados[1]] = nombre
                    datos_ingresados[0] += 1
                    datos_ingresados[1] += 1
                    maxSeats = 0
                    while maxSeats < 3:
                        print()
                        print_array(entradas)
                        print()
                        seat_number = input(f"Ingrese el asiento que desea comprar.\nLos asientos 1-20 son normales y tienen un precio de $50000.\nLos asientos 21-70 son buenos y cuestan $100000.\nLos asientos 71-100 son premium y cuestan $200000.\nUn rut solo puede comprar 3 pasajes. Usted ha comprado {maxSeats} pasajes.\n\n")
                        if seat_number in entradas:
                            reservation(seat_number, entradas)
                            asientos_comprados.append(seat_number)
                            asientos_persona[datos_ingresados[2]][maxSeats] = seat_number
                            seat_number_int = int(seat_number)
                            if 1 <= seat_number_int <= 20:
                                compra_tickets_asientos(0, compras, tickets_compras,contadoresAsientos)
                            elif 21 <= seat_number_int <= 70:
                                compra_tickets_asientos(1,compras,tickets_compras,contadoresAsientos)
                            else:
                                compra_tickets_asientos(2,compras,tickets_compras,contadoresAsientos)
                            print(f"Su cuenta va en {sum(compras[datos_ingresados[2]])}")
                            maxSeats += 1
                            if maxSeats < 3:
                                continuacion = int(input("¿Desea comprar más pasajes? \n1) Sí \n2) No\n"))
                                if continuacion == 1:
                                    pass
                                elif continuacion == 2:
                                    break
                        else:
                            print("El asiento ingresado no existe o ya está tomado.")
                    print(f"Ha comprado sus {maxSeats} pasajes.")
                    datos_ingresados[2] += 1  # se cambia el index para las compras de la siguiente persona. esta línea va aquí y no antes porque solo al salir de aquí se cambia de persona
                else:
                    print("Nombre no válido.")
            else:
                print("Rut no válido.")
        elif opcion == 2:
            rut_buscar = int(input("Ingrese el RUT del que desea buscar información:\n"))
            if rut_buscar in ruts:
                rut_index = np.where(ruts == rut_buscar)
                index = rut_index[0][0]
                print(f"Datos del cliente con rut {rut_buscar}:")
                print(f"Nombre: {nombres[index]}")
                print_client_purchase(0, index, tickets_compras, compras)
                print_client_purchase(1, index, tickets_compras, compras)
                print_client_purchase(2, index, tickets_compras, compras)
                print("Asientos comprados:", end=' ')
                for persona in asientos_persona[index]:
                    print(f"{persona}", end=', ')
                print()
                print(f"Total compra: ${sum(compras[index])}")
            else:
                print("Rut no encontrado.")
        elif opcion == 3:
            sumaCompras = np.sum(compras, axis=0)
            for i in range(3):
                if i == 0:
                    nombres = "normales"
                elif i == 1:
                    nombres = "buenos"
                elif i == 2:
                    nombres = "premium"
                print(f"Asientos {nombres} comprados: {contadoresAsientos[i]}")
                print(f"Recaudación total: {sumaCompras[i]}")
            print(f"Asientos comprados: {asientos_comprados}")
            print(f"Recaudación final: {np.sum(compras)}")
        elif opcion == 4:
            print("Gracias por usar este programa.")
            menu = False
        else:
            print("Opción inválida.")
    except Exception as e:
        print("Error:", str(e))

