


multiplicacion = lambda valor1, valor2: valor1 * valor2

print(multiplicacion(5,5))

def division(n5, n6):
    return n5 / n6
    

def suma_de_cuadrados(n1,n2,n3,n4):
    resultado = multiplicacion(n1, n2) + multiplicacion(n3, n4)
    resultado2 = n1**4
    return round((division(resultado, resultado2)), 2)

print(suma_de_cuadrados(5,5,4,4))