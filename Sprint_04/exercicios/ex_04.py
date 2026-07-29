def calcular_valor_maximo(operadores, operandos):
    # Aplica uma operação entre
    def operacao(op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            return a / b
        elif op == '%':
            return a % b
        else:
            raise ValueError(f"Operaçao desconhecida: {op}")

    # Combina usando zip e aplica usando map
    resultados = map(lambda x: operacao(x[0], x[1][0], x[1][1]), zip(operadores, operandos))

    # Retorna o maior
    return max(resultados)

# Entrada
operadores = ['+', '-', '*', '/', '+']
operandos = [(3, 6), (-7, 4.9), (8, -8), (10, 2), (8, 4)]

resultado = calcular_valor_maximo(operadores, operandos)
print(f"O resultado: {resultado}")