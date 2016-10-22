from flask import Flask, send_file
import PracticePres as pg

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <h1>Hello T.Hacks!</h1>
    """


@app.route("/greet/<string:name>")
def greet(name):
    return "Hello, {}!".format(name)


@app.route("/<int:num>")
def plot(num):
    return send_file(pg.plotPrimes(num), mimetype="image/png")

if __name__ == "__main__":
    app.run()
