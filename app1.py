import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "newdb1.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
Bootstrap(app)

db = SQLAlchemy(app)

class Book(db.Model):
    identification = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    description = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    datetime = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    longitude = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    latitude = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    elevation = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    
      
@app.route("/", methods=["GET", "POST"])
def home():
    if request.form:
        book = Book(identification=request.form.get("identification"), description=request.form.get("description"), datetime=request.form.get("datetime"), longitude=request.form.get("longitude"), latitude=request.form.get("latitude"), elevation=request.form.get("elevation"))
        db.session.add(book)
        db.session.commit()
    books = Book.query.all()
    return render_template("home.html", books=books)

@app.route("/update", methods=["POST"])
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    newtitle2 = request.form.get("newtitle2")
    oldtitle2 = request.form.get("oldtitle2")
    newtitle3 = request.form.get("newtitle3")
    oldtitle3 = request.form.get("oldtitle3")
    newtitle4 = request.form.get("newtitle4")
    oldtitle4 = request.form.get("oldtitle4")
    newtitle5 = request.form.get("newtitle5")
    oldtitle5 = request.form.get("oldtitle5")
    newtitle6 = request.form.get("newtitle6")
    oldtitle6 = request.form.get("oldtitle6")
    book = Book.query.filter_by(identification=oldtitle, description=oldtitle2, datetime=oldtitle3, longitude=oldtitle4, latitude=oldtitle5, elevation=oldtitle6).first()
    book.identification = newtitle
    book.description = newtitle2
    book.datetime = newtitle3
    book.longitude = newtitle4
    book.latitude = newtitle5
    book.elevation = newtitle6
    db.session.commit()
    return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
    identification = request.form.get("identification")
    description = request.form.get("description")
    datetime = request.form.get("datetime")
    longitude = request.form.get("longitude")
    latitude = request.form.get("latitude")
    elevation = request.form.get("elevation")
    book = Book.query.filter_by(identification=identification, description=description, datetime=datetime, longitude=longitude, latitude=latitude, elevation=elevation).first()
    db.session.delete(book)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)