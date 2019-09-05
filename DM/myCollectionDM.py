# python myCollectionDM.py

import mysql.connector,DB

myCollection_tb="myCollection_tb"
def getMyCollectionDB(accountID):
    db=DB.access()
    db["cur"].execute("""
    select * from {0}
    where accountID="{1}";
    """.format(myCollection_tb,accountID))
    result=db["cur"].fetchall()
    DB.close(db)
    return result
def deleteMyCollectionDB(accountID,myCollectionID):
    db=DB.access()
    try:
        db["cur"].execute("""
        delete from {0}
        where accountID="{1}" and mycollectionID="{2}";
        """.format(myCollection_tb,accountID,myCollectionID))
        db["conn"].commit()
        result=True
    except:
        db["conn"].rollback()
        result=False
    DB.close(db)
    return result
def postMycollectionDataDB(accountID,myCollectionID):
    db=DB.access()
    try:
        db["cur"].execute("""
        insert into mycollection_TB(accountID,myCollectionID) values("{0}","{1}");
        """.format(accountID,myCollectionID))
        db["conn"].commit()
        result=True
    except:
        db["conn"].rollback()
        result=False
    DB.close(db)
    return result



# accountDM
def getAccountinfoDB(UUID):
    db=DB.access()
    db["cur"].execute("""
    select * from account_ms
    where UUID="{0}";
    """.format(UUID))
    result=db["cur"].fetchall()
    DB.close(db)
    return result



# test
UUID="uuid"
accountID=getAccountinfoDB(UUID)[0]["accountID"]
# print(getMyCollectionDB(accountID))
# print(getAccountinfoDB(UUID))
# print(deleteMyCollectionDB(accountID,"PO00000009"))