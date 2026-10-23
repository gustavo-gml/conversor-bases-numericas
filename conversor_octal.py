def octal_para_decimal(numero):
    # Validação: verifica se a string está vazia ou contém caracteres fora de 0 a 7
    if not numero or any(digito not in "01234567" for digito in numero):
        raise ValueError("Digite somente números octais válidos (dígitos de 0 a 7).")

    decimal = 0
    for digito in numero:
        decimal = decimal * 8 + int(digito)

    return decimal


def decimal_para_base(numero, base):
    simbolos = "0123456789ABCDEF"

    if numero == 0:
        return "0"

    resultado = ""

    while numero > 0:
        resto = numero % base
        resultado = simbolos[resto] + resultado
        numero //= base

    return resultado


def converter_octal(numero):
    decimal = octal_para_decimal(numero)

    return {
        "decimal": str(decimal),
        "hexadecimal": decimal_para_base(decimal, 16),
        "binario": decimal_para_base(decimal, 2)
    }