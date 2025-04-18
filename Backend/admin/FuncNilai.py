import mysql.connector
from Backend.config import db_config



# create nilai baru
def tambah_nilai(id_mahsis, id_matkul, tugas, uts, uas, nilai_akhir, semester):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"INSERT INTO nilai (id_mahsis, id_matkul, tugas, uts, uas, nilai_akhir, semester) VALUES ('{id_mahsis}', '{id_matkul}','{tugas}', '{uts}', '{uas}', '{nilai_akhir}', '{semester}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
    
# read nilai
def tampil_nilai():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = """
    SELECT 
        nilai.id,
        mahasiswa.nama,
        mata_pelajaran.nama_mapel,
        nilai.tugas,
        nilai.uts,
        nilai.uas,
        nilai.nilai_akhir,
        nilai.semester,
        nilai.created_at,
        nilai.updated_at
    FROM nilai
    JOIN mahasiswa ON nilai.id_mahsis = mahasiswa.id
    JOIN mata_pelajaran ON nilai.id_matkul = mata_pelajaran.id
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# update nilai untuk update data
def update_nilai(id, id_mahsis, id_matkul, tugas, uts, uas, nilai_akhir, semester):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"""UPDATE nilai SET id_mahsis='{id_mahsis}', id_matkul='{id_matkul}', tugas='{tugas}', uts='{uts}', uas='{uas}', nilai_akhir='{nilai_akhir}', semester='{semester}', updated_at=NOW() WHERE id={id}"""
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
    
# delete mahasiswa
def delete_nilai(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"DELETE FROM nilai WHERE id='{id}'"
    cursor.execute(query)
    conn.commit()
    conn.close()

