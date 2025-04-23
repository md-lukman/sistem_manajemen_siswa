from flask import Blueprint, render_template,session, request, redirect, url_for
from Backend.siswa.FuncProfile import tampil_profile
from Backend.siswa.FuncJadwal import tampil_jadwal
from Backend.siswa.FuncJadwal import search_jadwal

jadwalSaya_bp = Blueprint('jadwalSaya_bp', __name__, url_prefix = "/jadwal")
userSiswa_bp = Blueprint('userSiswa_bp', __name__, url_prefix = '/siswa')


@jadwalSaya_bp.route('/saya')
def jadwal_saya():
    userID = session.get('user_id')
    data = tampil_profile(userID)
    
    keyword = session.pop('search_keyword', None)
    
    if keyword:
        jadwal = search_jadwal(keyword)
        is_search = True
    else:
        jadwal = tampil_jadwal()
        is_search = False
        
    return render_template('/user/jadwalSiswa.html', profile=data, jdw = jadwal, is_search=is_search)


@jadwalSaya_bp.route('/cari', methods=["POST"])
def cari_matkul():
    if request.method == "POST":
        keyword = request.form["input"]
        session['search_keyword'] = keyword
        return redirect(url_for("jadwalSaya_bp.jadwal_saya"))