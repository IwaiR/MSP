# python poetryDM.py

import mysql.connector,DB,myCollectionDM

poetry_tb="poetry_tb"
poetrydetail_tb="poetrydetail_tb"
def getPoetryListDB():
    db=DB.access()
    db["cur"].execute("select * from poetry_tb;")
    result=db["cur"].fetchall()
    DB.close(db)
    return result
def getPoetryDetailDB(poetryID):
    db=DB.access()
    db["cur"].execute("""
    select * from poetrydetail_tb 
    where poetryID=?
    """,(poetryID,))
    result=db["cur"].fetchall()
    DB.close(db)
    return result
def postPoetryDataDB(poetryTitle,poet,postDate,poetryData_Path):
    db=DB.access()
    try:
        db["cur"].execute("""
        insert into poetry_TB(poetryTitle,poet,postDate) values(?,?,?);
        """,(poetryTitle,poet,postDate,))
        db["cur"].execute("""
        select max(concat(initial,poetryID)) as poetryID  from poetry_TB;
        """)
        id=db["cur"].fetchall()
        print(id[0][0])
        try:
            db["cur"].execute("""
            insert into poetryDetail_TB(poetryID,poetryData_Path) values(?,?);
            """,(id[0][0],poetryData_Path,))
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
        id=result[0][0]
    except:
        return False
    result=myCollectionDM.postMycollectionDataDB(accountID,id)
    return result
    
        



# test
# print(getPoetryListDB())
# print(getPoetryDetailDB("PO00000001"))
# print(postPoetryDataDB("0000000001","poetry","test","2019-01-01","test.txt"))
# print(postPoetryData("00000000001","poetry","test","2019-01-01","test.txt"))