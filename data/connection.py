import pymysql

def get_conncetion():

    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "28102003",
        database = "bot_db",
        port = 3306,
        cursorclass=pymysql.cursors.DictCursor
    )

    return conn
