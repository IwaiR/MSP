from flask import Flask, Blueprint,render_template,redirect,url_for
import mysql.connector

app = Blueprint('myPage', __name__)

@app.route('/myPage')
def myPage():
    #DMの呼び出し

    return render_template('myPage.html')
