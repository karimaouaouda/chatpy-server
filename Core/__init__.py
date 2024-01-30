import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="chatpy"
)

db_cursor = mydb.cursor()


def cursor():
    return db_cursor
