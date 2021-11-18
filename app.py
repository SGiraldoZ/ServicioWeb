
from flask import Flask
from application.Producto.controller.productController import product_controller
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(product_controller, url_prefix="/webService")

@app.route('/')
def hello_world():  # put application's code here
    return 'This is the inventario Web Service </br></br></br>FuckOff'



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
