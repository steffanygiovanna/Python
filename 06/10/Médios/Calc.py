print("Faça uma conta: Soma, Subtração, Multiplicação ou Divisão.")

num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))
op = input("Digite qual será a operação (+, -, * ou /): \n")

if op == "+":
    print("A soma ente os números é:", num1 + num2)
elif op == "-":
    print("A Subtração dos números é:", num1 - num2)
elif op == "*":
    print("O resultado da Multiplicação será:", num1 * num2)
elif op == "/":
    print("O resultado da sua Divisão é:", num1 / num2)