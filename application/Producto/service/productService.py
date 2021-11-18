from ..modelo.Product import Product
from ..DAO.productDAO import *
from application.Owner.service.ownerService import getOwnerId


def getOwnerProducts(ownerId):
    result = find_products_by_owner(ownerId)
    return {"Products": result}

def createProduct(json):
    json["ownerId"] = getOwnerId(json["owner"])
    # CONSEGUIR PRODUCT ID CON OWNER DAO
    product = Product.from_Json(json)
    if product:
        create_product(product.name, product.cantidad, product.precio, product.ownerId)
        return True
    return False
