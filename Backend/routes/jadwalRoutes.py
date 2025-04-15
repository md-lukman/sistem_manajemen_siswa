from flask import Blueprint, render_template, request, redirect, url_for

from Backend.admin.FuncJadwal import tambah_jadwal



jadwal_bp = Blueprint('jadwal_bp', __name__, url_prefix = '/jadwal')
siswa_bp = Blueprint('siswa_bp', __name__, url_prefix='/admin')


@jadwal_bp.route('/create', methods=['GET'])
def createData():
    if request.method == 'GET':
        
        hari = request.args.get('hari')
        jam = request.args.get('jam')
        matkul = request.args.get('id_matkul')
        ruangan = request.args.get('ruangan')
        semester = request.args.get('semester')
        
        tambah_jadwal(hari, jam, matkul, ruangan, semester)
       
        return redirect(url_for('siswa_bp.panels'))
