from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    # def __init__(self, email=None, phone=None, password=None, active=True,userName=None, id=None):
    #     self.email = email
    #     self.phone = phone
    #     self.password = password
    #     self.active = active
    #     self.userName = userName
    #     self.isAdmin = False
    #     self.id = None
    # id = db.Column(db.Integer, primary_key=True)

    userName = db.Column(db.String(80), unique=True, nullable=False,primary_key=True)
    phone = db.Column(db.String(120), unique=True, nullable=False)