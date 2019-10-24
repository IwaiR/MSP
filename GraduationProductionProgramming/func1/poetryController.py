from flask import Blueprint,request,jsonify,make_response
from DM import poetryDM,accountDM,myCollectionDM

app = Blueprint('poetryController', __name__)


# test http://localhost:5000/poetryController/getPoetryList
@app.route("/poetryController/getPoetryList",methods=["GET"])
def getPoetryList():
    poetryList=[]
    poetryList=poetryDM.getPoetryListDB()
    return make_response(jsonify(poetryList))


# test http://localhost:5000/poetryController/getPoetryDetail?poetryID=
@app.route("/poetryController/getPoetryDetail",methods=["GET"])
def getPoetryDetail():
    poetryDetail=[]
    params = request.args
    try:
        poetryDetail=poetryDM.getPoetryDetailDB(params["poetryID"])
    except:
        pass
    return make_response(jsonify(poetryDetail))


# test http://localhost:5000/poetryController/postPoetryData?
# UUID=&poetryTitle=&postDate=&poetryData_Path=
@app.route("/poetryController/postPoetryData",methods=["GET"])
def postPoetryData():
    params = request.args
    try:
        UUID=params["UUID"]
        try:
            accountinfo=accountDM.getAccountinfoDB(UUID)[0]
            accountID=accountinfo["accountID"]
            poet=accountinfo["accountName"]
        except:
            return "does not exist UUID"
        poetryTitle=params["poetryTitle"]
        postDate=params["postDate"]
        poetryData_Path=params["poetryData_Path"]
        result=poetryDM.postPoetryDataDB(poetryTitle,poet,postDate,poetryData_Path)
        try:
            id=result[0]["poetryID"]
        except:
            return result+"\n Failed to post to mycollection_tb"
        result=myCollectionDM.postMycollectionDataDB(accountID,id)
    except:
        result=False
    return make_response(jsonify(result))