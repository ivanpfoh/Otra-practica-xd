'''
 * Crea las funciones capaces de transformar colores HEX
 * a RGB y viceversa.
 * Ejemplos:
 * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
 * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
'''

rgb = {"r": "0", "g": "0","b": "0"}
hexadecimal = [0,0,0]




def convertidor(): 
    respuesta = input("Quiere pasar de rgb a hexadecimal (1) o hexadecimal a rgb (2):\n")
    if respuesta == "1":
        rgb["r"] = int(input("Ingrese el numero para red de RGB"))
        rgb["g"] = int(input("Ingrese el numero para verde de RGB"))
        rgb["b"] = int(input("Ingrese el numero para azul de RGB"))
        hexadecimal[0] = hex(rgb["r"])
        hexadecimal[1] = hex(rgb["g"])
        hexadecimal[2] = hex(rgb["b"])
        print(hexadecimal)

    elif respuesta == "2":
        hexadecimal[0] = str(input("Ingrese el numero en hexadecimal para red"))
        hexadecimal[1] = str(input("Ingrese el numero en hexadecimal para green"))
        hexadecimal[2] = str(input("Ingrese el numero en hexadecimal para blue"))
        rgb["r"] = int(hexadecimal[0], 16)
        rgb["g"] = int(hexadecimal[1], 16)
        rgb["b"] = int(hexadecimal[2], 16)
        print(hexadecimal)

    else:
        print("Respuesta no valida.")
    

convertidor()