import mysql.connector

def access():
    db={}
    conn = mysql.connector.connect(user="root", password='kamata', host='localhost', database='smp')
    db["conn"]=conn
    db["cur_dic"]=conn.cursor(dictionary=True) #dict型でデータを取得：{column:値}
    db["cur_pre"]=conn.cursor(prepared=True)   #SQL文内に？を使用して、引数を指定するために使う
    db["cur_buff"]=conn.cursor(buffered=True)  #
    return db
def close(db):
    db["cur_dic"].close()
    db["cur_pre"].close()
    db["cur_buff"].close()
    db["conn"].close()


def Convert_to_dict(columns,result):
    dictResult=[]
    for data in result:
        dict={}
        for i in range(len(columns)):
            dict[columns[i]]=data[i]
        dictResult.append(dict)
    return dictResult