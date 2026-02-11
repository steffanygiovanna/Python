import pandas as pd

dados = {
    'Nome': ['Ana', 'Rebeca', 'Thamye'],
    'Idade': [23, 4, 5],
    'Salário': [2500.00, 5000.00, 6000.00]
}

df = pd.DataFrame(dados)
 # Adicionar uma coluna
df['Bonus'] = df['Salário'] * 0.1
print(df)
# Excluir uma coluna
df = df.drop(columns = ['Bonus'])
print(df)
# print(df[df['Idade'] > 15])