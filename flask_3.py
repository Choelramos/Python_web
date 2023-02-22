from urllib import request
from flask import Flask

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return "Página principal"


@app.route('/ola/')
@app.route('/ola/<nome>')
def ola(nome):
    return "Olá, " + nome


@app.route('/logar', methods=['GET', 'POST'])
def logar():
    if request.method == 'POST':
        return "Recebeu um post! Fazer login!"
    else:
        return "Recebeu um get! Exibir FORM de login"


app.run()

