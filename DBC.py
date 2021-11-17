import mysql.connector

OWNER_PRODS_QUERY='''SELECT Id, Nombre AS 'Producto', Precio, Cantidad
                    FROM Inventory WHERE OwnerId LIKE %s;'''


OWNER_PRODUCT_QUERY='''SELECT Id, Nombre, Cantidad
                        FROM Inventory WHERE OwnerId LIKE %s
                        AND Id = %s;'''

CREATE_USER = '''INSERT INTO Owner (Id, Name)
                VALUE (%s, %s);'''

INSERT_PRODUCT = '''INSERT INTO Product (Nombre, Cantidad, Precio, OwnerId)
                    VALUE (%s, %s, %s, %s)'''

GET_OWNER_ID = '''SELECT Id FROM OWNER 
                  WHERE Name LIKE %s'''

# crear la conexión

def connect():
    conn = mysql.connector.connect(host="remotemysql.com",
                                   database="varDt01HvK",
                                   user="varDt01HvK",
                                   password="gQa4TK4SvA"
                                   )

    return conn

# def executeQuery(query):
#     conn = connect()
#     cur = conn.cursor(dictionary=True)
#     cur.execute(query)
#     result = cur.fetchall()
#     conn.close()
#     return result


def getOwnerProds(userToken):
    conn = connect()
    cur = conn.cursor(dictionary=True)
    cur.execute(OWNER_PRODS_QUERY, (userToken,))
    result = cur.fetchall()
    conn.close()
    return result

def getOwnerProd(userToken, prodId):
    conn = connect()
    cur = conn.cursor(dictionary=True)
    cur.execute(OWNER_PRODUCT_QUERY, (userToken,prodId))
    result = cur.fetchall()
    conn.close()
    return result

def insertProduct(nombre, cantidad, precio, owner):
    conn = connect()
    cur = conn.cursor()
    cur.execute(INSERT_PRODUCT, (nombre, cantidad, precio, owner))
    conn.commit()
    conn.close()

def getOwnerId(owner):
    conn = connect()
    cur = conn.cursor()
    cur.execute(GET_OWNER_ID, (owner,))
    result = cur.fetchone()
    conn.close()
    return result[0]