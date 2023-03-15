from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')  # Raiz
def index():
    return render_template('inicio.html')


@app.route('/oi/')
@app.route('/oi/<nome>')
def ola(nome="mundo"):
    return "Olá, " + nome


app.run()
