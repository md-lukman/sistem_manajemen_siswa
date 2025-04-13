from flask import Flask, render_template, request, redirect, url_for
from Backend.admin.FuncSiswa import handle_login, tambah_mahasiswa, deleteMahasiswa, tampil_mahasiswa, updateMahasiswa
import os
from Backend.routes.siswaRoutes import siswa_bp

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
                return redirect(url_for('siswa_bp.admin_dashboard'))
            else:
                return redirect(url_for('user_dashboard'))
            
        else:
            return "Login gagal"
    return render_template('login.html')
    
    
app.register_blueprint(siswa_bp)




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