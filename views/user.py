from flask import request, Blueprint, render_template, redirect
import sqlite3

bp = Blueprint("user", __name__)



@bp.route("/users")
def user_list():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("SELECT id, username, email FROM users")
    data = cursor.fetchall()  # List of tuples - tuple = row in table
    users_list = []
    for item in data:
        user = {
            "id": item[0],
            "username": item[1],
            "email": item[2],
        }
        users_list.append(user)
    return render_template("user-list.html", users=users_list)

@bp.route("/users/<user_id>")
def user_page(user_id):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT username, email FROM users WHERE id = ?",
        [user_id],
    )
    data = cursor.fetchone()
    if data:
        user = {
            "username": data[0],
            "email": data[1],
        }
        return render_template("user-page.html", user=user)
    else:
        return "USER NOT FOUND"


@bp.route("/user/create", methods=["GET", "POST"])
def user_create_form():
    if request.method == "POST":
        print("Creating new user in DB")
        db = sqlite3.connect("data.db")
        cursor = db.cursor()
        new_user = [
            request.form["username"],
            request.form["password"],
            request.form["email"]
        ]
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", new_user)
        db.commit()
        return "USER CREATED"
    return render_template("user-create.html")


@bp.route("/user/<int:user_id>", methods=["DELETE"])
def user_delete(user_id):
    return f"Deleted user successfully {user_id}"


@bp.route("/user/<int:user_id>", methods=["PATCH"])
def user_update(user_id):
    updated_user = request.json()
    return f"Updated user {user_id} with data {updated_user}"

