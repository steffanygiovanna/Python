animal = {
    "Águia",
    "Alce",
    "Bode"
}

try:
    with open("animal.txt", "r") as arquivo:
        conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)

except Exception as e:
    print(f"Erro ao abrr o arquivo: {e}")


finally:
    print("Operação de abertura de arquivo finalizada.")