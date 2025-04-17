import mysql.connector
from Backend.config import db_config



# read mahasiswanya
def tampil_profile(user_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM mahasiswa WHERE id = '{user_id}' AND role = 'mahasiswa'")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows
