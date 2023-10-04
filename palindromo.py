espacios = " "
# Verifica que la palabra al reves sea la misma
def sacar_espacios(palabra_sin_espacios):
    for i in range(len(espacios)):
        palabra_sin_espacios = palabra_sin_espacios.replace(espacios[i],"")
    else:
        return palabra_sin_espacios
        

def es_palindromo(palabra):
    nueva_palabra = ""
    for i in range(1, (len(palabra) + 1), 1):
        nueva_palabra += palabra[-i]
    if nueva_palabra == palabra:
        print(f"La palabra {palabra} es palindromo.")
    else:
        print(f"La palabra {palabra} no es palindromo.")
    

        
es_palindromo(sacar_espacios("amo la paloma"))
