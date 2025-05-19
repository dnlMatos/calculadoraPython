from utils.input_handler import get_number, get_operation
from operations import adicao, subtracao, multiplicacao, divisao

def main():
    print("Bem-vindo à Calculadora Básica!")

    while True:
        try:
            num1 = get_number("Digite o primeiro número: ")
            num2 = get_number("Digite o segundo número: ")
            operacao = get_operation()

            if operacao == '+':
                resultado = adicao.somar(num1, num2)
            elif operacao == '-':
                resultado = subtracao.subtrair(num1, num2)
            elif operacao == '*':
                resultado = multiplicacao.multiplicar(num1, num2)
            elif operacao == '/':
                resultado = divisao.dividir(num1, num2)

            print(f"Resultado: {resultado}")
            break  # Encerra após operação bem-sucedida

        except Exception as e:
            print(f"Erro inesperado: {e}")
            print("Vamos tentar novamente.\n")

if __name__ == "__main__":
    main()
