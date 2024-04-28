

cadena = input("Ingrese una frase y se le devolvera el acronimo:\t")
acronimo = ""
cadena_separada = cadena.split()
for i in cadena_separada:
    acronimo += (i[0].capitalize())


print("El acronimo de \"{}\" es -> {}".format(cadena, acronimo))