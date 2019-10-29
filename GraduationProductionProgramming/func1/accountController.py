from flask import Flask, Blueprint,render_template,redirect,url_for, request, jsonify, make_response
import mysql.connector
# from ..DM import accountDM
#from ..DM
#import sys
#sys.path.append('../')
from DM import accountDM
#import C:\Users\k016c1297\Desktop\GIT2\GraduationProductionProgramming_sample\DM\accountDM
#import 呼ぶファイル名
app = Blueprint('accountContoller', __name__)

@app.route('/accountContoller/registration', methods=['GET', 'POST'])#ファイル名+関数名
def registration():
    #APIを使ったレスポンス↓
    #with app.test_request_context():
    params = request.args
    response = {}
    try: #accountNameのパラメーターがなければtry文でexceptにいくここかないとパラメーターに入力がなくても実行されてしまう
        accountName = params["accountName"]#accountNameパラメーターがある前提にする

        result=accountDM.CheckAcocountName(accountName)
        if result == True:
            UUID=params["UUID"]
            # accountName
            response=accountDM.insert(params["UUID"], params['accountName'], params['specialtyID'], params['profilePhoto_Path'], params['comment'], params['specialtyInstrument'])
        #response.setdefault('res', 'UUID : ' + params.get('UUID') + ' accountName : '+ params.get('accountName') + ' specialtyID :  ' + params.get('specialtyID') + ' profilePhoto_Path : ' + params.get('profilePhoto_Path') + ' comment : ' + params.get('comment') + ' specialtyInstrument : ' + params.get('specialtyInstrument'))
    # body = { "param" : "accountContoller"}
    # response = make_response(jsonify(body))
    # response.headers['registration'] = 'accountContoller...'
        else:
            response=False

        return make_response(jsonify(response))
    except:
        return "False"


    #accountDM.UUID=params["UUID"]
    # accountName
    #/accountContoller/registrationの後、?UUID=0001&accountName="Iwai"...とパラメーターを書く
    #if 'UUID' in params and 'accountName' in params and 'specialtyID' in params and 'profilePhoto_Path' in params and 'comment' in params and 'specialtyInstrument' in params:



    # accountDM.insert(UUID, accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument)

    #テスト用パラメーター↓
    # UUID = "00000000000000000000000000000002"#htmlとつなぐ前にテスト
    # accountName = "IwaiR"
    # specialtyID = "4"
    # profilePhoto_Path = "https://IwaiR_Photo.txt"
    # comment = "よろしくお願いします！"
    # specialtyInstrument = "ギター"
    # accountDM.insert(UUID, accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument)#URLのパラメーターを想定して

@app.route('/accountContoller/getAccountInfo', methods=['GET', 'POST'])#ファイル名+関数名
#テストOK path:http://localhost:5000/accountContoller/getAccountInfo?UUID=001
def getAccountInfo():#tryほしい
    response = {}
    params = request.args
    try:
        UUID=params["UUID"]
        accountDM.getAccountInfoDB(UUID)
        result = accountDM.getAccountInfoDB(UUID)
        response = result
        #print(accountDM.getAccountInfoDB(UUID))
        return make_response(jsonify(response))
    except:
        return False

@app.route('/accountContoller/updateAccountInfo', methods=['GET', 'POST'])#ファイル名+関数名
#テストOK Path:http://localhost:5000/accountContoller/updateAccountInfo?accountName=IwaiR&specialtyID=3&profilePhoto_Path=IwaiNPhoto.txt&comment=&specialtyInstrument=&UUID=001
def updateAccountInfo():#UUIDもわたす　print(result)ほしい
    params = request.args
    response = {}
    try:
        accountName = params["accountName"]
        specialtyID = params["specialtyID"]
        profilePhoto_Path = params["profilePhoto_Path"]
        comment = params["comment"]
        specialtyInstrument = params["specialtyInstrument"]
        UUID = params["UUID"]

        #accountDM.updateAccountInfoDB(accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument, UUID)
        # if 'accountName' in params and 'specialtyID' in params and 'profilePhoto_Path' in params and 'comment' in params and 'specialtyInstrument' in params and 'UUID' in params:
        #      response.setdefault('res','accountName : '+ params.get('accountName') + 'specialtyID :  ' + params.get('specialtyID') + 'profilePhoto_Path : ' + params.get('profilePhoto_Path') + 'comment : ' + params.get('comment') + 'specialtyInstrument : ' + params.get('specialtyInstrument') + 'UUID : ' + params.get('UUID'))
        result = accountDM.updateAccountInfoDB(accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument, UUID)
        response = result
        return make_response(jsonify(response))
    except:
        return "False"

    # accountName = "IwaiL"
    # specialtyID = "1"
    # profilePhoto_Path = "https://IwaiL_Photo.txt"
    # comment = "実は楽器ができない"
    # specialtyInstrument = "なし"
    # UUID = "00000000000000000000000000000001"#htmlとつなぐ前にテスト

    #accountDM.updateAccountInfoDB(accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument)
    #引数にUUIDをもってきてほしい
    #returnで返ってきて画面にreturnする
#UUID=001&accountName="IwaiR"&specialtyID="1"&profilePhoto_Path="IwaiPhoto.txt"&comment="よろしく"&specialtyInstrument="なし"
