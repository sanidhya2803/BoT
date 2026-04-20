import pymysql

def get_conncetion():

    conn = pymysql.connect(
        host = "bov6ijok5h5wiyrgatvt-mysql.services.clever-cloud.com",
        user = "utz3yxtpj7g9p7bk",
        password = "JZwLTangw8caeg77YXYW",
        database = "bov6ijok5h5wiyrgatvt",
        port = 3306,
        cursorclass=pymysql.cursors.DictCursor
    )

    return conn
