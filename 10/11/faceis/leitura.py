try:
     while True:
         
         try:
          num = int(input("Digite um número inteiro para ler:"))
          print("Você digitou o número:", num)
          break
   
         except ValueError:
          print("Erro: Por favor insira um número inteiro válido.")


finally:
 print("Operação de leitura finalizada.")