from flask import Flask, Blueprint,render_template,redirect,url_for, request
import mysql.connector
from DM import CreateAccountDM
#import 呼ぶファイル名
app = Blueprint('CreateAccount', __name__)

@app.route('/CreateAccount', methods=['GET', 'POST'])
def CreateAccount():
    if request.method == 'GET':
        return render_template('CreateAccount.html')
    else:
        CreateAccountDM.CreateAccountDM()

    #引数にUUIDをもってきてほしい
    #returnで返ってきて画面にreturnする
    return render_template('playingMain.html')
