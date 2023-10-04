#devuelve de a uno la una lista de el doble de los numeros pares,y el tamaño de la lista depende de la cantidad de veces que se lo llame e inicia desde el numero que se le asigno  en la asignacion de la misma a una variable.

def practicayield(num):
    
    while num > 0:
        if num % 2 == 0 :
            yield num * 2
            num +=1
        else:
            num += 1
            
lista1 = practicayield(1)
print(next(lista1))
print(next(lista1))
