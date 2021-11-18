import mysql.connector

def connect():
    conn = mysql.connector.connect(host="remotemysql.com",
                                   database="varDt01HvK",
                                   user="varDt01HvK",
                                   password="gQa4TK4SvA"
                                   )

    return conn