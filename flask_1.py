from flask import Flask

app = Flask(__name__)


@app.route('/pagina')
def pagina():
    return "Página inicial!"


@app.route('/ola')
def oi():
    return "Hello World!"


app.run()
