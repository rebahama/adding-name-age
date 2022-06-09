from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///agename'

db = SQLAlchemy(app)

# create a class-based model for the "Artist" table
class Person(db.Model):
    PersonId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
            # __repr__ to represent itself in the form of a string
            return self.name




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
