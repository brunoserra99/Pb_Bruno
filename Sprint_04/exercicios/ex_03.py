

from functools import reduce

def calcula_saldo(lancamentos) -> float:
    # Transforma a lista de lançamentos em uma lista de valores numéricos (positivos ou negativos)
    valores = map(lambda x: x[0] if x[1] == 'C' else -x[0], lancamentos)
    
    # Reduz a lista de valores a um saldo final, somando todos os elementos
    saldo_final = reduce(lambda x, y: x + y, valores)
    
    return saldo_final

'''
#Lancamento input usuario
lancamentos = []
print("----Programa para lancamentos Bancarios---- ")
print("Digite os lançamentos (valor e tipo: C para crédito, D para débito).")
print("Digite 'fim' para encerrar.")
print("Iniciando...")
print("Iniciando...Ok")
# Entrada dos lançamentos
for _ in iter(int, 1):  # Loop infinito simplificado
    valor_input = input("Valor (ou 'f'): ").strip().upper()
    if valor_input.lower() == 'f':
        break
    tipo = input("Tipo (C/D): ").strip().upper()
    if tipo in ('C', 'D'):
        lancamentos.append((float(valor_input), tipo))
'''

# Entrada lançamentos
lancamentos = [
    (200, 'D'),
    (300, 'C'),
    (100, 'C')
]

#resultado
resultado = calcula_saldo(lancamentos)
print(f"{resultado:.2f}")  