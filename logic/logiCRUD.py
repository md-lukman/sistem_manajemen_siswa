import mysql.connector
from config import db_config

def handle_login(username, password):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        user = cursor.fetchone()
        cursor.close()
        conn.close()
        if user:
            return user
        else:
            return None
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return False



# create mahasiswa
def tambah_mahasiswa(nama, nim, jenisKelamin, prodi, alamat, foto):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"INSERT INTO mahasiswa (nama, nim, jenis_kelamin, prodi, alamat, foto) VALUES ('{nama}', '{nim}','{jenisKelamin}','{prodi}', '{alamat}', '{foto}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
    
#read mahasiswanya
def tampil_mahasiswa():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mahasiswa")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows  

#update mahasiswa
def update_mahasiswa(nim, nama=None, alamat=None, jenis_kelamin=None, foto_path=None):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "UPDATE mahasiswa SET"
    if nama:
        query += f"nama='{nama}',"
    if alamat:
        query += f"alamat='{alamat}',"
    if jenis_kelamin:
        query += f"jenis_kelamin='{jenis_kelamin}',"
    if foto_path:
        query += f"foto='{foto_path}',"
    query = query.rstrip(',') + f"WHERE nim='{nim}'"
    cursor.execute(query)
    conn.commit()
    conn.close





