import re
import funciones.validacion

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

encabezado = ["IDarticulo", "articulo", "precio"]


def agregar_producto(matriz,IDs):
    
    cantidad = funciones.validacion.validar_numeros("Cuantos productos nuevos desea agregar?\n")

    bandera = True
    contador = 0
    
    while bandera:
        if contador == cantidad:
             bandera = False
        else:
            contador += 1
            
            idNuevo = str(int(IDs) + 1).zfill(2) 
            producto = input(f"Ingrese el nombre del producto numero {idNuevo}\n")

            while True:
                coincide = re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", producto)
                if coincide == None:
                    print("Solo se permiten el ingreso de letras")
                    producto = input("Ingrese nuevamente el nombre:\n").strip()
                else:
                    break

            precio = funciones.validacion.validar_numeros(f"Ingrese el precio del producto numero {idNuevo}\n")
            cadena_precio = str(precio)
            cadena_precio += ".00"
            
            datos = [idNuevo, producto, cadena_precio]

            matriz.append(datos)

    IDs = idNuevo

    return matriz, IDs
 

def editar_producto(matriz):

    cantidad = funciones.validacion.validar_numeros("Cuantos productos desea editar?\n")
    bandera = True
    contador = 0

    while bandera:
        if cantidad == contador:
            bandera=False

        else:
            contador+=1

            print("1- Nombre del producto")
            print("2- Precio del producto")

            cambio = funciones.validacion.validar_numeros("Ingrese la columna que desea editar\n")

            while cambio > 2 or cambio < 1:
                cambio = funciones.validacion.validar_numeros("Ingrese una opcion valida\n")
            
            numeroCorrecto = False
            validacion = True
            while validacion:
                if numeroCorrecto == True:
                    validacion = False
                else:
                    idProducto = funciones.validacion.validar_numeros("Ingrese el ID del producto a modificar\n" )
                    idProducto = str(idProducto).zfill(2)
                    valor = funciones.validacion.buscar_numeros(matriz_productos, idProducto)
                    if valor == True:
                        numeroCorrecto = True
                    else:
                        print(f"El ID {idProducto} no fue encontrado. Por favor intente de nuevo!")
            

            if cambio == 1:
                matriz [int(idProducto)-1][cambio] = str(input("Ingrese el nombre del producto\n"))

                while True:
                    coincide = re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", matriz [int(idProducto)-1][cambio])
                    if coincide == None:
                        print("Solo se permiten el ingreso de letras")
                        matriz [int(idProducto)+1][cambio] = input("Ingrese nuevamente el nombre:\n").strip()
                    else:
                        break
            
            elif cambio == 2:
                importe = funciones.validacion.validar_numeros("Ingrese el precio\n")
                matriz [int(idProducto)-1][cambio] = str(importe) + ".00"

    return matriz

def eliminar_producto(matriz):
    
    numeroCorrecto = False
    validacion = True
    while validacion:
        if numeroCorrecto == True:
            validacion = False
        else:
            id_a_eliminar = funciones.validacion.validar_numeros("Ingrese el ID del producto a modificar\n" )
            id_a_eliminar = str(id_a_eliminar).zfill(2)
            valor = funciones.validacion.buscar_numeros(matriz_productos, id_a_eliminar)
            if valor == True:
                numeroCorrecto = True
            else:
                print(f"El ID {id_a_eliminar} no fue encontrado. Por favor intente de nuevo!")

    posicion = -1
    for i in range(len(matriz)):
         if matriz[i][0] == id_a_eliminar:
            posicion = i
                
    if posicion != -1:
        matriz.pop(posicion)
        print(f"El producto con ID N°{id_a_eliminar} fue eliminado correctamente.")

    return matriz

matriz_productos = txt_a_matriz("Proyecto-grupal-/funciones/productos.txt","r")

        
if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecución")