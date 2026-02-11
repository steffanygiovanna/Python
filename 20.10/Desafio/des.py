print ("Mostrando números primos menor ou igual ao escolhido.")

num = int(input("Digite um número: "))
print ("Números primos menores ou iguais a", num , ":")

for i in range (2, num + 1):
    primo = True
    for p in range (2, i):
        if i % p == 0:
            primo = False
            break
    if primo:
        print (i) 