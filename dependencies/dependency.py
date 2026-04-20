from data import connection

def connections():
    
    conn = connection.get_conncetion()
    cursor = conn.cursor()

    try:
        yield cursor
    finally:
        cursor.close()
        conn.close()
