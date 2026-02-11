print("Que triângulo é esse: Equilatero, Isóceles ou Escaleno?")

a = float(input("Digite o valor do lado A: \n"))
b = float(input("Digite o valor do lado B: \n"))
c = float(input("Digite o valor do lado C: \n"))

if a == b  == c:
    print("Esse triÂngulo é Equilatero! \n")
elif a == b or b == c or a == c:
    print("Esse triângulo é Isóceles! \n")
else:
    print("Esse triângulo é Escaleno! \n")