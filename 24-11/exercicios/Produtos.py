import pandas as pd

dados = {
    'Produto': ['Impressora', 'Tablet', 'SSD', 'Mouse'],
    'Avaliações':[
    [5, 4, 4, 3],
    [4, 5, 5, 5],
    [5, 5, 5, 4],
    [3, 4, 3, 4]
    ]
}

df = pd.DataFrame(dados)
df = df.sort_values(by='Produto', ascending=False)
print(df)


df['Média'] = df['Avaliações'].apply(lambda x: sum(x) / len(x))
print("\nMédia das avaliações:\n", df[['Produto', 'Média']])

print("\n Avaliações acima da média:")
print(df[df['Média'] > 4.5])
