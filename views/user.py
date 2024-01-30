from flask import  request, Blueprint

bp = Blueprint("user", __name__)


@bp.route("/user")
def user_list():
    return "user list"

@bp.route("/user/<user_id>")
def user_page(user_id):
    return f"page for user {user_id}"

@bp.route("/user/create", methods=["GET", "POST"])
def user_create():
    if request.method == "GET":
        return "user create form"
    elif request.method == "POST":
        return "created user successfully"
    
@bp.route("/user/<int:user_id>", methods=["DELETE"])
def user_delete(user_id):
    return f"deleted user successfully {user_id}"

@bp.route("/user/<int:user_id>", methods=["PATCH"])
def user_update(user_id):
    updated_user = request.json("id")
    return f"updated user {user_id} with data {updated_user}"