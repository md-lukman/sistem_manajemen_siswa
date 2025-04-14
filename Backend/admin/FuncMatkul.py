import mysql.connector
from Backend.config import db_config




#menghitung jumlah matkul yang ada
def getJumlahMapel():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM mata_pelajaran")
    jumlah = cursor.fetchone()[0]
    conn.close()
    return jumlah
    

# create matkul baru
def tambah_matkul(kode_mapel, nama_mapel, deskripsi, guru_pengampu, semester):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"INSERT INTO mata_pelajaran (kode_mapel, nama_mapel, deskripsi, guru_pengampu, semester) VALUES ('{kode_mapel}', '{nama_mapel}','{deskripsi}','{guru_pengampu}', '{semester}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
    
# read matkul
def tampil_matkul():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mata_pelajaran")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows