import mysql.connector
from ...DBC import connect

OWNER_PRODS_QUERY='''SELECT Id, Nombre AS 'Producto', Precio, Cantidad
                    FROM Inventory WHERE OwnerId LIKE %s;'''


OWNER_PRODUCT_QUERY='''SELECT Id, Nombre, Cantidad
                        FROM Inventory WHERE OwnerId LIKE %s
                        AND Id = %s;'''

INSERT_PRODUCT = '''INSERT INTO Inventory (Nombre, Cantidad, Precio, OwnerId)
                    VALUE (%s, %s, %s, %s);'''

PRODUCT_EXISTS_BY_NAME = '''SELECT COUNT(Id) FROM INVENTORY
                            WHERE Nombre LIKE %s'''


def find_products_by_owner(userToken):
    conn = connect()
    cur = conn.cursor(dictionary=True)
    cur.execute(OWNER_PRODS_QUERY, (userToken,))
    result = cur.fetchall()
    conn.close()
    return result

def find_product_by_owner_and_id(userToken, prodId):
    conn = connect()
    cur = conn.cursor(dictionary=True)
    cur.execute(OWNER_PRODUCT_QUERY, (userToken,prodId))
    result = cur.fetchall()
    conn.close()
    return result

def create_product(nombre, cantidad, precio, owner):
    conn = connect()
    cur = conn.cursor()
    cur.execute(INSERT_PRODUCT, (nombre, cantidad, precio, owner))
    conn.commit()
    conn.close()

def product_exists_by_name(name):
    conn = connect()
    cur = conn.cursor()
    cur.execute(PRODUCT_EXISTS_BY_NAME, (name,))
    result = cur.fetchall()[0]
    return result >= 1