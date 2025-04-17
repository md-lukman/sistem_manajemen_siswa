import mysql.connector
from Backend.config import db_config



# read mahasiswanya
def tampil_profile():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mahasiswa")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows