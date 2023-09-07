celulares = {}

def agregar(id, marca, modelo, valor):
    celulares[id] = {"Marca": marca, "Modelo": modelo, "Valor": valor}

    def borrar(id):
        if id in celulares:
         del celulares[id]


    def buscar(id):
     if id in celulares:
        return celulares[id]
   
    
    while True:
        print("-----------------------\n")
        print("Tienda De telefonos ")
        print("[1].Agregar Usuarios ")  
        print("[2].Eliminar Usuarios ")  
        print("[3].buscar Usuarios")  
 
        option = int(input("\nSeleccione una opcion: "))
     
        if option == 1:
            agregar()
        elif option == 2:
            id = int(input("id"))
            borrar(id)    
        elif option == 3:
            id = int(input("id"))
            buscar(id)
