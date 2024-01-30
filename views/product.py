from dataclasses import dataclass
from flask import  request, Blueprint, url_for, redirect, request
from models.product import Product, product_create

bp = Blueprint("product", __name__, url_prefix="/products")





@bp.route("")
def product_list():
    # list_of_products = get_list_of_products()
    return "List of all products"


@bp.route("/<product_id>")
def product_page(product_id):
    return f"page for product {Product.get_product_by_id(product_id)}"


@bp.route("/create", methods=["GET", "POST"])
def product_create():
    if request.method == "GET":
        return "product create form"
    elif request.method == "POST":
        new_product = product_create("new product", 1.99, 10, "the best product")
        print(f"creating product: {new_product}")
        return "create product successfully" 

@bp.route("/<product_id>", methods=["DELETE"])
def product_delete(product_id):
    return f"deleted product successfully {product_id}"

@bp.route("/<product_id>", methods=["PATCH"])
def product_update(product_id):
    updated_product = request.json("id")
    print(f"updated product {product_id} with data {updated_product}")
    product_page_url = url_for("product.product_page", product_id=product_id)
    return redirect(product_page_url)