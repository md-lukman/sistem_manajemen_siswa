from flask import Blueprint, render_template, request, redirect, url_for
from Backend.admin.FuncNilai import tambah_nilai


nilai_bp = Blueprint('nilai_bp', __name__, url_prefix = '/nilai')
siswa_bp = Blueprint('siswa_bp', __name__, url_prefix='/admin')


@nilai_bp.route('/create', methods=['GET'])
def createData():
    if request.method == 'GET':
        
        id_mahsis = request.args.get('idMahasiswa')
        id_matkul = request.args.get('idMatkul')
        nilai = request.args.get('nilai')
        semester = request.args.get('semester')
        
    
        tambah_nilai(id_mahsis, id_matkul, nilai, semester)
        return redirect(url_for('siswa_bp.element'))