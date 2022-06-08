
from models import Person
from flask import Flask, render_template

hello="this"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/addperson")
def addperson():
    return render_template("addperson.html")


@app.route("/personadding")
def personadding():
    return render_template("personadding.html")


if __name__ == "__main__":
    app.run(
        debug=True
    )
