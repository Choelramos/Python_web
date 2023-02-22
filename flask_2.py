from flask import Flask

app = Flask(__name__)


@app.route('/pagina')
def pagina():
    return "Página inicial!"


@app.route('/ola/<nome>')
def ola(nome):
    return 'Olá, ' + nome


app.run()
