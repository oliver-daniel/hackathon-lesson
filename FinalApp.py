from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    html = """
    <h1>Hello T.Hacks!</h1>
    """
    return html

if __name__ == "__main__":
    app.run()
