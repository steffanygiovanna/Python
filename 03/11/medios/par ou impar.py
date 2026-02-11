print("Digite um número inteiro:")

def par_ou_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = int(input())
print(f"O número {numero} é {par_ou_impar(numero)}.")
