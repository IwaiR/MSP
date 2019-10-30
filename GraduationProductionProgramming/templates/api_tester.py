from flask import Flask, Blueprint,render_template,redirect,url_for, request, jsonify, make_response

app=Blueprint('api_tester', __name__)

@app.route('/api_tester', methods=['GET', 'POST'])
def display_tester():
    return render_template("api_tester.html")
