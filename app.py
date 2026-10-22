from flask import Flask, render_template, request # 1. Importe o render_template

from conversor_binario import converter_binario

from conversor_hexadecimal import converter_hexadecimal

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

if __name__ == '__main__':
    app.run(debug=True)
