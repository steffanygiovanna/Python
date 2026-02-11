def maior_lista(lista):
    maior_num = lista[0]

    for num in lista:
        if num > maior_num:
            maior_num = num
    return maior_num 

lista = [int(n) for n in input("Digite os números da lista separados por espaço: ").split()]

print(f"O maior número da lista é: {maior_lista(lista)}")
