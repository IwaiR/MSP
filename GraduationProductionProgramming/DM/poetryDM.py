# python poetryDM.py

import mysql.connector
from mysql.connector import Error

# import DB,myCollectionDM
from DM import DB  # Main.py 実行時

poetry_tb="poetry_tb"
poetrydetail_tb="poetrydetail_tb"
poetry_tb_columns=["initial","poetryID","poetryTitle","composer","postDate"]
poetrydetail_tb_columns=["poetryID","poetryData_Path"]
def getPoetryListDB():
    db=DB.access()
    db["cur_dic"].execute("select * from poetry_tb;")
    result=db["cur_dic"].fetchall()
    DB.close(db)
    return result
def getPoetryDetailDB(poetryID):
    db=DB.access()
    db["cur_pre"].execute("""
    select * from poetrydetail_tb 
    where poetryID=?
    """,(poetryID,))
    result=db["cur_pre"].fetchall()
    result=DB.Convert_to_dict(poetrydetail_tb_columns,result)
    DB.close(db)
    return result
def postPoetryDataDB(poetryTitle,poet,postDate,poetryData_Path):
    db=DB.access()
    try:
        db["cur_pre"].execute("""
        insert into poetry_TB(poetryTitle,poet,postDate) values(?,?,?);
        """,(poetryTitle,poet,postDate))
        db["cur_dic"].execute("""
        select max(concat(initial,poetryID)) as poetryID  from poetry_TB;
        """)
        id=db["cur_dic"].fetchall()
        try:
            db["cur_pre"].execute("""
            insert into poetryDetail_TB(poetryID,poetryData_Path) values(?,?);
            """,(id[0]["poetryID"],poetryData_Path,))
            db["conn"].commit()
            result=id
        except Error as e:
            db["conn"].rollback()
            result=poetry_tb+"\n"+str(e)
    except Error as e:
        db["conn"].rollback()
        result=poetry_tb+"\n"+str(e)
    DB.close(db)
    return result



# test
# print(getPoetryListDB())
# print(getPoetryDetailDB("PO00000001"))
# print(postPoetryDataDB("0000000001","poetry","test","2019-01-01","test.txt"))
# print(postPoetryData("00000000001","poetry","test","2019-01-01","test.txt"))