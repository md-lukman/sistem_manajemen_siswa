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
    
    

    