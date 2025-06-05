import re
import funciones.validacion

encabezado = ["IDventa", "cantidad", "IDarticulo", "articulo", "importe", "IDcliente"] 

matriz_ventas = [
    ["001", "4", "01", "silla", "40000.00", "03"],
    ["002", "2", "05", "mesa de luz", "40000.00", "02"],
    ["003", "5", "03", "escritorios", "125000.00", "05"],
    ["004", "1", "02", "mesa", "30000.00", "01"],
    ["005", "3", "04", "sillon","150000.00", "04"]
    ]

ultimoID = 5

def agregar_venta(matriz, IDs):

    cantidad = funciones.validacion.validar_numeros("Cuantos registros de venta desea agregar?\n")
    bandera = True
    contador = 0
    
    while bandera:
        if contador == cantidad:
             bandera = False
        else:
            contador += 1
            
            idNuevo = str(int(IDs) + 1).zfill(3)

            cantidadProductos = funciones.validacion.validar_numeros(f"Ingrese la cantidad de productos de la venta N°{idNuevo}\n")
            producto = input(f"Ingrese el nombre del artículo vendido N°{idNuevo}\n")

            while True:
                coincide = re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+",producto)
                if coincide == None:
                    print("Solo se permiten el ingreso de letras")
                    producto = input("Ingrese nuevamente el nombre\n").strip()
                else:
                    break

            precio = funciones.validacion.validar_numeros(f"Ingrese el précio del producto N°{idNuevo}\n")
            IDcliente = funciones.validacion.validar_numeros(f"Ingrese el ID del comprador de la venta N°{idNuevo}\n")
            IDcliente = str(IDcliente).zfill(2)

            importe = str(int(precio) * int(cantidadProductos))
            importe += ".00"
            
            datos = [idNuevo, cantidadProductos, producto, importe, IDcliente]

            matriz.append(datos)

    return matriz, IDs

def editar_venta(matriz):

    cantidad = funciones.validacion.validar_numeros("Cuántos registros de venta desea editar?\n")
    bandera = True
    contador = 0

    while bandera:
        if cantidad == contador:
            bandera=False

        else:
            contador+=1

            print("1. Cantidad")
            print("2. Nombre Articulo")
            print("3. Importe")
            print("4. ID Cliente")

            cambio = funciones.validacion.validar_numeros("Qué valor desea editar?\n")

            while cambio > 4 or cambio < 1:
                cambio = funciones.validacion.validar_numeros("Ingrese una opción valida\n")

            idVenta = funciones.validacion.validar_numeros("Cuál es el ID de la venta?\n")
            entero_idVenta = int(idVenta)

            for i in range(len(matriz)):
                if matriz[i][0] == entero_idVenta:
                    break 

            if cambio == 1:
                matriz [entero_idVenta-1][cambio] = funciones.validacion.validar_numeros("Ingrese la cantidad de articulos\n")
                int(matriz [entero_idVenta-1][cambio])

            elif cambio == 2:
                matriz [entero_idVenta-1][cambio] = input("Ingrese el nombre articulo\n")
                
                while True:
                    coincide = re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+",matriz [int(entero_idVenta)-1][cambio])
                    if coincide == None:
                        print("Solo se permiten el ingreso de letras")
                        matriz [entero_idVenta-1][cambio] = input("Ingrese nuevamente el nombre\n").strip()
                    else:
                        break
            
            elif cambio == 3:
                importe = funciones.validacion.validar_numeros("Ingrese el importe total de la venta\n")
                matriz [entero_idVenta-1][cambio] = str(importe) + ".00"
            
            else:
                ID_cliente = funciones.validacion.validar_numeros("Ingrese el ID del cliente\n")
                matriz [idVenta-1][cambio] = str(ID_cliente).zfill(2)

    return matriz


def eliminar_venta(matriz):

    while True:
        id_a_eliminar = funciones.validacion.validar_numeros("Ingrese el ID de la venta que desea eliminar \n")
        id_a_eliminar = str(id_a_eliminar) 

        posicion = -1
        for i in range(len(matriz)):
            if matriz[i][0] == id_a_eliminar:
                posicion = i
                break 

        if posicion != -1:
            matriz.pop(posicion)
            print(f"La venta con ID N°{id_a_eliminar} fue eliminada correctamente.")
            break
        else:
            print("")
            print(f"No se encontró ninguna venta con ID N°{id_a_eliminar}")
            print("Por favor, intenta de nuevo")

    return matriz

        

    

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecución")