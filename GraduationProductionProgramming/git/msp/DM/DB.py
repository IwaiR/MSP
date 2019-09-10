import mysql.connector

def access():
    db={}
    conn = mysql.connector.connect(user="root", password='kamata', host='localhost', database='smp')
    cur =conn.cursor(dictionary=True)
    # cur =conn.cursor()
    db["conn"]=conn
    db["cur"]=cur
    return db
def close(db):
    db["cur"].close()
    db["conn"].close()