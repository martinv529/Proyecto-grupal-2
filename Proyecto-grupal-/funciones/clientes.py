import re
import funciones.validacion

idClientes = ["01", "02", "03", "04", "05"]
nombresClientes = ["lionel messi", "diego armando maradona", "martin palermo", "juan Roman Riqueleme", "clemente rodriguez"]

encabezado = ["ID", "Nombre y Apellido"]

# Crear el diccionario con zip
dic_clientes = dict(zip(idClientes, nombresClientes))

# Función para agregar nuevos clientes

def agregar_cliente(diccionario, listaID):

    cantidad = funciones.validacion.validar_numeros("Cuantos clientes nuevos desea agregar?\n")

    contador = 0
    bandera = True
    
    while bandera:
        if cantidad == contador:
            bandera = False
        else:
            contador += 1

            # Calcular el nuevo ID
            idAnterior = listaID[-1]  # Último ID actual
            idNuevo = str(int(idAnterior) + 1).zfill(2)  # Sumar 1 y mantener formato "01", "02", etc.

            # Pedir el nombre del nuevo cliente
            nombre = str(input(f"Ingrese el nombre y apellido del nuevo cliente número {contador}\n")).strip()

            
            while True:
                coincide = re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", nombre)
                if coincide == None:
                    print("Solo se permiten el ingreso de letras")
                    nombre = input("Ingrese nuevamente el nombre:\n").strip()
                else:
                    break

            #agrega el nombre al diccionario
            diccionario.setdefault(idNuevo, nombre)
            #agrega el nuevo ID a la lista de IDs
            listaID.append(idNuevo)

    return diccionario

def eliminar_cliente(dicclientes):
    listanombres = []
    id = funciones.validacion.validar_numeros("Ingrese el ID del cliente que desea eliminar\n")
    cadena_id = str(id).zfill(2)
    

    while cadena_id not in dicclientes:
        id = funciones.validacion.validar_numeros("Ingrese nuevamente un ID valido\n")
        cadena_id = str(id).zfill(2)

    dicclientes.pop(cadena_id)
    
    return dicclientes

def modificar_cliente(dicclientes):
    id = str(funciones.validacion.validar_numeros("Ingrese el ID del cliente que desea editar\n"))
    
    idint = int(id)
    largo = len(dicclientes)
    while idint > largo or idint <= 0:
        id = str(input("Ingrese un id dentro del rango para el reemplazo\n"))
        idint = int(id)
    cambio = str(input("Ingrese el nuevo nombre para el reemplazo\n"))
    dicclientes[id] = cambio
    return dicclientes

if __name__ == "__main__":
    # Este código solo se ejecutará cuando se ejecute ventas.py directamente
    print("Fin de la ejecucion")