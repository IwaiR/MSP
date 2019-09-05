# python playingDM.py

import mysql.connector,DB

playing_tb="playing_tb"
playingdetail_tb="playingdetail_tb"
def getplayingListDB():
    db=DB.access()
    db["cur"].execute("""
    select * from {0}
    """.format(playing_tb))
    result=db["cur"].fetchall()
    DB.close(db)
    return result
def getplayingDetailDB(playingID):
    db=DB.access()
    db["cur"].execute("""
    select * from {0}
    where playingID="{1}"
    """.format(playingdetail_tb,playingID))
    result=db["cur"].fetchall()
    DB.close(db)
    return result
def postplayingDataDB(accountID,playingTitle,performer,poet,composer,postDate,playingData_Path):
    db=DB.access()
    try:
        db["cur"].execute("""
        insert into playing_TB(playingTitle,performer,poet,composer,postDate) values("{0}","{1}","{2}","{3}","{4}");
        """.format(playingTitle,performer,poet,composer,postDate))
        db["cur"].execute("""
        select max(concat(initial,playingID)) as playingID  from playing_TB;
        """)
        id=db["cur"].fetchall()
        try:
            db["cur"].execute("""
            insert into playingDetail_TB(playingID,playingData_Path) values("{0}","{1}");
            """.format(id[0]["playingID"],playingData_Path))
            db["cur"].execute("""
            insert into mycollection_TB(accountID,myCollectionID) values("{0}","{1}");
            """.format(accountID,id[0]["playingID"]))
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
print(getplayingListDB())
print(getplayingDetailDB("PL00000001"))
# print(postplayingDataDB("0000000001","playing","test","test","test","2019-01-01","test.txt"))