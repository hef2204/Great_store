import sqlite3
from flask import redirect, request, Blueprint, url_for, render_template

from models.product import Product, ProductCreate

bp = Blueprint("product", __name__, url_prefix="/product")


@bp.route("")
def product_list():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("SELECT id, title, description, price, image FROM products")
    data = cursor.fetchall()  # List of tuples - tuple = row in table
    product_list = []
    for item in data:
        product = {
            "id": item[0],
            "title": item[1],
            "description": item[2],
            "price": item[3],
            "image": item[4],
        }
        product_list.append(product)
    return render_template("product-list.html", products=product_list)


@bp.route("/products/<product_id>")
def product_page(product_id):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(
        "SELECT id, title, description, price, image FROM products WHERE id = ?",
        [product_id],
    )
    data = cursor.fetchone()
    if data:
        product = {
            "id": data[0],
            "title": data[1],
            "description": data[2],
            "price": data[3],
            "image": data[4],
        }
        return render_template("product.html", product=product)
    else:
        return "PRODUCT NOT FOUND"

@bp.route("/create_product", methods=["GET", "POST"])
def product_create_form():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT category FROM products")
    data = cursor.fetchall()
    # categories = [row[0] for row in data]
    return render_template("product-create.html", categories=data)




@bp.route("/<int:product_id>", methods=["PATCH"])
def product_update(product_id):
    updated_product = request.json()
    print(f"Updated product {product_id} with data {updated_product}")
    product_page_url = url_for("product.product_page", product_id=product_id)
    return redirect(product_page_url)

@bp.route('/create_product/submit', methods=['POST'])
def product_create_submit():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    if request.method == "POST":
        new_product = ProductCreate(
            title=request.form["title"],
            price=request.form["price"],
            description=request.form["description"],
            image=request.form["image"],
            category=request.form["category"]
        )
        cursor.execute("INSERT INTO products (title, price, description, image, category) VALUES (?, ?, ?, ?, ?)",
                       (new_product.title, new_product.price, new_product.description, new_product.image, new_product.category))
        db.commit()
        return redirect(url_for("product.product_list"))

@bp.route('/delete/<product_id>')
def delete_product(product_id):
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute("DELETE FROM products WHERE id = ?", [product_id])
    if cursor.rowcount == 1:
        db.commit()
        return ("success", 200)
    if cursor.rowcount == 0:
        return ("", 404)
    return ("", 500)




