import mysql.connector
from Backend.config import db_config


#tampil jadwal matkul mahasoiswa
def tampil_jadwal():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = """
    SELECT 
        jadwal_pelajaran.id,
        jadwal_pelajaran.hari,
        jadwal_pelajaran.jam,
        mata_pelajaran.nama_mapel,
        jadwal_pelajaran.ruangan,
        jadwal_pelajaran.semester
    FROM jadwal_pelajaran
    JOIN mata_pelajaran ON jadwal_pelajaran.id_matkul = mata_pelajaran.id
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

#tampil data berdasarkan keyword tertentu
def search_jadwal(keyword):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"""
    SELECT
        jadwal_pelajaran.id,
        jadwal_pelajaran.hari,
        jadwal_pelajaran.jam,
        mata_pelajaran.nama_mapel,
        jadwal_pelajaran.ruangan,
        jadwal_pelajaran.semester
    FROM jadwal_pelajaran
    JOIN mata_pelajaran ON jadwal_pelajaran.id_matkul = mata_pelajaran.id
    WHERE mata_pelajaran.nama_mapel LIKE '%{keyword}%'
    """
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
