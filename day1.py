import mysql.connector as conc

def connection1():
    return conc.connect(
        host="localhost",
        user="root",
        password="M.S.SA***",
        database="MYSQLPRAC"
    )
print("connected successfully")