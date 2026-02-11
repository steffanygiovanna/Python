print("Calcule seu IMC.")

alt = float(input("Digite sua altura (M) \n"))
peso = float(input("Digite seu peso (Kg): \n"))

imc = peso / (alt ** 2)

print(f"Seu Imc é: {imc:.2f} \n")

if imc < 18.5:
    print("Você está abaixo do peso, precisa ganhar peso de forma saudavel! \n")
elif imc > 18.6 and imc < 24.9:
    print("Seu peso está normal, parabéns continue se cuidando! \n")
elif imc > 25.0 and imc < 29.9:
    print("Você está com sobrepeso, precisa perder um pouco de peso, se cuide! \n")
elif imc > 30.0 and imc <34.9:
    print("Você está com Obesidade Grau 1, Lembre-se de se cuidar! \n")
elif imc > 35.0 and imc < 39.9:
    print("Você está com Obesidade Grau 2, Não desita de se cuidar! \n")
else:
    print("Você está com obesidade Grau 3, Procure o auxilio de um médico! \n")