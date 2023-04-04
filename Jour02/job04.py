import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="159753",
    database="LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("select nom, capacité from salles")
resultat = cursor.fetchall()

print(resultat)

cursor.close()
conn.close()