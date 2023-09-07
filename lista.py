mercado = []

def agregar(producto):
    mercado.append(producto)


def borrar(producto):
    if producto in mercado:
        mercado.remove(producto)
    
def buscar(producto):
    if producto in mercado:
        return producto
        
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
