from flask import Flask
from flask_cors import CORS
from api import User_api
from model import User_model
import pymysql

def create_app():
  app = Flask(__name__)
  CORS(app, supports_credentials=True)

  app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost/test"
  #配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动
  app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
  User_model.db.init_app(app)
  # with app.test_request_context():
  #   User_model.db.create_all()

  app.register_blueprint(User_api.user_api_url, url_prefix='/api/user/')

  # set the secret key.  keep this really secret:
  app.secret_key = b't\xb4\x00M\x00\xce\xc3\x97\x01\xfc@\xe9j33\xcc\x88\x8e\x1e\xab\xf4\xda\x9c\x9a'
  
  # if __name__ == '__main__':
  #   app.run(debug = True)
  return app