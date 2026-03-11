
def RegistroVentas():
    VALIDADOR = True
    while VALIDADOR:  
        try:
            NombreProducto = input("Ingrese el nombre del producto: ")  
            PrecioProducto = float(input("Ingrese el precio del producto: "))
            CantidadProducto = int(input("¿Cuántos productos desea comprar?: "))
            Total = PrecioProducto * CantidadProducto  
            VALIDADOR = False
            # Devolvemos los datos como una tupla
            return (NombreProducto, PrecioProducto, CantidadProducto, Total)
        except ValueError:       
            print("¡ERROR! Debe ingresar un número. Intente de nuevo.")