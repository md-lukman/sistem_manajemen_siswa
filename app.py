from flask import Flask, render_template, request, redirect, url_for
from logic.FuncSiswa import handle_login, tambah_mahasiswa, deleteMahasiswa, tampil_mahasiswa, updateMahasiswa
import os

app = Flask(__name__)

@app.route('/')
def login_form():
    return render_template('login.html')

@app.route('/login', methods=['GET'])
def login():
    if request.method == 'GET':
        username = request.args.get('username')
        password = request.args.get('password')
        user = handle_login(username, password)
        if user:
            if user['role'] == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
            
        else:
            return "Login gagal"
    return render_template('login.html')
    
    
@app.route('/admin/index')
def admin_dashboard():
    return render_template('/admin/index.html')
    

@app.route('/admin/siswa')
def widget():
    data = tampil_mahasiswa()
    return render_template('/admin/siswa.html', mahasiswa=data)

@app.route('/admin/matkul')
def charts():
    return render_template('/admin/matkul.html')

@app.route('/admin/nilai')
def elements():
    return render_template('/admin/Nilai.html')

@app.route('/admin/jadwal')
def panels():
    return render_template('/admin/jadwal.html')

@app.route('/create', methods=['POST'])
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
    
        tambah_mahasiswa(nama, nim, jenisKelamin, prodi, alamat, foto_nama
                         )
        return redirect(url_for('siswa'))

@app.route('/siswa')
def siswa():
    data = tampil_mahasiswa()
    return render_template('/admin/siswa.html', mahasiswa=data)


@app.route('/update/<int:id>', methods=['POST'])
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
    return redirect(url_for('siswa'))
    
@app.route('/delete/<int:id>')
def delete(id):
    deleteMahasiswa(id)
    data = tampil_mahasiswa()
    return render_template('/admin/siswa.html', mahasiswa=data)






if __name__ == '__main__':
    app.run(debug=True)