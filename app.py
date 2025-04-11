from flask import Flask, render_template, request, redirect, url_for
from logic.auth import handle_login

app = Flask(__name__)

@app.route('/')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = handle_login(username, password)
        if user:
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
            
        else:
            return "Login gagal"
    return render_template(login.html)
    
    
@app.route('/admin/index')
def admin_dashboard():
    return render_template('/admin/index.html')
    

@app.route('/admin/siswa')
def widget():
    return render_template('/admin/siswa.html')


@app.route('/admin/matkul')
def charts():
    return render_template('/admin/matkul.html')

@app.route('/admin/nilai')
def elements():
    return render_template('/admin/Nilai.html')

@app.route('/admin/jadwal')
def panels():
    return render_template('/admin/jadwal.html')
    
    
if __name__ == '__main__':
    app.run(debug=True)