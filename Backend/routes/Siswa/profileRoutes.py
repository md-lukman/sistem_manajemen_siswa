from flask import Blueprint, render_template, request, redirect, url_for
import os
from Backend.routes.siswaRoutes import updateMahasiswa

profile_bp = Blueprint('profile_bp', __name__, url_prefix = '/profile')
userSiswa_bp = Blueprint('userSiswa_bp', __name__, url_prefix = '/siswa')


@profile_bp.route('/update/<int:id>', methods=['POST'])
def update_profile(id):
    nama = request.form['nama']
    nim = request.form['nim']
    jk = request.form['jk']
    prodi = request.form['prodi']
    alamat = request.form['alamat']
    foto = request.files.get('foto')
    
    UPLOAD_FOLDER = os.path.join('static', 'uploads')
    if foto and foto.filename != '':
        foto_path = os.path.join(UPLOAD_FOLDER, foto.filename)
        foto.save(foto_path)
        foto_nama = foto.filename
    else:
        foto_nama = None

    updateMahasiswa(id, nama, nim, jk, prodi, alamat, foto_nama)
    
    return redirect(url_for('userSiswa_bp.edit_profile'))

