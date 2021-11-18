from flask import Blueprint, request, Response
from ..service.productService import *

product_controller = Blueprint("product",__name__)

@product_controller.route('/inventarioDisp.json', methods=['GET'])
def getAvailableProducts():
    userToken = request.args["user"]
    return getOwnerProducts(userToken)

@product_controller.route("/productInsert", methods = ['GET', 'POST'])
def insertProducts():
    data = request.get_json()
    productCreated = createProduct(data)
    if productCreated:
        return Response(status=200)
    return Response(status=400)

@product_controller.route("/exists", methods = ['GET'])
def productExists():
    product = request.args["product"]
    return {"Exists": product_exists_by_name(product)}