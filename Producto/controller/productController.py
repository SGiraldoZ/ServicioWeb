from flask import Blueprint, request, Response


product_controller = Blueprint("product",__name__)

@product_controller.route('/inventarioDisp.json', methods=['GET'])
def getAvailableProducts():
    userToken = request.args["user"]
    return {"Products":getOwnerProds(userToken)}

@product_controller.route("/productQt.json", methods=['GET'])
def getProductQuantity():
    userToken = request.args["user"]
    prodId = request.args["product"]
    return {"Products":getOwnerProd(userToken,prodId)}

@product_controller.route("/productInsert", methods = ['GET', 'POST'])
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