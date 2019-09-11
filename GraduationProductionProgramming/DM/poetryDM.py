# python poetryDM.py

import mysql.connector
import DB
# import myCollectionDM

poetry_tb="poetry_tb"
poetrydetail_tb="poetrydetail_tb"
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
    DB.close(db)
    return result
def postPoetryDataDB(poetryTitle,poet,postDate,poetryData_Path):
    db=DB.access()
    try:
        db["cur_pre"].execute("""
        insert into poetry_TB(poetryTitle,poet,postDate) values(?,?,?);
        """,(poetryTitle,poet,postDate,))
        db["cur_dic"].execute("""
        select max(concat(initial,poetryID)) as poetryID  from poetry_TB;
        """)
        id=db["cur_dic"].fetchall()
        print(id[0]["poetryID"])
        try:
            db["cur_pre"].execute("""
            insert into poetryDetail_TB(poetryID,poetryData_Path) values(?,?);
            """,(id[0]["poetryID"],poetryData_Path,))
            db["conn"].commit()
            result=id
        except:
            db["conn"].rollback()
            result=False
    except:
        db["conn"].rollback()
        result=False
    DB.close(db)
    return result



# poetryController
def postPoetryData(accountID,poetryTitle,poet,postDate,poetryData_Path):
    #accountidを確認する処理が必要
    result=postPoetryDataDB(poetryTitle,poet,postDate,poetryData_Path)
    try:
        id=result[0]["poetryID"]
    except:
        return False
    result=myCollectionDM.postMycollectionDataDB(accountID,id)
    return result
    
        



# test
print(getPoetryListDB())
# print(getPoetryDetailDB("PO00000001"))
# print(postPoetryDataDB("0000000001","poetry","test","2019-01-01","test.txt"))
# print(postPoetryData("00000000001","poetry","test","2019-01-01","test.txt"))