from flask import Flask, url_for, redirect
from views.user import bp as user_blueprint
from views.product import bp as product_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint)
app.register_blueprint(product_blueprint)
app.register_blueprint(product_blueprint, url_prefix="/products", name="products")


@app.route("/")
def home():
    return redirect(url_for("product.product_list"))






app.run(debug=True)