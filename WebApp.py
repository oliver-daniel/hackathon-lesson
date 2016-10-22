import PrimeGrapher as pg
from flask import Flask, send_file

app = Flask(__name__)


@app.route("/")
def index():
    html = """
    <a><h1>Hello T.Hacks!!!</h1></a>
    """
    return html


@app.route("/greet/<string:name>")
def greet(name):
    return "Hello, {}!".format(name)


@app.route("/<int:num>")
def plotNumber(num):
    return send_file(pg.plotPrimes(num), mimetype='image/png')
app.run()
