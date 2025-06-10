import funciones.ventas
import funciones.articulos
import funciones.clientes
import funciones.validacion

cortar = lambda texto: texto[:15] + "..." if len(texto) > 15 else texto

def mostrar_menu():
    print(" ")
    print("*** MENÚ PRINCIPAL ***")
    print(" ")
    print("1. Listado de todos los articulos y precios")
    print("2. Listado de todos los clientes")
    print("3. Listado de todas las ventas")
    print("4. Estadísticas de ventas por articulos")
    print("5. Estadísticas de ventas por clientes")
    print("6. Estadísticas de ventas por producto en específico ")
    print("7. Estadísticas de ventas por cliente en específico ")
    print("0. Salir")
 
    bandera = True
    while bandera:

        eleccion = input("Seleccione su opción (0-7) \n").strip()

        try:
            eleccion = int(eleccion)
        except ValueError:
            if eleccion == "":
                print("No se admiten espacios en blanco!\n")
                continue
            else:
                print("Solo se admiten numeros!\n")
                continue

        if eleccion == 1:
            opcion1=True
            while opcion1:
                print("OPCIÓN 1")
                print("1. Imprimir listado de articulos")
                print("2. agregar articulo/s")
                print("3. Editar articulo/s")
                print("4. Eliminar articulo/s")
                print("0. Volver al menú principal")

                opcion = input("Ingrese la opcion que desea\n")

                try:
                    opcion = int(opcion)
                except ValueError:
                    if opcion == "":
                        print("No se admiten espacios en blanco!\n")
                        continue
                    else:
                        print("Solo se admiten numeros!\n")
                        continue
                    
                
                if opcion == 1:
                    funciones.articulos.productos = [dict(zip(funciones.articulos.encabezado,fila))for fila in funciones.articulos.matriz_productos]
                    print(f"{funciones.articulos.encabezado[0]:<15} | {funciones.articulos.encabezado[1]:<20} | {funciones.articulos.encabezado[2]:>5}")
                    for producto in funciones.articulos.productos:
                        articulo_corto = cortar(producto['articulo'])
                        print(f"{producto['IDarticulo']:<15} | {articulo_corto:<20} | ${producto['precio']:>10}")

                elif opcion == 2:
                    funciones.articulos.matriz_productos, funciones.articulos.ultimoID = funciones.articulos.agregar_producto(funciones.articulos.matriz_productos, funciones.articulos.ultimoID)
                    funciones.articulos.productos = [dict(zip(funciones.articulos.encabezado,fila))for fila in funciones.articulos.matriz_productos]
                    print(f"{funciones.articulos.encabezado[0]:<15} | {funciones.articulos.encabezado[1]:<20} | {funciones.articulos.encabezado[2]:>5}")
                    for producto in funciones.articulos.productos:
                        articulo_corto = cortar(producto['articulo'])
                        print(f"{producto['IDarticulo']:<15} | {articulo_corto:<20} | ${producto['precio']:>10}")

                elif opcion == 3:
                    funciones.articulos.matriz_productos = funciones.articulos.editar_producto(funciones.articulos.matriz_productos)
                    funciones.articulos.productos = [dict(zip(funciones.articulos.encabezado,fila))for fila in funciones.articulos.matriz_productos]
                    print(f"{funciones.articulos.encabezado[0]:<15} | {funciones.articulos.encabezado[1]:<20} | {funciones.articulos.encabezado[2]:>5}")
                    for producto in funciones.articulos.productos:
                        articulo_corto = cortar(producto['articulo'])
                        print(f"{producto['IDarticulo']:<15} | {articulo_corto:<20} | ${producto['precio']:>10}")

                elif opcion == 4:
                    funciones.articulos.matriz_productos = funciones.articulos.eliminar_producto(funciones.articulos.matriz_productos)
                    funciones.articulos.productos = [dict(zip(funciones.articulos.encabezado,fila))for fila in funciones.articulos.matriz_productos]
                    print(f"funciones.{funciones.articulos.encabezado[0]:<15} | {funciones.articulos.encabezado[1]:<20} | {funciones.articulos.encabezado[2]:>5}")
                    for producto in funciones.articulos.productos:
                        articulo_corto = cortar(producto['articulo'])
                        print(f"{producto['IDarticulo']:<15} | {articulo_corto:<20} | ${producto['precio']:>10}")

                elif opcion == 0:
                    opcion1 = False
                else: 
                    print(" ")
                    print("Opción no válida. Intenta de nuevo.")

        elif eleccion == 2:
            opcion2 = True
            while opcion2:
                print("OPCIÓN 2")
                print("1. Imprimir listado de clientes")
                print("2. agregar cliente/s")
                print("3. Editar cliente/s")
                print("4. Eliminar cliente/s")
                print("0. Volver al menú principal")

                opcion = input("Ingrese la opcion que desea\n")  

                try:
                    opcion = int(opcion)
                except ValueError:
                    if opcion == "":
                        print("No se admiten espacios en blanco!\n")
                        continue
                    else:
                        print("Solo se admiten numeros!\n")
                        continue

                if opcion == 1:
                    print(f"{funciones.clientes.encabezado[0]:<5} | {funciones.clientes.encabezado[1]:<10}")
                    for id_cliente, nombre_cliente in funciones.clientes.dic_clientes.items():
                        print(f"{id_cliente:5} | {nombre_cliente:4}")

                elif opcion == 2:
                    funciones.clientes.dic_clientes = funciones.clientes.agregar_cliente(funciones.clientes.dic_clientes, funciones.clientes.idClientes)
                    print(f"{funciones.clientes.encabezado[0]:<5} | {funciones.clientes.encabezado[1]:<10}")
                    for id_cliente, nombre_cliente in funciones.clientes.dic_clientes.items():
                        print(f"{id_cliente:5} | {nombre_cliente:4}")

                elif opcion == 3:
                    funciones.clientes.dic_clientes = funciones.clientes.modificar_cliente(funciones.clientes.dic_clientes)
                    print(f"{funciones.clientes.encabezado[0]:<5} | {funciones.clientes.encabezado[1]:<10}")
                    for id_cliente, nombre_cliente in funciones.clientes.dic_clientes.items():
                        print(f"{id_cliente:5} | {nombre_cliente:4}")

                elif opcion == 4:
                    funciones.clientes.dic_clientes = funciones.clientes.eliminar_cliente(funciones.clientes.dic_clientes)
                    print(f"{funciones.clientes.encabezado[0]:<5} | {funciones.clientes.encabezado[1]:<10}")
                    for id_cliente, nombre_cliente in funciones.clientes.dic_clientes.items():
                        print(f"{id_cliente:5} | {nombre_cliente:4}")
                
                elif opcion == 0:
                    opcion2 = False
                else: 
                    print(" ")
                    print("Opción no válida. Intenta de nuevo.")

        elif eleccion == 3:
            opcion3 = True
            while opcion3:
                print("OPCIÓN 3")
                print("1. Imprimir listado de ventas")
                print("2. agregar venta/s")
                print("3. Editar venta/s")
                print("4. Eliminar venta/s")
                print("0. Volver al menú principal")
                    
                opcion = input("Ingrese la opcion que desea\n")

                try:
                    opcion = int(opcion)
                except ValueError:
                    if opcion == "":
                        print("No se admiten espacios en blanco!\n")
                        continue
                    else:
                        print("Solo se admiten numeros!\n")
                        continue


                if opcion == 1:
                    print(f"{funciones.ventas.encabezado[0]:<10} | {funciones.ventas.encabezado[1]:<10} | {funciones.ventas.encabezado[2]:<15} | {funciones.ventas.encabezado[3]:<15} | {funciones.ventas.encabezado[4]:<16} | {funciones.ventas.encabezado[5]:<5}")
                    for fila in funciones.ventas.matriz_ventas:
                        IDnuevo, cantidadProductos, IDarticulo, nombre, importe, IDcliente = fila
                        nombre_corto = cortar(nombre)
                        print(f"{IDnuevo:<5} | {cantidadProductos:<10} | {IDarticulo:<15} | {nombre_corto:<15} | ${importe:<15} | {IDcliente:>10}")

                elif opcion == 2:
                    funciones.ventas.matriz_ventas, funciones.ventas.ultimoID = funciones.ventas.agregar_venta(funciones.ventas.matriz_ventas, funciones.ventas.ultimoID, funciones.articulos.matriz_productos)
                    print(f"{funciones.ventas.encabezado[0]:<10} | {funciones.ventas.encabezado[1]:<10} | {funciones.ventas.encabezado[2]:<15} | {funciones.ventas.encabezado[3]:<15} | {funciones.ventas.encabezado[4]:<16} | {funciones.ventas.encabezado[5]:<5}")
                    for fila in funciones.ventas.matriz_ventas:
                        IDnuevo, cantidadProductos, IDarticulo, nombre, importe, IDcliente = fila
                        nombre_corto = cortar(nombre)
                        print(f"{IDnuevo:<5} | {cantidadProductos:<10} | {IDarticulo:<15} | {nombre_corto:<15} | ${importe:<15} | {IDcliente:>10}")

                elif opcion == 3:
                    funciones.ventas.matriz_ventas=funciones.ventas.editar_venta(funciones.ventas.matriz_ventas)
                    print(f"{funciones.ventas.encabezado[0]:<10} | {funciones.ventas.encabezado[1]:<10} | {funciones.ventas.encabezado[2]:<15} | {funciones.ventas.encabezado[3]:<15} | {funciones.ventas.encabezado[4]:<16} | {funciones.ventas.encabezado[5]:<5}")
                    for fila in funciones.ventas.matriz_ventas:
                        IDnuevo, cantidadProductos, IDarticulo, nombre, importe, IDcliente = fila
                        nombre_corto = cortar(nombre)
                        print(f"{IDnuevo:<5} | {cantidadProductos:<10} | {IDarticulo:<15} | {nombre_corto:<15} | ${importe:<15} | {IDcliente:>10}")

                elif opcion == 4:
                    funciones.ventas.matriz_ventas = funciones.ventas.eliminar_venta(funciones.ventas.matriz_ventas)
                    print(f"{funciones.ventas.encabezado[0]:<10} | {funciones.ventas.encabezado[1]:<10} | {funciones.ventas.encabezado[2]:<15} | {funciones.ventas.encabezado[3]:<15} | {funciones.ventas.encabezado[4]:<16} | {funciones.ventas.encabezado[5]:<5}")
                    for fila in funciones.ventas.matriz_ventas:
                        IDnuevo, cantidadProductos, IDarticulo, nombre, importe, IDcliente = fila
                        nombre_corto = cortar(nombre)
                        print(f"{IDnuevo:<5} | {cantidadProductos:<10} | {IDarticulo:<15} | {nombre_corto:<15} | ${importe:<15} | {IDcliente:>10}")
                            
                elif opcion == 0:
                    opcion3 = False
                else: 
                    print(" ")
                    print("Opción no válida. Intenta de nuevo.")
                    
        elif eleccion == 4:
            print("Hola opcion 4")
        elif eleccion == 5:
            print("Hola opcion 5")
        elif eleccion == 6:
            print("Hola opcion 6")
        elif eleccion == 7:
            print("Hola opcion 7")
        elif eleccion == 0:
            print("Saliste del programa.")
            bandera = False
        else:
            print(" ")
            print("Opción no válida. Intenta de nuevo.")

mostrar_menu()