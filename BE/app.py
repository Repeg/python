from flask import Flask, session, redirect, url_for, escape, request,jsonify,abort,Response 
from flask_cors import CORS
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
import pymysql
app = Flask(__name__)
CORS(app, supports_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/test"

#配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动

app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#获取SQLAlchemy实例对象，接下来就可以使用对象调用数据
db = SQLAlchemy(app)

#创建模型对象
class User(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(80), unique=True, nullable=False,primary_key=True)
    phone = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/login', methods=['POST'])
def login():
    admin = User(userName='admin', phone='138999999997')
    db.session.add(admin)
    db.session.commit()
    userName = ''
    if 'username' in session:
        userName = session['username']
    else:
        session['username'] = request.form['username']
        userName = session['username']
    res = {'success': True,'userName': userName}
    return jsonify(res)

@app.route('/logout',methods=['POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return '200'

# set the secret key.  keep this really secret:
app.secret_key = b't\xb4\x00M\x00\xce\xc3\x97\x01\xfc@\xe9j33\xcc\x88\x8e\x1e\xab\xf4\xda\x9c\x9a'

if __name__ == '__main__':
  app.run(debug = True)