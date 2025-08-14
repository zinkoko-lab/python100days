from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)


# DB構築
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
# initialize the app with the extension
db.init_app(app)


class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, type_=Integer)
    title: Mapped[str] = mapped_column(unique=True, type_=String(250), nullable=False)
    author: Mapped[str] = mapped_column(type_=String(250), nullable=False)
    rating: Mapped[float] = mapped_column(type_=Float, nullable=False)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        return render_template("add.html")
    elif request.method == "POST":
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"],
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))


@app.route("/<int:id>/edit_rating", methods=["GET", "POST"])
def edit_rating(id):
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        if request.method == "GET":
            return render_template("edit_rating.html", book=book)
        elif request.method == "POST":
            new_rating = request.form["new_rating"]
            book.rating = new_rating
            db.session.commit()
    return redirect(url_for("home"))


@app.route("/<int:id>/delete")
def delete(id):
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
        db.session.delete(book)
        db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
