import pandas as pd

dados = {
    'Nome': ['Ana Souza', 'João Lima', 'Carla Mendes', 'Pedro Rocha'],
    'Idade': [28, 32, 41, 22],
    'Salário': [3500, 4200, 5100, 2800]
}

df = pd.DataFrame(dados)
df = df.sort_values(by='Salário', ascending=False)
print(df)

print("\nFuncionários com idade abaixo de 30 anos:")
print(df[df['Idade'] < 30])

df['Média'] = df['Salário'].mean()
print("\nPreço médio dos funcionários: R$", df['Média'][0])
print("\nSalários acima da média:")
print(df[df['Salário'] > 3900])