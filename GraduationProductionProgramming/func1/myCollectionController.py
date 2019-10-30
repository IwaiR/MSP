from flask import Blueprint,request,jsonify,make_response
import re
from DM import myCollectionDM,accountDM

app = Blueprint('myCollectionController', __name__)


class MyCollectionID:
    pattern="(PO|CO|MU|PL)[\\d]{8}"
    def __init__(self,id):
        self.id=id
    def check(self):
        result=re.match(self.pattern,self.id)
        if result:
            return True
        return False
    def pattern_check(mycollectionid):
        result=re.match(MyCollectionID.pattern,mycollectionid)
        if result:
            return True
        return False


# test http://localhost:5000/mycollectionController/getMycollection?UUID=
@app.route("/mycollectionController/getMycollection",methods=["GET"])
def getMycollection():
    myCollectionList=[]
    params = request.args
    try:
        UUID=params["UUID"]
        try:
            accountID=accountDM.getAccountInfoDB(UUID)[0]["accountID"]
        except:
            return make_response(jsonify(myCollectionList))
        myCollectionList=myCollectionDM.getMyCollectionDB(accountID)
    except:
        pass
    return make_response(jsonify(myCollectionList))


# test http://localhost:5000/mycollectionController/deleteMyCollection?UUID=&mycollectionID=
@app.route("/mycollectionController/deleteMyCollection",methods=["GET"])
def deleteMyCollection():
    result=False
    params = request.args
    try:
        UUID=params["UUID"]
        mycollectionID=params["mycollectionID"]
        # mycollectionIDのデータチェック
        if not MyCollectionID.pattern_check(mycollectionID):
            return "Invalid mycollectionID"
        try:
            accountID=accountDM.getAccountInfoDB(UUID)[0]["accountID"]
        except:
            return make_response(jsonify(result))
        result=myCollectionDM.deleteMyCollectionDB(accountID,mycollectionID)
    except:
        pass
    return make_response(jsonify(result))


# test http://localhost:5000/mycollectionController/postMycollectionData?UUID=&mycollectionID=
@app.route("/mycollectionController/postMycollectionData",methods=["GET"])
def postMycollectionData():
    params = request.args
    try:
        UUID=params["UUID"]
        mycollectionID=params["mycollectionID"]
        # mycollectionIDのデータチェック
        if not MyCollectionID.pattern_check(mycollectionID):
            return "Invalid mycollectionID"
        try:
            accountID=accountDM.getAccountInfoDB(UUID)[0]["accountID"]
        except:
            return "does not exist UUID"
        result=myCollectionDM.postMycollectionDataDB(accountID,mycollectionID)
    except:
        result=False
    return make_response(jsonify(result))
