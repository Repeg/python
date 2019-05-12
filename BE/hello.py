from flask import Flask, session, redirect, url_for, escape, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/api/login', methods=['POST'])
def login():
    if 'username' in session:
        return session['username']
    else:
        session['username'] = request.form['username']
        return '200'

@app.route('/logout',methods=['POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return '200'

# set the secret key.  keep this really secret:
app.secret_key = b't\xb4\x00M\x00\xce\xc3\x97\x01\xfc@\xe9j33\xcc\x88\x8e\x1e\xab\xf4\xda\x9c\x9a'

if __name__ == '__main__':
  app.run(debug = True)