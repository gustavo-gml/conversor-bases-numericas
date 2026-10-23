def decimal_para_binario(numero):
    if numero == 0:
        return "0"

    resultado = ""

    while numero > 0:
        resto = numero % 2
        resultado = str(resto) + resultado
        numero = numero // 2

    return resultado