from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, URLField, SubmitField, TimeField, SelectField
from wtforms.validators import DataRequired, URL
from datetime import datetime
import csv


app = Flask(__name__)
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


class CafeForm(FlaskForm):
    coffee_emojies = ["☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"]
    wifi_emojies = ["✘", "🛜", "🛜🛜", "🛜🛜🛜", "🛜🛜🛜🛜", "🛜🛜🛜🛜🛜"]
    power_sockets = ["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]
    cafe_name = StringField("Cafe Name", validators=[DataRequired()])
    location_URL = URLField(
        "Location URL from GoogleMap ", validators=[DataRequired(), URL()]
    )
    open_time = TimeField("Open Time", validators=[DataRequired()])
    close_time = TimeField("Close Time", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating", choices=coffee_emojies, validators=[DataRequired()]
    )
    wifi_rating = SelectField(
        "WiFi Rating", choices=wifi_emojies, validators=[DataRequired()]
    )
    power_outlet = SelectField(
        "Power Socket Availability", choices=power_sockets, validators=[DataRequired()]
    )
    submit = SubmitField("Submit")


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


def time_formatter(time: datetime.time):
    time_format = "%I:%M %p"
    return time.strftime(time_format)


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe_name.data
        location = form.location_URL.data
        open_time = time_formatter(form.open_time.data)
        close_time = time_formatter(form.close_time.data)
        coffe_rating = form.coffee_rating.data
        wifi = form.wifi_rating.data
        power = form.power_outlet.data
        new_data = [
            cafe_name,
            location,
            open_time,
            close_time,
            coffe_rating,
            wifi,
            power,
        ]
        with open("./cafe-data.csv", "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(new_data)
        return render_template("index.html")
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    data = []
    with open("cafe-data.csv", newline="", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data.append(row)
    return render_template("cafes.html", cafes=data)


if __name__ == "__main__":
    app.run(debug=True)
