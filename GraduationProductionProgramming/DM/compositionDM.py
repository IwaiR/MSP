# python compositionDM.py

import mysql.connector
from mysql.connector import Error

# import DB,myCollectionDM
from DM import DB  # Main.py 実行時


composition_tb="composition_tb"
compositiondetail_tb="compositiondetail_tb"
composition_tb_columns=["initial","compositionID","compositionTitle","composer","postDate"]
compositiondetail_tb_columns=["compositionID","compositionData_Path"]
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
    result=DB.Convert_to_dict(compositiondetail_tb_columns,result)
    DB.close(db)
    return result
def postCompositionDataDB(compositionTitle,composer,postDate,compositionData_Path):
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
            db["conn"].commit()
            result=id
        except Error as e:
            db["conn"].rollback()
            result=composition_tb+"\n"+str(e)
    except Error as e:
        db["conn"].rollback()
        result=composition_tb+"\n"+str(e)
    DB.close(db)
    return result
