import mysql.connector
from Backend.config import db_config


def handle_login(nama, nim):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = f"SELECT * FROM mahasiswa WHERE nama = '{nama}' AND nim = '{nim}'"
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
def tambah_mahasiswa(nama, nim, jenisKelamin, prodi, alamat, foto, role):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"INSERT INTO mahasiswa (nama, nim, jenis_kelamin, prodi, alamat, foto, role) VALUES ('{nama}', '{nim}','{jenisKelamin}','{prodi}', '{alamat}', '{foto}', '{role}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()


# read mahasiswanya
def tampil_mahasiswa():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mahasiswa")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


# update mahasiswa untuk update data
def updateMahasiswa(id, nama, nim, jk, prodi, alamat, foto, role):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    if foto:
        query = f"""UPDATE mahasiswa SET nama='{nama}', nim='{nim}', jenis_kelamin='{jk}', prodi='{prodi}', alamat='{alamat}', foto='{foto}', role='{role}', updated_at=NOW() WHERE id={id}"""
    else:
        query = f"""UPDATE mahasiswa SET nama='{nama}', nim='{nim}',jenis_kelamin='{jk}', prodi='{prodi}', alamat='{alamat}', role='{role}', updated_at=NOW() WHERE id={id}"""

    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
# delete mahasiswa
def deleteMahasiswa(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"DELETE FROM mahasiswa WHERE id='{id}'"
    cursor.execute(query)
    conn.commit()
    conn.close()