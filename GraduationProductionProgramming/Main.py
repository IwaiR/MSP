from flask import Flask
import mysql.connector
import os
from func1 import(
    accountController,myCollectionController,
    poetryController,compositionController,musicController,playingController
)
from templates import(
    api_tester
)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)


app.register_blueprint(accountController.app)
app.register_blueprint(myCollectionController.app)
app.register_blueprint(poetryController.app)
app.register_blueprint(compositionController.app)
app.register_blueprint(musicController.app)
app.register_blueprint(playingController.app)
# for test
app.register_blueprint(api_tester.app)


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=5000)

