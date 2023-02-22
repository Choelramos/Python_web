from flask import Flask

app = Flask(__name__)


@app.route('/pagina')
def pagina():
    return "Página inicial!"


@app.route('/ola/')
@app.route('/ola/<nome>')  # utilizando parâmetro da função olá, isso vai passar o valor como argumento para função!
def ola(nome="mundo"):
    return 'Olá, ' + nome


app.run()
