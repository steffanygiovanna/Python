print("Digite um número inteiro:")

def verificar_primo(num):
    if num <= 1:
        return "Composto"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return "Composto"
    return "Primo"

num = int(input())
print(f"O número {num} é {verificar_primo(num)}.")
