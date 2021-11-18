import mysql.connector
from ...DBC import connect

CREATE_USER = '''INSERT INTO Owner (Id, Name)
                VALUE (%s, %s);'''

GET_OWNER_ID = '''SELECT Id FROM Owner
                  WHERE Name LIKE %s;'''

GET_OWNER_LIST = '''Select * FROM Owner;'''

def get_owner_id(owner):
    conn = connect()
    cur = conn.cursor()
    cur.execute(GET_OWNER_ID, (owner,))
    result = cur.fetchone()
    conn.close()
    return result[0]

def get_all_owners():
    conn = connect()
    cur = conn.cursor(dictionary=True)
    cur.execute(GET_OWNER_LIST)
    result = cur.fetchall()
    conn.close()
    return result