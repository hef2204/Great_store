from flask import  request, Blueprint

product_blueprint = Blueprint("product", __name__)



@product_blueprint.route("/product")
def product_list():
    return "List of all products"


@product_blueprint.route("/product/<product_id>")
def product_page(product_id):
    product_id = request.args.get("id") 
    return f"page for product with id {product_id}"


@product_blueprint.route("/product/create", methods=["GET", "POST"])
def product_create():
    if request.method == "GET":
        return "product create form"
    elif request.method == "POST":
        return "create product successfully" 

@product_blueprint.route("/product/<product_id>", methods=["DELETE"])
def product_delete(product_id):
    return f"deleted product successfully {product_id}"

@product_blueprint.route("/product/<product_id>", methods=["PATCH"])
def product_update(product_id):
    updated_product = request.json("id")
    return f"updated product {product_id} with data {updated_product}"