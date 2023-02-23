from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('inicio.html')


@app.route('/oi/')
@app.route('/oi/<nome>')
def ola(nome="mundo"):
    return "Olá, ", nome_recebido = nome


    if __name__ == '__main__':
        app.run()
