print ("calculo de números pares do 1 ao 20")

soma = 0

for i in range (1, 21):
    if i % 2 == 0:
        soma += i
        print ("Soma dos números pares: ", soma)