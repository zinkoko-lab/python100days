from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, asc, desc
from flask_wtf import FlaskForm
from wtforms import FloatField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange
from flask_migrate import Migrate
import requests
import os
from dotenv import load_dotenv

# -------------------------
# 環境変数の読み込み
# -------------------------
load_dotenv()
API_TOKEN = os.getenv("TOKEN")

# -------------------------
# TMDB API 用の定数定義
# -------------------------
SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
DETAIL_URL = "https://api.themoviedb.org/3/movie"
IMG_URL = "https://image.tmdb.org/t/p/w500"
HEADERS = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_TOKEN}",
}


# -------------------------
# TMDB API - 検索処理
# -------------------------
def movie_search(movie_title: str) -> dict:
    """映画タイトルでTMDBから検索結果を取得"""
    params = {
        "query": movie_title,
        "include_adult": "false",
        "page": "1",
    }
    response = requests.get(SEARCH_URL, headers=HEADERS, params=params)
    result = response.json()["results"]
    return result


# -------------------------
# TMDB API - 詳細取得処理
# -------------------------
def movie_detail(movie_id: int) -> dict:
    """映画IDでTMDBから詳細情報を取得"""
    response = requests.get(f"{DETAIL_URL}/{movie_id}", headers=HEADERS)
    result = response.json()

    # 必要な情報だけ抽出
    title = result["title"]
    img_url = f"{IMG_URL}/{result['poster_path']}"
    year = result["release_date"].split("-")[0]
    description = result["overview"]

    return {
        "title": title,
        "img_url": img_url,
        "year": year,
        "description": description,
    }


# -------------------------
# Flaskアプリ設定
# -------------------------
app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


# -------------------------
# DB設定（SQLAlchemy + Migrate）
# -------------------------
class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate(app, db)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies-collection.db"
db.init_app(app)


# -------------------------
# 映画テーブル定義
# -------------------------
class Movie(db.Model):
    """映画コレクションのモデル"""

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# 初回だけテーブル作成
with app.app_context():
    db.create_all()


# -------------------------
# フォーム定義
# -------------------------
class EditForm(FlaskForm):
    """評価・レビュー編集用フォーム"""

    rating = FloatField(
        "Your Rating Out of 10. e.g.7.5",
        validators=[DataRequired(), NumberRange(min=0, max=10)],
    )
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")


class AddForm(FlaskForm):
    """映画追加用フォーム"""

    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")


# -------------------------
# 映画ランキング再計算
# -------------------------
def ranker():
    """映画のratingに応じてrankingを再計算"""
    with app.app_context():
        result = db.session.execute(db.select(Movie).order_by(asc(Movie.rating)))
        movies = result.scalars().all()
        ranker_ = len(movies)
        for movie in movies:
            movie.ranking = ranker_
            ranker_ -= 1
        db.session.commit()


# -------------------------
# ルーティング
# -------------------------
@app.route("/")
def home():
    """ホーム画面 - ランキング順に映画一覧表示"""
    with app.app_context():
        ranker()
        result = db.session.execute(db.select(Movie).order_by(desc(Movie.ranking)))
        movies = result.scalars().all()
    return render_template("index.html", movies=movies)


@app.route("/<int:id>/edit", methods=["GET", "POST"])
def edit(id):
    """映画の評価とレビューを編集"""
    edit_form = EditForm()
    with app.app_context():
        movie = db.get_or_404(Movie, id)
        if edit_form.is_submitted():
            movie.rating = edit_form.rating.data
            movie.review = edit_form.review.data
            db.session.commit()
            return redirect(url_for("home"))
        return render_template("edit.html", form=edit_form, movie=movie)


@app.route("/<int:id>/delete")
def delete(id):
    """映画を削除"""
    with app.app_context():
        movie = db.one_or_404(db.select(Movie).where(Movie.id == id))
        db.session.delete(movie)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["GET", "POST"])
def add():
    """映画追加フォーム → TMDB検索結果表示"""
    add_form = AddForm()
    if add_form.is_submitted():
        movie_keyword = add_form.title.data
        movies_result = movie_search(movie_keyword)  # TMDB API 呼び出し
        return render_template("select.html", movies=movies_result)
    return render_template("add.html", form=add_form)


@app.route("/save/<int:id>", methods=["GET", "POST"])
def save(id):
    """TMDB詳細情報から映画をDBに保存し、編集画面へ遷移"""
    detail_data = movie_detail(id)
    movie = Movie(
        title=detail_data["title"],
        year=detail_data["year"],
        description=detail_data["description"],
        img_url=detail_data["img_url"],
    )
    with app.app_context():
        db.session.add(movie)
        db.session.commit()
        added_movie = db.one_or_404(
            db.select(Movie).where(Movie.title == detail_data["title"])
        )
    return redirect(url_for("edit", id=added_movie.id))


# -------------------------
# メイン処理
# -------------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)
