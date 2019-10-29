from flask import Flask
import mysql.connector
import os
from func1 import(
    accountController,myCollectionController,
    poetryController,compositionController,musicController,playingController
)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


app.register_blueprint(accountController.app)
app.register_blueprint(myCollectionController.app)
app.register_blueprint(poetryController.app)
app.register_blueprint(compositionController.app)
app.register_blueprint(musicController.app)
app.register_blueprint(playingController.app)


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)

#from app1.playingMain import app1
#app.register_blueprint(app1, url_prefix='/app1')

#from app1.CreateAccount import app1
#app.register_blueprint(app1, url_prefix='/app1')

#if __name__ == "__main__":
#    app.run(host='0.0.0.0')
