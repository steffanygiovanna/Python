int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real: "))

resultado1 = (2 * int1) * (int2 / 2)
resultado2 = (3 * int1) + real
resultado3 = real ** 3

print(f"Resultado 1 (dobro do primeiro * metade do segundo): {resultado1}")
print(f"Resultado 2 (triplo do primeiro + o terceiro): {resultado2}")
print(f"Resultado 3 (o terceiro elevado ao cubo): {resultado3:.2f}")
