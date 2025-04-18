from flask import Flask, render_template
import os
from Backend.routes.siswaRoutes import siswa_bp
from Backend.routes.matkulRoutes import matkul_bp
from Backend.routes.nilaiRoutes import nilai_bp
from Backend.routes.jadwalRoutes import jadwal_bp
from Backend.routes.logout.logout import logout_bp
from Backend.routes.login.login import login_bp
from Backend.routes.Siswa.dashboardSiswa import userSiswa_bp
from Backend.routes.Siswa.profileRoutes import profile_bp
from Backend.routes.Siswa.jadwalRoute import jadwalSaya_bp


app = Flask(__name__)
app.secret_key = 'tes'


@app.route('/')
def login_form():
    return render_template('login.html')

app.register_blueprint(siswa_bp)
app.register_blueprint(matkul_bp)
app.register_blueprint(nilai_bp)
app.register_blueprint(jadwal_bp)
app.register_blueprint(logout_bp)
app.register_blueprint(login_bp)
app.register_blueprint(userSiswa_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(jadwalSaya_bp)


if __name__ == '__main__':
    app.run(debug=True)