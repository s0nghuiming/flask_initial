from flask import Flask, request, render_template


app = Flask(__name__)

# curl -X POST --data "username=Kevin&password=1" 127.0.0.1:5000/login
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

def valid_login(username='', password=''):
    pass
    print("User: " + username)
    print("Password: " + password)
