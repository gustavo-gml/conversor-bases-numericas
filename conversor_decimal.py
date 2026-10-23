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


def validar_decimal(numero):
    # Valida se a string enviada contém apenas dígitos inteiros (0-9)
    if not numero or not numero.isdigit():
        raise ValueError("Digite somente números inteiros válidos (dígitos de 0 a 9).")

    return int(numero)


def converter_decimal(numero):
    
    dec = validar_decimal(numero)

    return {
        "binario": decimal_para_base(dec, 2),
        "octal": decimal_para_base(dec, 8),
        "hexadecimal": decimal_para_base(dec, 16)
    }