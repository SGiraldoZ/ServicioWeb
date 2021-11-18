import mysql.connector
from ...DBC import connect

CREATE_USER = '''INSERT INTO Owner (Id, Name)
                VALUE (%s, %s);'''

GET_OWNER_ID = '''SELECT Id FROM Owner
                  WHERE Name LIKE %s;'''


def get_owner_id(owner):
    conn = connect()
    cur = conn.cursor()
    cur.execute(GET_OWNER_ID, (owner,))
    result = cur.fetchone()
    conn.close()
    return result[0]