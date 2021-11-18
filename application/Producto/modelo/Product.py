import json

class Product:
    def __init__(self, name, cantidad, precio, ownerId):
        self.name = name
        self.cantidad = cantidad
        self.precio = precio
        self.ownerId = ownerId
        
    @staticmethod
    def from_Json(json):
        if json:
            if "nombre" in json:
                nombre = json['nombre']
            else:
                return None
            if "cantidad" in json:
                cantidad = json['cantidad']
            else:
                return None
            if "precio" in json:
                precio = json['precio']
            else:
                return None
            if "ownerId" in json:
                ownerId = json['ownerId']
            else:
                return None
        return Product(nombre, cantidad, precio, ownerId)

    def to_Json(self):
        myDict = {}
        myDict["Producto"] = self.name
        myDict["Cantidad"] = self.cantidad
        myDict["Precio"] = self.precio
        myDict["Id"] = self.id
        myDict["ownerId"] = self.ownerId

        return json.dumps(myDict)

