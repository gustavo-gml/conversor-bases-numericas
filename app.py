from flask import Flask, render_template, request # 1. Importe o render_template

from conversor_binario import converter_binario

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


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
