import pandas as pd

dados = {
    'Item': ['Pendrive', 'Headset', 'WebCam', 'Teclado'],
    'Quantidade': [25, 12, 8, 15],
    'Preço Unitário': [30, 150, 220, 95]
}

df = pd.DataFrame(dados)

df['Valor Total'] = df['Quantidade'] * df['Preço Unitário']
print("Dados dos eletrônicos:\n", df)


df['Média'] = df['Preço Unitário'].mean()
print("\nPreço médio dos eletrônicos: R$", df['Média'][0])

print("\n Itens com valor unitário acima de 100:")
print(df[df['Preço Unitário'] > 100])
df.to_csv('Eletronicos', index=False)
print("\nArquivo CSV gerado com sucesso!")