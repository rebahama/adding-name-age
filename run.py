from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///nameage'

db = SQLAlchemy(app)

# create a class-based model for the "Person" table
class Person(db.Model):
    PersonId = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __repr__(self):
            # __repr__ to represent itself in the form of a string
            return f"Name:{self.name} Age:{self.age}"



@app.route('/')
def index():
    return render_template('index.html')

@app.route("/addperson")
def addperson():
    person=list(Person.query.order_by(Person.name).all())
    return render_template("addperson.html", person=person)


@app.route("/personadding", methods=["GET", "POST"])
def personadding():
    if request.method == "POST":
        person = Person(name=request.form.get("name"),
        age = request.form.get("age")                
        )
        db.session.add(person)
        db.session.commit()
        return redirect("addperson")
    return render_template("personadding.html")


if __name__ == "__main__":
    app.run(
        debug=True
    )
