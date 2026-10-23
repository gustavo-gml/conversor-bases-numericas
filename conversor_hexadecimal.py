def hexadecimal_para_decimal(numero):
    numero = numero.strip().upper()
    simbolos = "0123456789ABCDEF"

    if not numero or any(digito not in simbolos for digito in numero):
        raise ValueError("Digite um número hexadecimal válido (0-9 e A-F).")

    decimal = 0
    for digito in numero:
        valor_digito = simbolos.index(digito)
        decimal = decimal * 16 + valor_digito

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


def converter_hexadecimal(numero):
    decimal = hexadecimal_para_decimal(numero)

    return {
        "binario": decimal_para_base(decimal, 2),
        "decimal": str(decimal),
        "octal": decimal_para_base(decimal, 8)
    }