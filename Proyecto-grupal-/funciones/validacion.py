
def buscar_numeros(matriz, id):          
    encontrado = False
    while encontrado == False:
        for fila in matriz:
            if fila[0] == id:
                encontrado = True
                
        if encontrado == False:
            print("El ID no fue encontrado. Por favor intente nuevamente.")

    return encontrado

def validar_numeros(mensaje):
    while True:
        valor = input(mensaje)

        try:
            valor = int(valor)
            break
        except ValueError:
            if valor == "":
                print("No se admiten espacios en blanco!\n")
            elif valor != "":
                print("Solo se admiten numeros!\n")
            
    return valor


                    

