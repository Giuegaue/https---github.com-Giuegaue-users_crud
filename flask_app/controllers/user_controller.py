from flask import render_template, redirect, session, request

from flask_app import app
from flask_app.models.user import User


@app.route("/")
def index():
    all_users = User.get_all()
    print(all_users)
    return render_template("index.html", all_users = all_users)


@app.route("/user/add")
def new_user():
    return render_template("add_user.html")


@app.route("/user/create", methods = ["POST"])
def create_user():
    User.create(request.form)
    print(request.form)
    return redirect("/")


@app.route("/user/<id>/edit")
def edit(id):
    return render_template("edit_user.html", user = User.get_one({"id": id}))


@app.route("/user/<id>/update", methods = ["POST"])
def update_user(id):
    print(request.form)
    data = {
        **request.form,
        "id": id
    }
    User.update(data)
    return redirect(f"/user/{id}")


@app.route("/user/<id>")
def display_user(id):
    return render_template("user_page.html", user = User.get_one({"id": id}))

@app.route("/user/<id>/delete")
def delete(id):
    User.delete({"id": id})
    return redirect("/")
