
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

                    

