from flask import Blueprint, render_template,session, request, redirect, url_for
from Backend.siswa.FuncProfile import tampil_profile
from Backend.siswa.FuncJadwal import tampil_jadwal

jadwalSaya_bp = Blueprint('jadwalSaya_bp', __name__, url_prefix = "/jadwal")
userSiswa_bp = Blueprint('userSiswa_bp', __name__, url_prefix = '/siswa')


@jadwalSaya_bp.route('/saya')
def jadwal_saya():
    userID = session.get('user_id')
    jadwal = tampil_jadwal()
    data = tampil_profile(userID)
    return render_template('/user/jadwalSiswa.html', profile=data, jdw = jadwal)

