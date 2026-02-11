print("Verificação de países na lista: \n")

países = ["Brasil", "Argentina", "Coreia do sul", "Japão", "Espanha"]

país_input = input("Digite o nome do país que deseja verificar: ")

if país_input in países:
    print("O País esta na lista. \n")
else:
    print("O País não está na lista. \n")