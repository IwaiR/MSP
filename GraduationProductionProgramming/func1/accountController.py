from flask import Flask, Blueprint,render_template,redirect,url_for, request, jsonify, make_response
import mysql.connector
from DM import accountDM

app = Blueprint('accountContoller', __name__)


#テスト http://localhost:5000/accountContoller/registration?UUID=&
# accountName=&specialtyID=&profilePhoto_Path=&comment=&specialtyInstrument=
@app.route('/accountContoller/registration', methods=['GET', 'POST'])#ファイル名+関数名
def registration():
    params = request.args
    response = {}
    try: 
        accountName = params["accountName"]
        result=accountDM.CheckAcocountName(accountName)
        if result == True:
            response=accountDM.insert(params["UUID"], params['accountName'], params['specialtyID'], params['profilePhoto_Path'], params['comment'], params['specialtyInstrument'])
        else:
            response=False
    except:
        response=False
    return make_response(jsonify(response))


#テスト http://localhost:5000/accountContoller/getAccountInfo?UUID=001
@app.route('/accountContoller/getAccountInfo', methods=['GET', 'POST'])
def getAccountInfo():
    response = {}
    params = request.args
    try:
        UUID=params["UUID"]
        accountDM.getAccountInfoDB(UUID)
        result = accountDM.getAccountInfoDB(UUID)
        response = result
    except:
        response=False
    return make_response(jsonify(response))


#テスト http://localhost:5000/accountContoller/updateAccountInfo?accountName=&specialtyID=&profilePhoto_Path=&comment=&specialtyInstrument=&UUID=
@app.route('/accountContoller/updateAccountInfo', methods=['GET', 'POST'])
def updateAccountInfo():
    params = request.args
    response = {}
    try:
        accountName = params["accountName"]
        specialtyID = params["specialtyID"]
        profilePhoto_Path = params["profilePhoto_Path"]
        comment = params["comment"]
        specialtyInstrument = params["specialtyInstrument"]
        UUID = params["UUID"]
        result = accountDM.updateAccountInfoDB(accountName,  specialtyID, profilePhoto_Path, comment, specialtyInstrument, UUID)
        response = result
    except:
        response=False
    return make_response(jsonify(response))