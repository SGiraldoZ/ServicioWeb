from ..modelo.Product import Product
from ..DAO.productDAO import *


def getOwnerProducts(ownerId):
    result = find_products_by_owner(ownerId)
    return {"Products": result}

def createProduct(json):
    product = Product.from_Json(json)
    if product:
        create_product(product.name, product.cantidad, product.precio, product.ownerId)
        return True
    return False
