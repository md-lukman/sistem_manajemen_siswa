from flask import Blueprint, render_template, request, redirect, url_for


userSiswa_bp = Blueprint('userSiswa_bp', __name__, url_prefix = '/siswa')

@userSiswa_bp.route('/index')
def siswa_dashboard():
    return render_template('/user/index.html')