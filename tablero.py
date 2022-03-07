from flask import Flask, render_template
import math
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", phrase="hello", cantidadUno=8, cantidadDos=int(8))


@app.route('/<numero>')
def tabla(numero):
    return render_template("index.html", phrase="hello", cantidadUno=int(numero), cantidadDos=int(8))


@app.route('/<numero1>/<numero2>')
def tablaDos(numero1, numero2):
    return render_template("index.html", cantidadUno=int(numero1), cantidadDos=int(numero2))


@app.route('/<numero1>/<numero2>/<color1>/<color2>')
def tablaTres(numero1, numero2, color1, color2):
    return render_template("index.html", cantidadUno=int(numero1), cantidadDos=int(numero2), nuevocolorUno=color1, nuevocolorDos=color2)


if __name__ == "__main__":
    app.run(debug=True)
