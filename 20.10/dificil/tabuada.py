print ("Digite um número para ver a tabuada dele: ")

num = int(input())
print ("Tabuada do número:", num)
for i in range (1, 11):
    result = num * i
    print (num, "x", i, "=", result)