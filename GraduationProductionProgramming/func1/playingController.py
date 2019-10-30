from flask import Blueprint,request,jsonify,make_response
from DM import playingDM,accountDM,myCollectionDM

app = Blueprint('playingController', __name__)


# test http://localhost:5000/playingController/getPlayingList
@app.route("/playingController/getPlayingList",methods=["GET"])
def getPlayingList(): 
    playingList=[]
    playingList=playingDM.getPlayingListDB()
    return make_response(jsonify(playingList))


# test http://localhost:5000/playingController/getPlayingDetail?playingID=
@app.route("/playingController/getPlayingDetail",methods=["GET"])    
def getPlayingDetail(): 
    playingDetail=[]
    params = request.args
    try:
        playingDetail=playingDM.getPlayingDetailDB(params["playingID"])
    except:
        pass
    return make_response(jsonify(playingDetail))


# test http://localhost:5000/playingController/postPlayingData?
# UUID=&playingTitle=&poet=&composer=&postDate=&playingData_Path=
@app.route("/playingController/postPlayingData",methods=["GET"])    
def postPlayingData(): 
    params = request.args
    try:
        UUID=params["UUID"]
        try:
            accountinfo=accountDM.getAccountInfoDB(UUID)[0]
            accountID=accountinfo["accountID"]
            performer=accountinfo["accountName"]
        except:
            return "does not exist UUID"
        playingTitle=params["playingTitle"]
        poet=params["poet"]
        composer=params["composer"]
        postDate=params["postDate"]
        playingData_Path=params["playingData_Path"]
        result=playingDM.postPlayingDataDB(playingTitle,performer,poet,composer,postDate,playingData_Path)
        try: # resultからplayingIDを取得
            id=result[0]["playingID"]
        except:
            return result+"\n Failed to post to mycollection_tb"
        result=myCollectionDM.postMycollectionDataDB(accountID,id)
    except:
        result=False
    return make_response(jsonify(result))