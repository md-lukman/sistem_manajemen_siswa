from flask import Blueprint, render_template, request, redirect, url_for
import os
from Backend.admin.FuncMatkul import tambah_matkul, getJumlahMapel, tampil_matkul
from Backend.routes.siswaRoutes import chart


matkul_bp = Blueprint('matkul_bp', __name__, url_prefix='/matkul')
siswa_bp = Blueprint('siswa_bp', __name__, url_prefix='/admin')




@matkul_bp.route('/create', methods=['GET'])
def createData():
    if request.method == 'GET':
        total_mapel = getJumlahMapel()
        
        kode_mapel = f"MATKUL{total_mapel + 1:03}"
        nama_mapel = request.args.get('namaMapel')
        deskripsi = request.args.get('deskripsi')
        guru_pengampu = request.args.get('guruPengampu')
        semester = request.args.get('semester')
        
    
        tambah_matkul(kode_mapel, nama_mapel, deskripsi, guru_pengampu, semester)
        return redirect(url_for('siswa_bp.chart'))
    
