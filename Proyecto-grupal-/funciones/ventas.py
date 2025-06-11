import re
import funciones.validacion
import funciones.articulos

encabezado = ["IDventa", "cantidad", "IDarticulo", "articulo", "importe", "IDcliente"] 

def txt_a_matriz(archivo, modo):
    try:
        matriz = []
        arch = open(archivo, modo, encoding="UTF-8")
        linea = arch.readline().strip()
        while linea:
            matriz.append(linea.split(";"))
            linea = arch.readline().strip()
    except OSError:
        print("No se pudo leer el archivo")
    finally:
        try:
            arch.close()
        except:
            print("No se pudo cerrar el archivo")
    return matriz

ultimoID = 5

multiplicar = lambda x, y: x * y

def agregar_venta(matriz_venta, IDs, matriz_producto):

    cantidad = funciones.validacion.validar_numeros("Cuantos registros de venta desea agregar?\n")
    bandera = True
    contador = 0
    
    while bandera:
        if contador == cantidad:
             bandera = False
        else:
            contador += 1
            
            idNuevo = str(int(IDs) + 1).zfill(3)

            cantidadProductos = int(funciones.validacion.validar_numeros(f"Ingrese la cantidad de productos de la venta N°{idNuevo}\n"))

            numeroCorrecto = False
            validacion = True
            while validacion:
                if numeroCorrecto == True:
                    validacion = False
                else:
                    IDarticulo = funciones.validacion.validar_numeros(f"Ingrese el N° de ID del artículo de la venta N°{idNuevo}\n")
                    IDarticulo = str(IDarticulo).zfill(2)
                    valor = funciones.validacion.buscar_numeros(matriz_producto, IDarticulo)
                    if valor == True:
                        numeroCorrecto = True
                    else:
                        print(f"El ID {IDarticulo} no fue encontrado. Por favor intente de nuevo!")

            IDcliente = funciones.validacion.validar_numeros(f"Ingrese el ID del comprador de la venta N°{idNuevo}\n")
            IDcliente = str(IDcliente).zfill(2)

            posicion = -1
            for i in range(len(matriz_producto)):
                if matriz_producto[i][0] == IDarticulo:
                    posicion = i

            precio = matriz_producto[posicion][2][:-3]
            precio = int(precio)

            importe = str(multiplicar(precio, cantidadProductos))
            importe += ".00"

            producto = matriz_producto[posicion][1]

            datos = [idNuevo, cantidadProductos, IDarticulo, producto , importe, IDcliente]

            matriz_venta.append(datos)

    return matriz_venta, IDs

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

            numeroCorrecto = False
            validacion = True
            while validacion:
                if numeroCorrecto == True:
                    validacion = False
                else:
                    idVenta = funciones.validacion.validar_numeros("Ingrese el ID del producto a modificar\n" )
                    idVenta = str(idVenta).zfill(3)
                    valor = funciones.validacion.buscar_numeros(matriz_ventas, idVenta)
                    if valor == True:
                        numeroCorrecto = True
                        enteroVenta = int(idVenta)
                    else:
                        print(f"El ID {idVenta} no fue encontrado. Por favor intente de nuevo!")

            if cambio == 1:
                matriz [enteroVenta-1][cambio] = funciones.validacion.validar_numeros("Ingrese la cantidad de articulos\n")
                int(matriz [enteroVenta-1][cambio])

            elif cambio == 2:
                matriz [enteroVenta-1][cambio] = input("Ingrese el nombre articulo\n")
                
                while True:
                    coincide = re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+",matriz [int(enteroVenta)-1][cambio])
                    if coincide == None:
                        print("Solo se permiten el ingreso de letras")
                        matriz [enteroVenta-1][cambio] = input("Ingrese nuevamente el nombre\n").strip()
                    else:
                        break
            
            elif cambio == 3:
                importe = funciones.validacion.validar_numeros("Ingrese el importe total de la venta\n")
                matriz [enteroVenta-1][cambio] = str(importe) + ".00"
            
            else:
                ID_cliente = funciones.validacion.validar_numeros("Ingrese el ID del cliente\n")
                matriz [enteroVenta-1][cambio] = str(ID_cliente).zfill(2)

    return matriz


def eliminar_venta(matriz):

    numeroCorrecto = False
    validacion = True
    while validacion:
        if numeroCorrecto == True:
            validacion = False
        else:
            id_a_eliminar = funciones.validacion.validar_numeros("Ingrese el ID de la venta que desea eliminar\n" )
            id_a_eliminar = str(id_a_eliminar).zfill(3)
            valor = funciones.validacion.buscar_numeros(matriz_ventas, id_a_eliminar)
            if valor == True:
                numeroCorrecto = True
                id_a_eliminar = str(id_a_eliminar) 
            else:
                print(f"El ID {id_a_eliminar} no fue encontrado. Por favor intente de nuevo!") 

        posicion = -1
        for i in range(len(matriz)):
            if matriz[i][0] == id_a_eliminar:
                posicion = i

        if posicion != -1:
            matriz.pop(posicion)
            print(f"La venta con ID N°{id_a_eliminar} fue eliminada correctamente.")
            
        else:
            print("")
            print(f"No se encontró ninguna venta con ID N°{id_a_eliminar}")
            print("Por favor, intenta de nuevo")

    return matriz

        
matriz_ventas = txt_a_matriz("Proyecto-grupal-/funciones/ventas.txt","r")
    

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecución")