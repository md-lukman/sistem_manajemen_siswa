import mysql.connector
from Backend.config import db_config



# create nilai baru
def tambah_jadwal(hari, jam, matkul, ruangan, semester):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"INSERT INTO jadwal_pelajaran (hari, jam, id_matkul, ruangan, semester) VALUES ('{hari}', '{jam}','{matkul}', '{ruangan}', '{semester}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
    
# read jadwal
def tampil_jadwal():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jadwal_pelajaran")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


# read jadwal kondisi tertentu
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


# update jadwal untuk update data
def update_jadwal(id, hari, jam, id_matkul, ruangan, semester):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"""UPDATE jadwal_pelajaran SET hari='{hari}', jam='{jam}', id_matkul='{id_matkul}', ruangan='{ruangan}', semester='{semester}' WHERE id={id}"""
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()
    
    
# delete jadwal
def delete_jadwal(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"DELETE FROM jadwal_pelajaran WHERE id='{id}'"
    cursor.execute(query)
    conn.commit()
    conn.close()