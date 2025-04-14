import mysql.connector
from Backend.config import db_config



# create nilai baru
def tambah_nilai(id_mahsis, id_matkul, nilai, semester):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = f"INSERT INTO nilai (id_mahsis, id_matkul, nilai, semester) VALUES ('{id_mahsis}', '{id_matkul}','{nilai}', '{semester}')"
    cursor.execute(query)
    conn.commit()
    cursor.close()
    conn.close()