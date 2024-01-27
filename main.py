from flask import Flask
from user import user_blueprint
from product import product_blueprint

app = Flask(__name__)
app.register_blueprint(user_blueprint)
app.register_blueprint(product_blueprint)






app.run(debug=True)