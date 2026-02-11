print ("Insira números até encerrar o programa")

print ("Digite um número(só encerra se digitar um número negativo): ")

num = 0

while num >=0:
    num = int(input("Digite um número: "))
    if num < 0:
        print("O número digitado foi um numero negativo, encerrando o programa!")