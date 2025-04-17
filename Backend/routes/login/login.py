from flask import Blueprint,session, redirect, url_for, render_template, request
from Backend.admin.FuncSiswa import handle_login


login_bp = Blueprint('login_bp', __name__, url_prefix = '/auth')
siswa_bp = Blueprint('siswa_bp', __name__, url_prefix='/admin')
userSiswa_bp = Blueprint('userSiswa_bp', __name__, url_prefix = '/siswa')

@login_bp.route('/login', methods = ['GET'])
def login():
    if request.method == 'GET':
        nama = request.args.get('nama')
        nim = request.args.get('nim')
        
        user = handle_login(nama, nim)
        
        if user:
            session['user_id'] = user['id']
            session['nama'] = user['nama']
            session['role'] = user.get('role', 'Mahasiswa')
            
            if session['role'] == 'Admin':
                return redirect(url_for('siswa_bp.admin_dashboard'))
            else:
                return redirect(url_for('userSiswa_bp.siswa_dashboard'))
            
        else:
            return "Login gagal"
    return render_template('login.html')