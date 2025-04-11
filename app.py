from flask import Flask, render_template, request
from logic.auth import handle_login

app = Flask(__name__)

@app.route('/')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if handle_login(username, password):
        return "Login berhasil"
    else:
        return "login gagal"
    
if __name__ == '__main__':
    app.run(debug=True)