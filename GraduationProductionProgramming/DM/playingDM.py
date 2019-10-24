# python playingDM.py

import mysql.connector
from mysql.connector import Error

# import DB,myCollectionDM
from DM import DB  # Main.py 実行時

playing_tb="playing_tb"
playingdetail_tb="playingdetail_tb"
playing_tb_columns=["initial","playingID","playingTitle","performer","poet","composer","postDate"]
playingdetail_tb_columns=["playingID","playingData_Path"]
def getPlayingListDB():
    db=DB.access()
    db["cur_dic"].execute("select * from playing_tb")
    result=db["cur_dic"].fetchall()
    DB.close(db)
    return result
def getPlayingDetailDB(playingID):
    db=DB.access()
    db["cur_pre"].execute("""
    select * from playingdetail_tb
    where playingID=?
    """,(playingID,))
    result=db["cur_pre"].fetchall()
    result=DB.Convert_to_dict(playingdetail_tb_columns,result)
    DB.close(db)
    return result
def postPlayingDataDB(playingTitle,performer,poet,composer,postDate,playingData_Path):
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
            db["conn"].commit()
            result=id
        except Error as e:
            db["conn"].rollback()
            result=playing_tb+"\n"+str(e)
    except Error as e:
        db["conn"].rollback()
        result=playing_tb+"\n"+str(e)
    DB.close(db)
    return result





# test
# print(getplayingListDB())
# print(getplayingDetailDB("PL00000002"))
# print(postplayingDataDB("0000000001","playing","test","test","test","2019-01-01","test.txt"))