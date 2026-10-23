from flask import Flask, render_template, request # 1. Importe o render_template

from conversor_binario import converter_binario

from conversor_hexadecimal import converter_hexadecimal
from conversor_octal import converter_octal

from conversor_decimal import decimal_para_binario

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')


@app.route('/binario', methods=['GET', 'POST'])
def pagina_binario():
    resultados = None
    erro = None
    numero = ""

    if request.method == 'POST':
        numero = request.form.get('numero', '').strip()

        try:
            resultados = converter_binario(numero)
        except ValueError as e:
            erro = str(e)

    return render_template(
        'binario.html',
        resultados=resultados,
        erro=erro,
        numero=numero
    )

@app.route('/hexadecimal', methods=['GET', 'POST'])
def pagina_hexadecimal():
    resultados = None
    erro = None
    numero = ""

    if request.method == 'POST':
        numero = request.form.get('numero', '').strip()

        try:
            resultados = converter_hexadecimal(numero)
        except ValueError as e:
            erro = str(e)

    return render_template(
        'hexadecimal.html',
        resultados=resultados,
        erro=erro,
        numero=numero
    )
    
@app.route('/decimal', methods=['GET', 'POST'])
def pagina_decimal():    
    resultado = None
    erro = None
    numero = ""

    if request.method == 'POST':
        numero = request.form.get('numero', '').strip()

        try:
            valor = int(numero)

            if valor < 0:
                raise ValueError("Número negativo.")

            resultado = decimal_para_binario(valor)

        except ValueError:
            erro = "Digite um número inteiro válido e não negativo."

    return render_template(
        'decimal.html',
        resultado=resultado,
        erro=erro,
        numero=numero
    )

@app.route('/octal', methods=['GET', 'POST'])
def octal():
    if request.method == 'POST':
        numero = request.form.get('numero', '').strip()
        
        try:
            resultados = converter_octal(numero)
            return render_template('octal.html', numero=numero, resultados=resultados)
        except ValueError as e:
            return render_template('octal.html', numero=numero, erro=str(e))
            
    return render_template('octal.html')

if __name__ == '__main__':
    app.run(debug=True)
