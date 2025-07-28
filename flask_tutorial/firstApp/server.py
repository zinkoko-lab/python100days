from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import (
    UserMixin,
    LoginManager,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pytz
import os


app = Flask(__name__)
db = SQLAlchemy()
if app.debug:
    # ①Flaskのセッション情報の暗号化等に使用, 本番環境ではこのコードを変える
    SECRET_KEY = os.urandom(24)
    DB_INFO = {
        "user": "postgres",
        "password": "",
        "host": "localhost",
        "name": "postgres",
    }
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg://{user}:{password}@{host}/{name}".format(**DB_INFO)
    )
else:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace(
        "postgres://", "postgresql+psycopg://"
    )

app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
db.init_app(app)
migrate = Migrate(app, db)

# -----------------------------MEMO-----------------------------
# tableの作成 @ python console
# from server import app, db
# >>> with app.app_context():
# ...     db.create_all()

# CRUD
# C = create
# R = read
# U = update
# D = delete

# -----------------------------POST TABLE-----------------------------


# Post tableの定義
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500), nullable=False)
    body = db.Column(db.String(10000), nullable=False)
    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=lambda: datetime.now(pytz.timezone("Asia/Tokyo")),
    )
    img_name = db.Column(db.String(100), nullable=True)  # 画像のパス保存用カラムを追加


# -----------------------------USER MANAGEMENT-----------------------------


# ②login管理システム
login_manager = LoginManager()
login_manager.init_app(app)


# User table の定義
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)


# ③現在のユーザーを識別するために必要
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # 引数には文字列がくるため整数型に変換


# 4つ機能の実装
# ①サインアップ機能
# ②ログイン機能
# ③ログイン判定機能
# ④ログアウト機能


# ①サインアップ機能
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":  # リクエストのメソッドの判別
        return render_template("signup.html")

    elif request.method == "POST":  # リクエストのメソッドの判別

        # リクエストできた情報の取得
        username = request.form.get("username")
        password = request.form.get("password")
        hashed_password = generate_password_hash(password)

        # 取得したデータの保存
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        return redirect("/login")


# ②ログイン機能
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html", msg="")
    elif request.method == "POST":
        # html から username & password を取得
        username = request.form.get("username")
        password = request.form.get("password")
        # usernameを元に DB からのデータを取得
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(
                user.password, password=password
            ):  # 入力の password と DB の password が一致しているか確認
                login_user(user)
                return redirect("/admin")
            else:
                msg = "ユーザ名/パスワードが違います！"
                return render_template("login.html", msg=msg)
        else:
            msg = "そのユーザー名は存在しません！"
            return render_template("login.html", msg=msg)


# ④ログアウト機能
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")


# -----------------------------POST RELATED FUNCTIONS-----------------------------
@app.route("/")
def index():
    posts = Post.query.all()
    return render_template("index.html", posts=posts)


@app.route("/<int:post_id>/readmore")
def read_more(post_id):
    post = Post.query.get(post_id)
    return render_template("readmore.html", post=post, current_user=current_user)


@app.route("/admin")
@login_required
def adimin():
    posts = Post.query.all()
    return render_template("admin.html", posts=posts)


# アップロードが許可される拡張子
app.config["ALLOWED_EXTENSIONS"] = {"png", "jpg", "jpeg", "gif"}


def allowed_file(filname):
    # ドットが無ければ拡張子が無いので不可
    if "." not in filname:
        return False

    # 拡張子を取り出して小文字に変換
    extentsion = filname.rsplit(".", 1)[1].lower()

    # 許可された拡張子か確認
    allowed_extensions = app.config["ALLOWED_EXTENSIONS"]
    return extentsion in allowed_extensions


@app.route("/create", methods=["GET", "POST"])
@login_required
def create():
    if request.method == "GET":  # リクエストのメソッドの判別
        return render_template("create.html")

    elif request.method == "POST":  # リクエストのメソッドの判別

        # リクエストできた情報の取得
        title = request.form.get("title")
        body = request.form.get("body")

        # 取得したimgファイルをデータベースではなくstaticのimgディレクトリの下に保存する
        # filenameだけをデータベースに保存
        file = request.files["img"]  # htmlで入力されたimgファイルの取得
        filename = (
            file.filename
        )  # そのimgファイルのファイル名を一旦filenameという変数の保存

        if not allowed_file(filename):
            return "許可されていないファイル形式です", 400

        img_name = os.path.join(
            app.static_folder, "img", filename
        )  # staticファイル内の保存先pathの生成
        file.save(img_name)

        # 取得したデータの保存
        post = Post(title=title, body=body, img_name=filename)
        db.session.add(post)
        db.session.commit()

        return redirect("/admin")


@app.route("/<int:post_id>/update", methods=["GET", "POST"])
@login_required
def update(post_id):
    # 編集したいpostの情報をデータベースから取得
    post = Post.query.get(post_id)
    if request.method == "GET":  # リクエストのメソッドの判別
        return render_template("update.html", post=post)

    elif request.method == "POST":  # リクエストのメソッドの判別

        # htmlで更新された内容を取得してpostインスタンスのattributesを更新
        post.title = request.form.get("title")
        post.body = request.form.get("body")

        # 更新したpostオブジェクトをデータベースに保存
        db.session.commit()
        return redirect("/admin")


@app.route("/<int:post_id>/delete")
@login_required
def delete(post_id):
    # 削除したいpostの情報をデータベースから取得
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect("/admin")


if __name__ == "__main__":
    app.run(debug=True)
