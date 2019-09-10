from flask import Flask, Blueprint,render_template,redirect,url_for
import mysql.connector

app = Blueprint('playingMain', __name__)

@app.route('/playingMain')
def playingMain():
    return render_template('playingMain.html')


    #DBの照合を行うif分の作成
