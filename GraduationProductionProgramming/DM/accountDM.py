from flask import Flask, Blueprint,render_template,redirect,url_for,request, jsonify, make_response
from urllib.parse import urlparse
import mysql.connector
from mysql.connector import Error
from DM import DB


account_ms_columns=["accountID","UUID","accountName",
"specialtyID","profilePhoto_Path","comment"
,"specialtyInstrument"]


#python Main.py
def CheckAcocountName(accountName):
#テストOK UUID=004&accountName=IwaiL&specialtyID=1&profilePhoto_Path=IwaiLPhoto.txt&comment=&specialtyInstrument=なし
    db=DB.access()
    cur = db["cur_pre"]
    #入力されたアカウント名の内容が被っていないかの処理↓
    try:
        cur.execute('SELECT * from account_MS where accountName =?', (accountName,))
        a = len(cur.fetchall())
        #b = len(a) #長さでtrueかどうかを分岐させる
        if a == 0:
            result=True
        else:
            result=False
    except Error as e:
        result=str(e)
    DB.close(db)
    return result


#DBへのSQL文とContorollerへの記述↓
def insert(UUID, accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument):
    db=DB.access()
    cur=db["cur_pre"]
    conn=db["conn"]
    try:
        cur.execute('''INSERT INTO account_MS (UUID, accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument) values (?, ?, ?, ?, ?, ?)'''
        ,(UUID, accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument))
        conn.commit()
        result=True
    except Error as e:
        conn.rollback()
        result=str(e)
    DB.close(db)
    return result


def getAccountInfoDB(UUID):
#テストOK path:http://localhost:5000/accountContoller/getAccountInfo?UUID=001
    db=DB.access()
    cur=db["cur_pre"]
    try:
        cur.execute('SELECT * from account_MS where UUID=?', (UUID,))
        result=cur.fetchall()
        result=DB.Convert_to_dict(account_ms_columns, result)
    except:
        result=False
    DB.close(db)
    return result

#updateはTrue or False の形で返す
def updateAccountInfoDB(accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument, UUID):
    db=DB.access()
    cur=db["cur_pre"]
    conn=db["conn"]
    try:
        cur.execute('''update account_MS set accountName= ?, specialtyID=?, profilePhoto_Path=?,
        comment=?, specialtyInstrument=? where UUID= ? ''', (accountName, specialtyID, profilePhoto_Path, comment, specialtyInstrument, UUID))
        conn.commit()
        result=True
    except:
        conn.rollback()
        result=False
    DB.close(db)
    return result
