# python accountDM.py

import mysql.connector
from mysql.connector import Error

# import DB,myCollectionDM
from DM import DB  # Main.py 実行時

account_ms="account_ms"
account_ms_columns=["accountID","UUID","accountName",
"specialtyID","profilePhoto_Path","comment"
,"specialtyInstrument"]

def getAccountinfoDB(UUID):
    db=DB.access()
    db["cur_pre"].execute("""
    select * from account_ms
    where UUID=? ;
    """,(UUID,))
    result=db["cur_pre"].fetchall()
    result=DB.Convert_to_dict(account_ms_columns,result)
    DB.close(db)
    return result