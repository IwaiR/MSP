from flask import Flask, Blueprint,render_template,redirect,url_for,request
from DM import yobareru
app = Blueprint('yobu', __name__)
def test2():
    yobareru.test()


    #DBの照合を行うif分の作成

#Controller側はBlueprintを入れる(Main.pyにも追加)
#上記のようにfrom DM import ファイル名と
#ファイル名.関数名()をつける
