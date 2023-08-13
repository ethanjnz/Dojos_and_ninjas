from dojo_app import app
from flask import render_template, redirect, request
from dojo_app.models.dojo import Dojo
from dojo_app.models.ninja import Ninja

@app.route("/ninjas")
def display_form():
    dojos = Dojo.get_all()
    return render_template('ninja_form.html', dojos=dojos)


@app.post('/ninja/add')
def process_ninja():
    Ninja.create(request.form)
    return redirect(f'/dojo/{request.form["dojo_id"]}')