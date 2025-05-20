def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erro: Divisão por zero não é permitida.")
        return None
 