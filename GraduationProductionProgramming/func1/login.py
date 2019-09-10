from flask import Flask, Blueprint,render_template,redirect,url_for,request
import mysql.connector

app = Blueprint('login', __name__) #ここでの'login'はユニーク

#@app.route('/')
#def index():
#    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
def index():
    # if request.method == 'GET':
    return render_template('login.html')
    # else:
    #     #パラメータを取得
    #     name = request.form['name']
    #     passwd = request.form['pass']
    #     if name == "" or passwd == "":
    #         return '<dialog open>データを入力してください<br><a href="/">戻る</a></dialog>'
    #     #データベースをオープン
    #     con = connect('library.db')
    #     #取得する形式をディクショナリに
    #     con.row_factory = Row
    #     cur = con.cursor()
    #     #データの存在を確認
    #     cur.execute('SELECT * FROM users WHERE name=?', (name, ))
    #     result = cur.fetchall()
    #     con.close
    #     if len(result) != 0:
    #         #パスワードのチェック
    #         for row in result:
    #             if passwd == row['pass']:
    #                 #パスワードが一致したらセッションにユーザー名を登録
    #                 session['username'] = request.form['name']
    #                 #管理者ユーザーの場合は、管理ページに飛ぶ
    #                 if name == "admin" and passwd == row['pass']:
    #                     return redirect(url_for('manager'))
    #                 else:
    #                 #一般ユーザの場合は、図書一覧ページに飛ぶ
    #                     return redirect(url_for('list'))
    #
    #     return '<dialog open>データを入力してください<br><a href="/">戻る</a></dialog>'

#@app.route('/playingMain', methods=['POST'])
#def playingMain():
#    return render_template('playingMain.html')
#上のプログラムは/loginにpostメソッドでusernameとpasswordをreturnしている
