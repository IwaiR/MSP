from flask import Flask
import mysql.connector
import os
from func1 import(
    login, CreateAccount, playingMain, myPage,myCollection, yobu,
    accountController,myCollectionController,
    poetryController,compositionController,musicController,playingController
)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

#conn = mysql.connector.connect(user='root', password='root', host='localhost', database='test')
#cur = conn.cursor()

##cur.close
#conn.close
#@app.route('/app1/login')
#def app1_login():
#    return 'app1_login'

#@app.route('/app1/CreateAccount')
#def app1_CreateAccount():
#    return 'app1_CreateAccount'

#@app.route('/app1/playingMain')
#def app1_playingMain():
#    return 'app1_playingMain'


# app.register_blueprint(login.app)
# app.register_blueprint(CreateAccount.app)
# app.register_blueprint(playingMain.app)
# app.register_blueprint(myPage.app)
# app.register_blueprint(myCollection.app)
# app.register_blueprint(yobu.app)
# app.register_blueprint(accountController.app)
app.register_blueprint(myCollectionController.app)
app.register_blueprint(poetryController.app)
app.register_blueprint(compositionController.app)
app.register_blueprint(musicController.app)
app.register_blueprint(playingController.app)


#yobu.test2()

#app.register_blueprint(CreateAccount.app)
#app.register_blueprint(playingMain.app)
if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)

#from app1.playingMain import app1
#app.register_blueprint(app1, url_prefix='/app1')

#from app1.CreateAccount import app1
#app.register_blueprint(app1, url_prefix='/app1')

#if __name__ == "__main__":
#    app.run(host='0.0.0.0')
