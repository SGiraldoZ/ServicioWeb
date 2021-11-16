
from flask import Flask, request

from DBC import getOwnerProds, getOwnerProd

app = Flask(__name__)


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






if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
