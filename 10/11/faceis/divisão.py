try:
    num1 = int(input("Digite um número inteiro:"))
    num2 = int(input("Digite o número divisor:"))

    result = num1 / num2
    print(f"O resultado da divisão é: {result}")

except ValueError:
    print("Erro: Por favor, insira apenas números inteiros")

except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")

finally:
    print("Operação finalizada.")