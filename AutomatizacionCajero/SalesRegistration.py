def SalesRegistration():
    VALIDATOR = True
    while VALIDATOR:  
        try:
            ProductName = input("Enter the product name: ")
            if ProductName.strip()=="":
                int("Error: Empty Name")
            else:
                try:
                    ProductPrice = float(input("Enter the product price: "))
                    
                    if ProductPrice < 0:
                        # Forzamos un error de valor convirtiendo algo que no es número
                        int("Error: Negative") 
                    else:
                        ProductQuantity = int(input("How many products do you want to buy?: "))
                        
                        if ProductQuantity < 0:
                            int("Error: Negative Quantity")
                        else:

                            Total = ProductPrice * ProductQuantity  
                            VALIDATOR = False
                            return (ProductName, ProductPrice, ProductQuantity, Total)
                except ValueError:
                    print("ERROR! Invalid input (it must be a positive number). Try again.")
        except ValueError:
            print("ERROR! Invalid input (it must be a positive number). Try again.")