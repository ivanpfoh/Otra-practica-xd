def numeros():
    n1 = int(input("Ingrese el primer numero:\n " ))
    n2 = int(input("Ingrese el segunod numero:\n "))
    return n1, n2

def calculadora (calculo):
    try:
        if calculo == "+":
            n1, n2 = numeros()
            return (n1 + n2)
        elif calculo == "-":
            n1, n2 = numeros()
            return (n1 - n2)
        elif calculo == "*":
            n1, n2 = numeros()
            return (n1 * n2)
        elif calculo == "/":
            n1, n2 = numeros()
            return (n1 / n2)
        elif calculo == "//":
            n1, n2 = numeros()
            return (n1 // n2)
        elif calculo == "%":
            n1, n2 = numeros()
            return (n1 % n2)
        elif calculo == "**":
            n1, n2 = numeros()
            return (n1 ** n2)
    except:
        print("Ingrese una operacion valida.")



print("El resultado es: ",calculadora(input("Ingrese la operacion que quiere realizar:\n")))