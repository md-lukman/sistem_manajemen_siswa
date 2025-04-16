from flask import Blueprint, redirect, url_for, render_template, request
from Backend.admin.FuncSiswa import handle_login


login_bp = Blueprint('login_bp', __name__, url_prefix = '/auth')
siswa_bp = Blueprint('siswa_bp', __name__, url_prefix='/admin')

@login_bp.route('/login', methods = ['GET'])
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