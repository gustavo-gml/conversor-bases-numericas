
def binario_para_decimal(numero):
    if not numero or any(digito not in "01" for digito in numero):
        raise ValueError("Digite somente 0 e 1.")

    decimal = 0

    for digito in numero:
        decimal = decimal * 2

        if digito == "1":
            decimal += 1

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


def converter_binario(numero):
    decimal = binario_para_decimal(numero)

    return {
        "decimal": str(decimal),
        "hexadecimal": decimal_para_base(decimal, 16),
        "octal": decimal_para_base(decimal, 8)
    }
