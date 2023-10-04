feliz = "Me alegro que estes teniendo un buen dia. Ten un abrazo (:"
triste = "A veces esta bien tener malos dias, para saber el valor de los buenos dias. Siempre que llovio paro, una vez diluvio pero fue para salvar a los seres vivos."



def animo(respuesta):
    
    if respuesta == "triste":
        print(triste)
    elif respuesta == "feliz":
        print(feliz)
    else:
        print("Respuesta no valida, por favor ingrese una respuesta valida.")


animo(input("Ingrese como esta hoy, si triste o feliz: "))