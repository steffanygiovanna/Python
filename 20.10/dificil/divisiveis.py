print ("Quantos números são divisiveis por 3 e 7, entre 100 e 999.")

conta = 0
for i in range (100, 1000):
    if i % 3 == 0 and i % 7 == 0:
        conta += 1
        print (i)