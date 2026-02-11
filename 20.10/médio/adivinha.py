print ("Adivinhe o número entre 1 a 10")

import random

num = random.randint(1, 10)

resp = 0
while resp != num:
    resp = int(input("Digite um número: "))
    if resp < num:
        print("Tente um número maior.")
    elif resp > num:
        print("Tente um número menor.")
    else :
        print("Você acertou o número escolhido!")