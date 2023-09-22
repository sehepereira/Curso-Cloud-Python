# laço com for
contador = 1
for i in range (1, 21):
    if(i == 13):
        continue
    else:
        print(i)

# laço com while


while (contador <= 20):
    if(contador == 13):
        contador += 1
        continue
    else:
        print(contador)
        contador += 1

# laço com for reverso
for j in range (20, 0, -1):
    if(j == 13):
        continue
    else:
        print(j)