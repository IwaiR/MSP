from flask import Blueprint,request,jsonify,make_response
from DM import musicDM,accountDM,myCollectionDM

app = Blueprint('musicController', __name__)


# test http://localhost:5000/musicController/getMusicList
@app.route("/musicController/getMusicList",methods=["GET"])
def getMusicList(): 
    musicList=[]
    musicList=musicDM.getMusicListDB()
    return make_response(jsonify(musicList))


# test http://localhost:5000/musicController/getMusicDetail?musicID=
@app.route("/musicController/getMusicDetail",methods=["GET"])    
def getMusicDetail(): 
    musicDetail=[]
    params = request.args
    try:
        musicDetail=musicDM.getMusicDetailDB(params["musicID"])
    except:
        pass
    return make_response(jsonify(musicDetail))


# test http://localhost:5000/musicController/postMusicData?
# UUID=&musicTitle=&poet=&composer=&postDate=&poetryData_Path=&compositionData_Path=
@app.route("/musicController/postMusicData",methods=["GET"])    
def postMusicData(): 
    params = request.args
    try:
        UUID=params["UUID"]
        try:
            accountinfo=accountDM.getAccountInfoDB(UUID)[0]
            accountID=accountinfo["accountID"]
            contributor=accountinfo["accountName"]
        except:
            return "does not exist UUID"
        musicTitle=params["musicTitle"]
        poet=params["poet"]
        composer=params["composer"]
        postDate=params["postDate"]
        poetryData_Path=params["poetryData_Path"]
        compositionData_Path=params["compositionData_Path"]
        result=musicDM.postMusicDataDB(musicTitle,poet,composer,contributor,postDate,poetryData_Path,compositionData_Path)
        try: # resultからmusicIDを取得
            id=result[0]["musicID"]
        except:
            return result+"\n Failed to post to mycollection_tb"
        result=myCollectionDM.postMycollectionDataDB(accountID,id)
    except:
        result=False
    return make_response(jsonify(result))