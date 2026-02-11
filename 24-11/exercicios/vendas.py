import pandas as pd

dados = {
    'Produto': ['Caderno', 'Lápis', 'Mochila', 'Borracha'],
    'Preço': [12.00, 2.00, 85.00, 3.00],
    'Vendidos': [40, 150, 10, 80]
}

df = pd.DataFrame(dados)

df = df.sort_values(by='Produto')

df['Faturamento'] = df['Preço'] * df['Vendidos']
print("Dados de Vendas: \n", df)

df.to_csv('Faturamento_500.csv', index=False)
print("\nProdutos com faturamento alto")
print(df[df['Faturamento']> 500])
print("\n Arquivo CSV gerado com sucesso!")