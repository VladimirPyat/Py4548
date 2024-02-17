import pymysql
from config import host, user, password, port, db_name

try:
    connection = pymysql.connect(
    host = host,
    user = user,
    port = port,
    password = password,
    database = db_name,
    cursorclass = pymysql.cursors.DictCursor
    )
    print ("Succesfully connected")

    try:
        cursor = connection.cursor()
        cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS phones (
        id SERIAL PRIMARY KEY,
        product_name VARCHAR(45) NOT NULL,
        price INT NOT NULL); """)

        cursor.execute(""" 
                INSERT phones (product_name, price) VALUES ("iPhone X", "76000"),
                ("iPhone 8", "51000"),
                ("Galaxy S9", "56000");
                 """)

        cursor.execute("SELECT * FROM phones")
        rows = cursor.fetchall()
        print(rows)

        connection.commit() # после insert, update, delete
    finally:
        connection.close()

except Exception as ex:
    print ("Error")
    print(ex)