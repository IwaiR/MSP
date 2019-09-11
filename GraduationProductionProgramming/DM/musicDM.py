# python musicDM.py

import mysql.connector,DB

music_tb="music_tb"
musicdetail_tb="musicdetail_tb"
def getmusicListDB():
    db=DB.access()
    db["cur"].execute("select * from music_tb;")
    result=db["cur"].fetchall()
    DB.close(db)
    return result
def getmusicDetailDB(musicID):
    db=DB.access()
    db["cur"].execute("""
    select * from musicdetail_tb
    where musicID=?
    """,(musicID,))
    result=db["cur"].fetchall()
    DB.close(db)
    return result
def postmusicDataDB(accountID,musicTitle,poet,composer,contributor,postDate,poetryData_Path,compositionData_Path):
    db=DB.access()
    try:
        db["cur"].execute("""
        insert into music_TB(musicTitle,poet,composer,contributor,postDate) values(?,?,?,?,?);
        """,(musicTitle,poet,composer,contributor,postDate))
        db["cur"].execute("""
        select max(concat(initial,musicID)) as musicID  from music_TB;
        """)
        id=db["cur"].fetchall()
        try:
            db["cur"].execute("""
            insert into musicDetail_TB(musicID,poetryData_Path,compositionData_Path) values(?,?,?);
            """,(id[0][0],poetryData_Path,compositionData_Path))
            db["cur"].execute("""
            insert into mycollection_TB(accountID,myCollectionID) values(?,?);
            """,(accountID,id[0][0]))
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
# print(getmusicListDB())
# print(getmusicDetailDB("MU00000002"))
# print(postmusicDataDB("0000000001","music","test","test","test","2019-01-01","test.txt","test.txt"))