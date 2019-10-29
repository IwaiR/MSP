from flask import Flask, Blueprint,render_template,redirect,url_for,request, jsonify, make_response
from urllib.parse import urlparse
import mysql.connector
from mysql.connector import Error
from DM import DB
#import DB
#url = urlparse('mysql://k016c1297:kamata@localhost:3306/msp')
#下記で通信を確立ここから↓
conn = mysql.connector.connect(
    host ='localhost',
    #port = url.port or 3306,
    user = 'root',
    password =  'kamata',
    database = 'msp',
)
#conn.is_connected
#ここまで↑
account_ms_columns=["accountID","UUID","accountName",
"specialtyID","profilePhoto_Path","comment"
,"specialtyInstrument"]


#python Main.py
def CheckAcocountName(accountName):#accountNameはもらってくる値(今回はaccountControllerから)
#テストOK UUID=004&accountName=IwaiL&specialtyID=1&profilePhoto_Path=IwaiLPhoto.txt&comment=&specialtyInstrument=なし
    conn = mysql.connector.connect(
        host ='localhost',
        #port = url.port or 3306,
        user = 'root',
        password =  'kamata',
        database = 'msp',
    )

    cur = conn.cursor(prepared=True)#?を使う時　これをdictionary=Trueにするとdictionary型の形で取得できる
    #入力されたアカウント名の内容が被っていないかの処理↓
    try:
        cur.execute('SELECT * from account_MS where accountName =?', (accountName,))
        #cur.execute('SELECT count(accountName) duplicate_count, accountName from accountName group by account_MS')
        a = len(cur.fetchall())
        #b = len(a) #長さでtrueかどうかを分岐させる
        if a == 0:
            return True
        else:
            return False
    except Error as e:
        result=e

    return result


#DBへのSQL文とContorollerへの記述↓
def insert(UUID, accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument):
    cur = conn.cursor(prepared=True)#?を使う時　これをdictionary=Trueにするとdictionary型の形で取得できる
    try:
        cur.execute('''INSERT INTO account_MS (UUID, accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument) values (?, ?, ?, ?, ?, ?)'''
        ,(UUID, accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument))
        conn.commit()
        result=True
    except Error as e:
        conn.rollback()
        result=str(e)
    cur.close()
    # conn.close()
    return result

# def getAccountInfoDB(UUID):

def getAccountInfoDB(UUID):
#テストOK path:http://localhost:5000/accountContoller/getAccountInfo?UUID=001
    conn = mysql.connector.connect(
        host ='localhost',
        #port = url.port or 3306,
        user = 'root',
        password =  'kamata',
        database = 'msp',
    )
    #global conn

    cur = conn.cursor(prepared=True)#?を使う時　これをdictionary=Trueにするとdictionary型の形で取得できる
    try:
        cur.execute('SELECT * from account_MS where UUID=?', (UUID,))
        #conn.commit() selectはcommitいらない
        result=cur.fetchall()
        result=DB.Convert_to_dict(account_ms_columns, result)
        #account_ms_columns(上記)をresultにいえる account_ms_columns内の全てのデータがないと成り立たない
    except:
        #conn.rollback()
        result=False
    conn.close()
    return result

#updateはTrue or False の形で返す
def updateAccountInfoDB(accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument, UUID):
    conn = mysql.connector.connect(
        host ='localhost',
        #port = url.port or 3306,
        user = 'root',
        password =  'kamata',
        database = 'msp',
    )

    cur = conn.cursor(prepared=True)#?を使う時　これをdictionary=Trueにするとdictionary型の形で取得できる
    try:
        cur.execute('''update account_MS set accountName= ?, specialtyID=?, profilePhoto_Path=?,
        comment=?, specialtyInstrument=? where UUID= ? ''', (accountName, specialtyID, profilePhoto_Path, comment, specialtyInstrument, UUID))
        conn.commit()
        result=True
    except Error as e:
        print("error",e)
        conn.rollback()
        result=False
    conn.close()
    return result

#print(getAccountInfoDB('00000000000000000000000000000001'))
#DMはBlueprintをいれる必要なし
#呼ばれる関数を記述する
