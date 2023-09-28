
primos = []

for i in range (1, 100):
    for j in range (1, i):
        if (i % j) == 0:
            primos.append(i)
        
        
print(primos)