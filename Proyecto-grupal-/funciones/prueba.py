


matriz_productos =[
    ["01", "silla", "10000.00"], 
    ["02","mesa","30000.00"],
    ["03","escritorio","25000.00"],
    ["04","sillon","50000.00"],
    ["05","mesa de luz","20000.00"]
    ]

valor = input("Hola\n")

def buscar_numeros(matriz, id):          
    encontrado = False
    while encontrado == False:
        for fila in matriz:
            if fila[0] == id:
                encontrado = True
        
        if encontrado == False:
            print("El ID no fue encontrado. Por favor intente nuevamente.")
        else:
            print("El id fue encontrado")

        return encontrado
    
buscar_numeros(matriz_productos, valor)



