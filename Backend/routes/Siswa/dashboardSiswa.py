from flask import Blueprint, render_template, request, redirect, url_for
from Backend.siswa.FuncProfile import tampil_profile


userSiswa_bp = Blueprint('userSiswa_bp', __name__, url_prefix = '/siswa')

@userSiswa_bp.route('/index')
def siswa_dashboard():
    data = tampil_profile()
    return render_template('/user/index.html', profile=data)


@userSiswa_bp.route('/profile')
def edit_profile():
    data = tampil_profile()
    return render_template('/user/profile.html', profile=data)