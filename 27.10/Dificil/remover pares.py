print("Removendo os números pares:")

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in num[:]:
    if i % 2 == 0:
        num.remove(i)

print("Lista sem números pares:", num)
for i in num:
    print(i)