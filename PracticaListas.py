puntaje_de_peliculas = {}
respuesta = ""
respuesta = input("Quiere hacer una lista de peliculas favoritas?")
while respuesta == "si":
    puntaje_de_peliculas[input("Ingrese la peliculas que le gusta: ")] = input("Ingrese la valoracion que le da a la pelicula: ")
    print(puntaje_de_peliculas)
    respuesta = input("Le gusta otra peliculas?")


puntaje_de_series = {}
respuesta2 = ""
respuesta2 = input("Quiere hacer una lista de series favoritas?")
while respuesta2 == "si":
    puntaje_de_series[input("Ingrese la serie que le gusta: ")] = input("Ingrese la valoracion que le da a la serie: ")
    print(puntaje_de_series)
    respuesta2 = input("Le gusta otra serie?")



puntaje_de_libros = {}
respuesta3 = ""
respuesta3 = input("Quiere hacer una lista de libros favoritos?")
while respuesta3 == "si":
    puntaje_de_libros[input("Ingrese el libro que le gusta: ")] = input("Ingrese la valoracion que le da a el libro: ")
    print(puntaje_de_libros)
    respuesta3 = input("Le gusta otro libro?")


print(puntaje_de_libros)
print(puntaje_de_peliculas)
print(puntaje_de_series)