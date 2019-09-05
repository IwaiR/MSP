# python compositionDM.py

import mysql.connector,DB

composition_tb="composition_tb"
compositiondetail_tb="compositiondetail_tb"
def getCompositionListDB():
    db=DB.access()
    db["cur"].execute("""
    select * from {0};
    """.format(composition_tb))
    result=db["cur"].fetchall()
    DB.close(db)
    return result
def getCompositionDetailDB(compositionID):
    db=DB.access()
    db["cur"].execute("""
    select * from {0}
    where compositionID="{1}"
    """.format(compositiondetail_tb,compositionID))
    result=db["cur"].fetchall()
    DB.close(db)
    return result
def postCompositionDataDB(accountID,compositionTitle,composer,postDate,compositionData_Path):
    db=DB.access()
    try:
        db["cur"].execute("""
        insert into composition_TB(compositionTitle,composer,postDate) values("{0}","{1}","{2}");
        """.format(compositionTitle,composer,postDate))
        db["cur"].execute("""
        select max(concat(initial,compositionID)) as compositionID  from composition_TB;
        """)
        id=db["cur"].fetchall()
        try:
            db["cur"].execute("""
            insert into compositionDetail_TB(compositionID,compositionData_Path) values("{0}","{1}");
            """.format(id[0]["compositionID"],compositionData_Path))
            db["cur"].execute("""
            insert into mycollection_TB(accountID,myCollectionID) values("{0}","{1}");
            """.format(accountID,id[0]["compositionID"]))
            db["conn"].commit()
            result=True
        except:
            db["conn"].rollback()
            result=False
    except:
        db["conn"].rollback()
        result=False
    DB.close(db)
    return result





# test
# print(getCompositionListDB())
# print(getCompositionDetailDB("CO00000001"))
# print(postCompositionDataDB("0000000002","composition","test","2019-01-01","test.txt"))