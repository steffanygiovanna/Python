valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))

salario_bruto = valor_hora * horas_trabalhadas

desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05

total_descontos = desconto_ir + desconto_inss + desconto_sindicato
salario_liquido = salario_bruto - total_descontos

print("\n--- Demonstrativo de Pagamento ---")
print(f"Salário Bruto     : R$ {salario_bruto:.2f}")
print(f"IR (11%)          : R$ {desconto_ir:.2f}")
print(f"INSS (8%)         : R$ {desconto_inss:.2f}")
print(f"Sindicato (5%)    : R$ {desconto_sindicato:.2f}")
print(f"Salário Líquido   : R$ {salario_liquido:.2f}")
