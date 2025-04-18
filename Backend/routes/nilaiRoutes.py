from flask import Blueprint, render_template, request, redirect, url_for
from Backend.admin.FuncNilai import tambah_nilai, update_nilai, tampil_nilai, delete_nilai


nilai_bp = Blueprint('nilai_bp', __name__, url_prefix = '/nilai')
siswa_bp = Blueprint('siswa_bp', __name__, url_prefix='/admin')


@nilai_bp.route('/create', methods=['GET'])
def createData():
    if request.method == 'GET':
        
        id_mahsis = request.args.get('idMahasiswa')
        id_matkul = request.args.get('idMatkul')
        tugas = request.args.get('tugas')
        uts = request.args.get('uts')
        uas = request.args.get('uas')
        nilai_akhir = request.args.get('nilai_akhir')
        semester = request.args.get('semester')
        
    
        tambah_nilai(id_mahsis, id_matkul, tugas, uts, uas, nilai_akhir, semester)
        return redirect(url_for('siswa_bp.element'))
    
    
@nilai_bp.route('/update/<int:id>', methods=['POST'])
def edit(id):

    id_mahsis = request.form.get('idMahasiswa')
    id_matkul = request.form.get('idMatkul')
    tugas = request.form.get('tugas')
    uts = request.form.get('uts')
    uas = request.form.get('uas')
    nilai_akhir = request.form.get('nilai_akhir')
    semester = request.form.get('semester')
        
    
    update_nilai(id, id_mahsis, id_matkul, tugas, uts, uas, nilai_akhir, semester)
    return redirect(url_for('siswa_bp.element'))


@nilai_bp.route('/delete/<int:id>')
def delete(id):
    delete_nilai(id)
    nilai = tampil_nilai()
    return render_template('/admin/Nilai.html', nilai=nilai)