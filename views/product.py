from flask import  request, Blueprint

bp = Blueprint("product", __name__, url_prefix="/products")



@bp.route("")
def product_list():
    return "List of all products"


@bp.route("/<product_id>")
def product_page(product_id):
    product_id = request.args.get("id") 
    return f"page for product with id {product_id}"


@bp.route("/create", methods=["GET", "POST"])
def product_create():
    if request.method == "GET":
        return "product create form"
    elif request.method == "POST":
        return "create product successfully" 

@bp.route("/<product_id>", methods=["DELETE"])
def product_delete(product_id):
    return f"deleted product successfully {product_id}"

@bp.route("/<product_id>", methods=["PATCH"])
def product_update(product_id):
    updated_product = request.json("id")
    return f"updated product {product_id} with data {updated_product}"