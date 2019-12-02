from flask import Flask, session, redirect, url_for, escape, request,jsonify,abort,Response 
from flask.blueprints import Blueprint
import sys
sys.path.append("..")
from model import User_model

user_api_url = Blueprint('user_api_url', __name__)

@user_api_url.route('/login', methods=['POST'])
def login():
    admin = User_model.User(userName='admin', phone='138999999997')
    User_model.db.session.add(admin)
    User_model.db.session.commit()
    userName = ''
    if 'username' in session:
        userName = session['username']
    else:
        session['username'] = request.form['username']
        userName = session['username']
    res = {'success': True,'userName': userName}
    return jsonify(res)

@user_api_url.route('/register', methods=['POST'])
def register():
    admin = User_model.User(userName='admin', phone='138999999997')
    User_model.db.session.add(admin)
    User_model.db.session.commit()
    userName = ''
    return jsonify(res)

@user_api_url.route('/logout',methods=['POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return '200'