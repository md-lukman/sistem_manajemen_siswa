import mysql.connector
from Backend.config import db_config



# read nilai
def tampil_nilai_saya(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"""
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
    WHERE nilai.id_mahsis = '{id}'
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows