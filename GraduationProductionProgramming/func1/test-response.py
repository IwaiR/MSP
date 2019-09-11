from flask import Flask, request, jsonify, make_response
app = Flask(__name__)

@app.route("/hoge", methods=['GET'])
def getHoge():
    # URLパラメータ
    params = request.args
    response = {}
    for param in params:
        response.setdefault(param,params[param])
    return make_response(jsonify(response))

@app.route("/hoge",methods=["POST"])
def postHoge():
    # ボディ(application/json)パラメータ
    params = request.json
    response = {}
    for param in params:
        response.setdefault(param,params[param])
    return make_response(jsonify(response))


if __name__ == '__main__':
    app.run(host='localhost', port=5000)