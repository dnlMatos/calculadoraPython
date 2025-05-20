def get_number(prompt):
    while True:
        try:
            valor = float(input(prompt))
            return valor
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

def get_operation():
    operacoes_validas = ['+', '-', '*', '/']
    while True:
        operacao = input("Digite a operação (+, -, *, /): ")
        if operacao in operacoes_validas:
            return operacao
        else:
            print("Operação inválida! Tente novamente.")
 