from flask import Blueprint, render_template, request, redirect, url_for
import os
from Backend.admin.FuncMatkul import tambah_matkul, getJumlahMapel, tampil_matkul, update_matkul, delete_matkul



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
    
    
@matkul_bp.route('/update/<int:id>', methods=['POST'])
def edit(id):
    nama_mapel = request.form['namaMapel']
    deskripsi = request.form['deskripsi']
    guru_pengampu = request.form['guruPengampu']
    semester = request.form['semester']
        
    update_matkul(id, nama_mapel, deskripsi, guru_pengampu, semester)
    return redirect(url_for('siswa_bp.chart'))

@matkul_bp.route('/delete/<int:id>')
def delete(id):
    delete_matkul(id)
    data = tampil_matkul()
    return render_template('/admin/matkul.html', matkul=data)
    
