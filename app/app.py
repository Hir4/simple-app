import uuid

from database_functions import save_data, get_data
from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("forms.html")


@app.route("/data", methods=["POST", "GET"])
def data_page():
    if request.method == "GET":
        data = get_data()
        return render_template("data.html", form_data=data)
    if request.method == "POST":
        treated_form = dict(request.form)
        treated_form[str(uuid.uuid1())] = treated_form.pop("thought")
        save_data(treated_form)
        return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
