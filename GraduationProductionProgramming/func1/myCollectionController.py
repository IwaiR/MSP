from flask import Blueprint,request,jsonify,make_response
from DM import myCollectionDM

app = Blueprint('myCollectionController', __name__)


# test http://localhost:5000/mycollectionController/getMycollectionRequest?accountID=
@app.route("/mycollectionController/getMycollectionRequest",methods=["GET"])
def getMycollectionRequest():
    params = request.args
    if "accountID" in params:
        result=myCollectionDM.getMyCollectionDB(params["accountID"])
    else:
        result=False
    return make_response(jsonify(result))