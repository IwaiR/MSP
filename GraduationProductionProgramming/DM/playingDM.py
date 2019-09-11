# python playingDM.py

import mysql.connector,DB

playing_tb="playing_tb"
playingdetail_tb="playingdetail_tb"
def getplayingListDB():
    db=DB.access()
    db["cur_dic"].execute("select * from playing_tb")
    result=db["cur_dic"].fetchall()
    DB.close(db)
    return result
def getplayingDetailDB(playingID):
    db=DB.access()
    db["cur_pre"].execute("""
    select * from playingdetail_tb
    where playingID=?
    """,(playingID,))
    result=db["cur_pre"].fetchall()
    DB.close(db)
    return result
def postplayingDataDB(accountID,playingTitle,performer,poet,composer,postDate,playingData_Path):
    db=DB.access()
    try:
        db["cur_pre"].execute("""
        insert into playing_TB(playingTitle,performer,poet,composer,postDate) values(?,?,?,?,?);
        """,(playingTitle,performer,poet,composer,postDate))
        db["cur_dic"].execute("""
        select max(concat(initial,playingID)) as playingID  from playing_TB;
        """)
        id=db["cur_dic"].fetchall()
        try:
            db["cur_pre"].execute("""
            insert into playingDetail_TB(playingID,playingData_Path) values(?,?);
            """,(id[0]["playingID"],playingData_Path))
            db["cur_pre"].execute("""
            insert into mycollection_TB(accountID,myCollectionID) values(?,?);
            """,(accountID,id[0]["playingID"]))
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
# print(getplayingListDB())
# print(getplayingDetailDB("PL00000002"))
# print(postplayingDataDB("0000000001","playing","test","test","test","2019-01-01","test.txt"))