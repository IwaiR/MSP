from flask import Flask, Blueprint,render_template,redirect,url_for
import mysql.connector

app = Blueprint('myCollection', __name__)

@app.route('/myCollection')
def myCollection():
    return render_template('myCollection.html')


    #DBの照合を行うif分の作成
