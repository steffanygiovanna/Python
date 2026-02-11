num = int(input("Digite um numero:"))
num2 = int(input("Digite outro numero:"))

def maior_menor(num, num2):
    if num > num2:
        return f"O maior numero é {num}"
    elif num2 > num:
        return f"O maior numero é {num2}"
    else:
        return "Os numeros são iguais"

print(maior_menor(num, num2))
