import pandas as pd

dados = {
    'Produto': ['Mouse', 'Teclado', 'Monitor', 'Cabo HDMI'],
    'Preço': [50.00, 150.00, 900.00, 40.00],
    'Estoque': [20, 15, 8, 50]
}

df = pd.DataFrame(dados)
# Criar nova coluna 
df['|Total'] = df['Preço'] * df['Estoque']
# Salvar em CSV
df.to_csv('Tabela_Completa.csv', index=False)
print("Tabela Completa:\n", df)
print("\nArquivo CSV gerado com sucesso!")