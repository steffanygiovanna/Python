print("Digite um número inteiro:")

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * fatorial(num - 1)

num = int(input())
print(f"O número {num} é {fatorial(num)}.")
