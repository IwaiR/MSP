# python compositionDM.py

import mysql.connector,DB

composition_tb="composition_tb"
compositiondetail_tb="compositiondetail_tb"
def getCompositionListDB():
    db=DB.access()
    db["cur_dic"].execute("select * from composition_tb;")
    result=db["cur_dic"].fetchall()
    DB.close(db)
    return result
def getCompositionDetailDB(compositionID):
    db=DB.access()
    db["cur_pre"].execute("""
    select * from compositiondetail_tb
    where compositionID=?
    """,(compositionID,))
    result=db["cur_pre"].fetchall()
    DB.close(db)
    return result
def postCompositionDataDB(accountID,compositionTitle,composer,postDate,compositionData_Path):
    db=DB.access()
    try:
        db["cur_pre"].execute("""
        insert into composition_TB(compositionTitle,composer,postDate) values(?,?,?);
        """,(compositionTitle,composer,postDate))
        db["cur_dic"].execute("""
        select max(concat(initial,compositionID)) as compositionID  from composition_TB;
        """)
        id=db["cur_dic"].fetchall()
        try:
            db["cur_pre"].execute("""
            insert into compositionDetail_TB(compositionID,compositionData_Path) values(?,?);
            """,(id[0]["compositionID"],compositionData_Path))
            db["cur_pre"].execute("""
            insert into mycollection_TB(accountID,myCollectionID) values(?,?);
            """,(accountID,id[0]["compositionID"]))
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