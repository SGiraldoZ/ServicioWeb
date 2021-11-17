
from flask import Flask, request, Response

from DBC import *

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'This is the inventario Web Service </br></br></br>FuckOff'


@app.route('/webService/inventarioDisp.json', methods=['GET'])
def getAvailableProducts():
    userToken = request.args["user"]
    return {"Products":getOwnerProds(userToken)}

@app.route("/webService/productQt.json", methods=['GET'])
def getProductQuantity():
    userToken = request.args["user"]
    prodId = request.args["product"]
    return {"Products":getOwnerProd(userToken,prodId)}

@app.route("/webService/productInsert", methods = ['GET', 'POST'])
def insertProducts():
    data = request.get_json()
    if data:
        if "nombre" in data:
            nombre = data['nombre']
        if "cantidad" in data:
            cantidad = data['cantidad']
        if "precio" in data:
            precio = data['precio']
        if "owner" in data:
            owner = data['owner']
        ownerId = getOwnerId(owner)
        insertProduct(nombre, cantidad, precio, ownerId)
        return Response(status=200)

    return "<h1> Algo salio mal</h1>"








if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
