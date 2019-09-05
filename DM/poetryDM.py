# python poetryDM.py

import mysql.connector,DB

poetry_tb="poetry_tb"
poetrydetail_tb="poetrydetail_tb"
def getPoetryListDB():
    db=DB.access()
    db["cur"].execute("""
    select * from {0}
    """.format(poetry_tb))
    result=db["cur"].fetchall()
    DB.close(db)
    return result
def getPoetryDetailDB(poetryID):
    db=DB.access()
    db["cur"].execute("""
    select * from {0}
    where poetryID="{1}"
    """.format(poetrydetail_tb,poetryID))
    result=db["cur"].fetchall()
    DB.close(db)
    return result
def postPoetryDataDB(accountID,poetryTitle,poet,postDate,poetryData_Path):
    db=DB.access()
    try:
        db["cur"].execute("""
        insert into poetry_TB(poetryTitle,poet,postDate) values("{0}","{1}","{2}");
        """.format(poetryTitle,poet,postDate))
        db["cur"].execute("""
        select max(concat(initial,poetryID)) as poetryID  from poetry_TB;
        """)
        id=db["cur"].fetchall()
        try:
            db["cur"].execute("""
            insert into poetryDetail_TB(poetryID,poetryData_Path) values("{0}","{1}");
            """.format(id[0]["poetryID"],poetryData_Path))
            db["cur"].execute("""
            insert into mycollection_TB(accountID,myCollectionID) values("{0}","{1}");
            """.format(accountID,id[0]["poetryID"]))
            db["conn"].commit()
            result=True
        except:
            result=False
            db["conn"].rollback()
    except:
        result=False
        db["conn"].rollback()
    DB.close(db)
    return result





# test
print(getPoetryListDB())
print(getPoetryDetailDB("P000000001"))
# print(postPoetryDataDB("0000000001","poetry","test","2019-01-01","test.txt"))