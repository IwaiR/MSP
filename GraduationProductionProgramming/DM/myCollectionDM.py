# python myCollectionDM.py

import mysql.connector
from mysql.connector import Error

# import DB
from DM import DB  # Main.py 実行時

myCollection_tb="myCollection_tb"
account_ms_columns=["accountID","UUID","accountName",
"specialtyID","profilePhoto_Path","comment"
,"specialtyInstrument"]
myCollection_tb_columns=["accountID","myCollectionID"]
def getMyCollectionDB(accountID):
    db=DB.access()
    db["cur_pre"].execute("""
    select * from myCollection_tb
    where accountID=?;
    """,(accountID,))
    result=db["cur_pre"].fetchall()
    result=DB.Convert_to_dict(myCollection_tb_columns,result)
    DB.close(db)
    return result
def deleteMyCollectionDB(accountID,myCollectionID):
    db=DB.access()
    db["cur_pre"].execute("""
    select * from mycollection_tb
    where accountID=? and mycollectionID=?;
    """,(accountID,myCollectionID))
    result=db["cur_pre"].fetchall()
    if len(result)==0:
        return False
    try:
        db["cur_pre"].execute("""
        delete from myCollection_tb
        where accountID=? and mycollectionID=?;
        """,(accountID,myCollectionID))
        db["conn"].commit()
        result=True
    except Error as e:
        db["conn"].rollback()
        result=myCollection_tb+"\n"+str(e)
    DB.close(db)
    return result
def postMycollectionDataDB(accountID,myCollectionID):
    db=DB.access()
    try:
        db["cur_pre"].execute("""
        insert into mycollection_TB(accountID,myCollectionID) values(?,?);
        """,(accountID,myCollectionID))
        db["conn"].commit()
        result=True
    except Error as e :
        db["conn"].rollback()
        result=myCollection_tb+"\n"+str(e)
    DB.close(db)
    return result



# accountDM
def getAccountinfoDB(UUID):
    db=DB.access()
    db["cur_pre"].execute("""
    select * from account_ms
    where UUID=?;
    """,(UUID,))
    result=db["cur_pre"].fetchall()
    DB.close(db)
    result=DB.Convert_to_dict(account_ms_columns,result)
    return result
    


# test
# UUID="uuid"
# accountID="0000000001"
# accountinfo=getAccountinfoDB(UUID)
# print(accountinfo)
# result=getMyCollectionDB(accountID)
# print(result)
# print(getAccountinfoDB(UUID))
# print(deleteMyCollectionDB(accountID,"PL00000002"))
# print(postMycollectionDataDB("11","dfghjkjhgfdfghjkjhs"))

