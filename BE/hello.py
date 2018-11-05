from flask import Flask, session, redirect, url_for, escape, request
app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # session['username'] = request.form['username']
        return '2000'
    return '200'

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = b't\xb4\x00M\x00\xce\xc3\x97\x01\xfc@\xe9j33\xcc\x88\x8e\x1e\xab\xf4\xda\x9c\x9a'

if __name__ == '__main__':
  app.run(debug = True, host='127.0.0.1', port=5000)