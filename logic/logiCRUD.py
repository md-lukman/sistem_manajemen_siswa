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



# create
def tambah_mahasiswa(nama, nim, jenisKelamin, prodi, alamat, foto):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"INSERT INTO mahasiswa (nama, nim, jenis_kelamin, prodi, alamat, foto) VALUES ('{nama}', '{nim}','{jenisKelamin}','{prodi}', '{alamat}', '{foto}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()




