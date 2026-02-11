print("Vamos conferir sua nota?")

nota = int(input("Digit sua nota (de 0 até 100): \n"))

if nota >= 60:
    print("Você foi Aprovado(a), Parabéns! \n")
elif nota <= 59:
    print("Você foi Reprovado, Estude mais! \n")