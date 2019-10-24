# python musicDM.py

import mysql.connector
from mysql.connector import Error

# import DB,myCollectionDM
from DM import DB  # Main.py 実行時

music_tb="music_tb"
musicdetail_tb="musicdetail_tb"
music_tb_columns=["initial","musicID","musicTitle","poet","composer","contributor","postDate"]
musicdetail_tb_columns=["musicID","poetryData_Path","compositionData_Path"]
def getMusicListDB():
    db=DB.access()
    db["cur_dic"].execute("select * from music_tb;")
    result=db["cur_dic"].fetchall()
    DB.close(db)
    return result
def getMusicDetailDB(musicID):
    db=DB.access()
    db["cur_pre"].execute("""
    select * from musicdetail_tb
    where musicID=?
    """,(musicID,))
    result=db["cur_pre"].fetchall()
    result=DB.Convert_to_dict(musicdetail_tb_columns,result)
    DB.close(db)
    return result
def postMusicDataDB(musicTitle,poet,composer,contributor,postDate,poetryData_Path,compositionData_Path):
    db=DB.access()
    try:
        db["cur_pre"].execute("""
        insert into music_TB(musicTitle,poet,composer,contributor,postDate) values(?,?,?,?,?);
        """,(musicTitle,poet,composer,contributor,postDate))
        db["cur_dic"].execute("""
        select max(concat(initial,musicID)) as musicID  from music_TB;
        """)
        id=db["cur_dic"].fetchall()
        try:
            db["cur_pre"].execute("""
            insert into musicDetail_TB(musicID,poetryData_Path,compositionData_Path) values(?,?,?);
            """,(id[0]["musicID"],poetryData_Path,compositionData_Path))
            db["conn"].commit()
            result=id
        except Error as e:
            db["conn"].rollback()
            result=music_tb+"\n"+str(e)
    except Error as e:
        db["conn"].rollback()
        result=music_tb+"\n"+str(e)
    DB.close(db)
    return result





# test
# print(getmusicListDB())
# print(getmusicDetailDB("MU00000002"))
# print(postmusicDataDB("0000000001","music","test","test","test","2019-01-01","test.txt","test.txt"))