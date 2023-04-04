import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="159753",
    database="LaPlateforme"
)

cursor = conn.cursor()

cursor.execute("select SUM(capacité) as salles_totale from salles")
resultat = cursor.fetchone()


print("La capacité de toutes les salles est de:", resultat[0])
cursor.close()
conn.close()