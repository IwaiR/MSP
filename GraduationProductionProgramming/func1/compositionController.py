from flask import Blueprint,request,jsonify,make_response
from DM import compositionDM,accountDM,myCollectionDM

app = Blueprint('compositionController', __name__)


# test http://localhost:5000/compositionController/getPoetryList
@app.route("/compositionController/getPoetryList",methods=["GET"])
def getCompositionList(): 
    compositionList=[]
    compositionList=compositionDM.getCompositionListDB()
    return make_response(jsonify(compositionList))


# test http://localhost:5000/compositionController/getCompositionDetail?compositionID=
@app.route("/compositionController/getCompositionDetail",methods=["GET"])    
def getCompositionDetail(): 
    compositionDetail=[]
    params = request.args
    try:
        compositionDetail=compositionDM.getCompositionDetailDB(params["compositionID"])
    except:
        pass
    return make_response(jsonify(compositionDetail))


# test http://localhost:5000/compositionController/postCompositionData?
# UUID=&compositionTitle=&postDate=&compositionData_Path=
@app.route("/compositionController/postCompositionData",methods=["GET"])    
def postCompositionData(): 
    params = request.args
    try:
        UUID=params["UUID"]
        try:
            accountinfo=accountDM.getAccountinfoDB(UUID)[0]
            accountID=accountinfo["accountID"]
            composer=accountinfo["accountName"]
        except:
            return "does not exist UUID"
        compositionTitle=params["compositionTitle"]
        postDate=params["postDate"]
        compositionData_Path=params["compositionData_Path"]
        result=compositionDM.postCompositionDataDB(compositionTitle,composer,postDate,compositionData_Path)
        try: # resultからcompositionIDを取得
            id=result[0]["compositionID"]
        except:
            return result+"\n Failed to post to mycollection_tb"
        result=myCollectionDM.postMycollectionDataDB(accountID,id)
    except:
        result=False
    return make_response(jsonify(result))