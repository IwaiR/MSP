from flask import Flask, Blueprint,render_template,redirect,url_for,request
from urllib.parse import urlparse
import mysql.connector

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

#DBへのSQL文とContorollerへの記述↓
def CreateAccountDM():
    conn.commit()
    cur = conn.cursor()
    cur.execute("""INSERT INTO account_MS (accountID, UUID, accountName, specialtyID,
    profilePhoto_Path, comment, specialtyInstrument) values (?, ?, ?, ?, ?, ?, ?)""",(, , , , ))

    conn.close()
#return /CreateAccount.py

# conn.ping(reconnect=True)
#

# cur.execute('SELECT * FROM account_ms')
# cur.fetchall()
#
# cur = conn.cursor(dictionary=True)
#
# cur.fetchall()

# #def CreateAccount():
#    print('アカウントを作成しました')

#if __name__ == '__main__':
#    CreateAccount()

#print('モジュール名: {}'.format(__name__))


#DMはBlueprintをいれる必要なし
#呼ばれる関数を記述する
#最終的にはreturnでController側に返すのも忘れずに

    #DBの照合を行うif分の作成
