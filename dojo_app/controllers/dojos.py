from flask import render_template, redirect, request
from dojo_app.models.dojo import Dojo
from dojo_app import app


@app.route("/")
def reroute_to_home():
    return redirect("/dojos")


@app.route("/dojos")
def display_home():
    dojos = Dojo.get_all()
    return render_template("index.html", dojos=dojos)


@app.post("/dojos/added")
def create_dojo():
    Dojo.create(request.form)
    return redirect("/")

@app.route('/dojo/<int:dojo_id>')
def display_dojos(dojo_id):
    dojos = Dojo.get_one(dojo_id)
    return render_template('dojo_table.html', dojos=dojos)