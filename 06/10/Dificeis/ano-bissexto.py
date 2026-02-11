print("Ano bissexto")

ano = int(input("Digite um ano: \n"))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é Bissexto! \n")
else:
    print(f"O ano {ano} Não é bissexto! \n")