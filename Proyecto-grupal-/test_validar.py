#Esta funcion funciona correctamente ya que elimina el ID especificado
def eliminar_producto():

    matriz =[
    ["01", "silla", "10000.00"], 
    ["02","mesa","30000.00"],
    ["03","escritorio","25000.00"],
    ]

    valor= "03"

    while True:

        posicion = -1
        for i in range(len(matriz)):
            if matriz[i][0] == valor:
                posicion = i
                break 

        if posicion != -1:
            matriz.pop(posicion)
            print(f"El producto con ID N°{valor} fue eliminado correctamente.")
            break
        else:
            print("")
            print(f"No se encontró ningún producto con ID N°{valor}")
            print("Por favor, intenta de nuevo")

    largo_matriz = len(matriz)

    return matriz, largo_matriz

#Esta funcion agrega en vez de eliminar
def eliminar_producto():

    matriz =[
    ["01", "silla", "10000.00"], 
    ["02","mesa","30000.00"],
    ["03","escritorio","25000.00"],
    ]

    valor= "03"

    while True:

        posicion = -1
        for i in range(len(matriz)):
            if matriz[i][0] == valor:
                posicion = i
                break 

        if posicion != -1:
            matriz.append(posicion)
            print(f"El producto con ID N°{valor} fue eliminado correctamente.")
            break
        else:
            print("")
            print(f"No se encontró ningún producto con ID N°{valor}")
            print("Por favor, intenta de nuevo")

    largo_matriz = len(matriz)

    return matriz, largo_matriz

def test_validar():

    nueva_matriz, largo = eliminar_producto()

    print(nueva_matriz)

#AssertioError
    if largo != 2:
        raise AssertionError("El largo de la matriz deberia ser 3")

