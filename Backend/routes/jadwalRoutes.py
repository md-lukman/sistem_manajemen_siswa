from flask import Blueprint, render_template, request, redirect, url_for

from Backend.admin.FuncJadwal import tambah_jadwal, update_jadwal, delete_jadwal



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
    
    
@jadwal_bp.route('/update/<int:id>', methods=['POST'])
def updateJadwal(id):
    
    hari = request.form['hari']
    jam = request.form['jam']
    id_matkul = request.form['id_matkul']
    ruangan = request.form['ruangan']
    semester = request.form['semester']
    
    update_jadwal(id, hari, jam, id_matkul, ruangan, semester)
    return redirect(url_for('siswa_bp.panels'))
    

@jadwal_bp.route('/delete/<int:id>')
def deleteJadwal(id):
    delete_jadwal(id)
    return redirect(url_for('siswa_bp.panels'))

    
   