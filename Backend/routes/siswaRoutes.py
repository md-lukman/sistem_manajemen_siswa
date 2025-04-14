from flask import Blueprint, render_template, request, redirect, url_for
import os
from Backend.admin.FuncSiswa import tampil_mahasiswa, tambah_mahasiswa, updateMahasiswa, deleteMahasiswa


siswa_bp = Blueprint('siswa_bp', __name__, url_prefix='/admin')



@siswa_bp.route('/index')
def admin_dashboard():
    return render_template('/admin/index.html')

@siswa_bp.route('/siswa')
def widget():
    data = tampil_mahasiswa()
    return render_template('/admin/siswa.html', mahasiswa=data)

@siswa_bp.route('/matkul')
def chart():
    return render_template('/admin/matkul.html')

@siswa_bp.route('/nilai')
def element():
    return render_template('/admin/Nilai.html')

@siswa_bp.route('/jadwal')
def panels():
    return render_template('/admin/jadwal.html')

@siswa_bp.route('/create', methods=['POST'])
def createData():
    if request.method == 'POST':
        nama = request.form.get('nama')
        nim = request.form.get('nim')
        jenisKelamin = request.form.get('jkelamin')
        prodi = request.form.get('prodi')
        alamat = request.form.get('alamat')
        foto = request.files.get('foto')
        
        UPLOAD_FOLDER = os.path.join('static', 'uploads')
        if foto and foto.filename != '':
            foto_path = os.path.join(UPLOAD_FOLDER, foto.filename)
            foto.save(foto_path)
            foto_nama = foto.filename
        else:
            foto_nama = None
    
        tambah_mahasiswa(nama, nim, jenisKelamin, prodi, alamat, foto_nama)
        return redirect(url_for('siswa_bp.siswa'))
    

@siswa_bp.route('/siswa')
def siswa():
    data = tampil_mahasiswa()
    return render_template('/admin/siswa.html', mahasiswa=data)

@siswa_bp.route('/update/<int:id>', methods=['POST'])
def edit(id):
    nama = request.form['nama']
    nim = request.form['nim']
    jk = request.form['jkelamin']
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
    return redirect(url_for('siswa_bp.siswa'))


@siswa_bp.route('/delete/<int:id>')
def delete(id):
    deleteMahasiswa(id)
    data = tampil_mahasiswa()
    return render_template('/admin/siswa.html', mahasiswa=data)






