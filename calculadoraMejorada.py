def numeros():
    n1 = int(input("Ingrese el primer numero que quiere sumar:\n " ))
    n2 = int(input("Ingrese el segunod numero que quiere sumar:\n "))
    return n1, n2

def calculadora (calculo):
    try:
        if calculo == "+":
            n1, n2 = numeros()
            return (n1 + n2)
        if calculo == "-":
            n1, n2 = numeros()
            return (n1 - n2)
        if calculo == "*":
            n1, n2 = numeros()
            return (n1 * n2)
        if calculo == "/":
            n1, n2 = numeros()
            return (n1 / n2)
        if calculo == "//":
            n1, n2 = numeros()
            return (n1 // n2)
        if calculo == "%":
            n1, n2 = numeros()
            return (n1 % n2)
        if calculo == "**":
            n1, n2 = numeros()
            return (n1 ** n2)
    except:
        print("Ingrese una operacion valida.")



print(calculadora(input("Ingrese la oepracion que quiera realizar:\n")))