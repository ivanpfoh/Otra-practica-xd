
secuencia = [] 

for i in range(50):
    if i == 0:
        secuencia.append(0)
        secuencia.append(i + 1)
    else:
        secuencia.append(secuencia[i]+secuencia[i-1])
        
print(secuencia)
