print("Adicione mais frutas a lista: \n")

frutas = ["Pera", "Abacaxi", "Uva", "Melancia", "Lichia"]

for i in frutas:
    print(i)

for i in range (3):
 append_fruit = input("Digite o nome de uma fruta para adiciona-la: ")
 frutas.append(append_fruit)

print("Nova lista de frutas: \n", frutas)
for i in frutas:
    print(i)