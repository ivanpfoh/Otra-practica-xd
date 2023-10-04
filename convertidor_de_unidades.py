valorDolarVenta = 790 
valorDolarCompra = 785
dolares, pesos = 0, 0

def calculadora_pesos_a_dolar():

    respuesta = input("Quiere vender dolares o comprar dolares?\n")
    
    if respuesta == "vender":
        dolares = int(input("Ingrese la cantidad de dolares?\n"))
        print (f"La venta de ${dolares} dolares le dara = $",dolares*valorDolarVenta ," pesos.")
    elif respuesta == "comprar":
        pesos = int(input("Ingrese la cantidad de pesos que utilizara para la compra?\n"))
        print (f"La compra de ${pesos} pesos le dara = $",(pesos // valorDolarCompra) ," dolares.")
        
        


calculadora_pesos_a_dolar()
        