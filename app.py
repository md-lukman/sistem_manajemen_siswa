from flask import Flask, render_template, request, redirect, url_for
from Backend.admin.FuncSiswa import handle_login
import os
from Backend.routes.siswaRoutes import siswa_bp
from Backend.routes.matkulRoutes import matkul_bp
from Backend.routes.nilaiRoutes import nilai_bp
from Backend.routes.jadwalRoutes import jadwal_bp

app = Flask(__name__)

@app.route('/')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
        user = handle_login(username, password)
        if user:
            if user['role'] == 'admin':
                return redirect(url_for('siswa_bp.admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
            
        else:
            return "Login gagal"
    return render_template('login.html')
    
    
app.register_blueprint(siswa_bp)
app.register_blueprint(matkul_bp)
app.register_blueprint(nilai_bp)
app.register_blueprint(jadwal_bp)





if __name__ == '__main__':
    app.run(debug=True)