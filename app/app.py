import json
import uuid

from flask import Flask, redirect, render_template, request

from db.save_data import save_data

app = Flask(__name__)


@app.route("/")
def main_page():
    return render_template("forms.html")


@app.route("/data", methods=["POST", "GET"])
def data_page():
    # if request.method == "GET":
    #     filename = "./db/phrases.json"
    #     with open(filename, "r") as read_file:
    #         treatedJson = json.load(read_file)
    #         return render_template("data.html", form_data=treatedJson)
    # if request.method == "POST":
    #     treated_form = dict(request.form)
    #     treated_form[str(uuid.uuid1())] = treated_form.pop("thought")
    #     save_data(treated_form)
    #     return redirect("/")
    import psycopg2

    conn = psycopg2.connect(database="db_simple_app",
                            host="172.18.0.2",
                            user="user_fael",
                            password="test123",
                            port="5432")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM thoughts WHERE id = 1")
    print(cursor.fetchone())
    return cursor.fetchone()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
