from RegistroVentas import RegistroVentas 
def SeguirComprando():    
    Historial = []
    Bucle = True
    while Bucle:
        Continuar_Comprando = input("¿Desea comprar algo? (si/no): ")
        if Continuar_Comprando == "si":
            DatosProducto = RegistroVentas()
            Historial.append(DatosProducto)
            print("Producto registrado con éxito.")
        elif Continuar_Comprando == "no":
            print("\n--- RESUMEN DE SU COMPRA ---")
            TotalPagar = 0
            for Posicion in Historial:
                print(f"Producto: {Posicion[0]} | Precio unitario: {Posicion[1]} | Cantidad: {Posicion[2]} | Total a pagar: {Posicion[3]}")
                TotalPagar = TotalPagar + Posicion[3]
            print("-" * 30)
            print("TOTAL FINAL A PAGAR: $", TotalPagar)
            print("Gracias por su compra, vuelva pronto")
            Bucle = False
        else:
            print("ERROR!!! Solo ingrese si o no")