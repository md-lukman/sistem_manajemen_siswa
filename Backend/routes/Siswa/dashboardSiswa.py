from flask import Blueprint, render_template,session, request, redirect, url_for
from Backend.siswa.FuncProfile import tampil_profile
from Backend.siswa.FuncDashboard import tampil_nilai_saya


userSiswa_bp = Blueprint('userSiswa_bp', __name__, url_prefix = '/siswa')

@userSiswa_bp.route('/index')
def siswa_dashboard():
    
    if session.get('role') != 'Mahasiswa':
        return "kamu bukan siswa!"
    user_id = session.get('user_id')
    
    data = tampil_profile(user_id)
    return render_template('/user/index.html', profile=data)


@userSiswa_bp.route('/profile')
def edit_profile():
    user_id = session.get('user_id')
    data = tampil_profile(user_id)
    return render_template('/user/profile1.html', profile=data)


@userSiswa_bp.route('/nilai')
def nilai_siswa():
    user_id = session.get('user_id')
    data = tampil_profile(user_id)
    nilai = tampil_nilai_saya(user_id)
    return render_template('/user/nilaiSiswa.html', profile=data, nilai=nilai)