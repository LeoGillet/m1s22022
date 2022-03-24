# chevaliers.py

import psycopg2 # Python SQL driver for PostgreSQL
import psycopg2.extras

print('Connexion à la base de données...')
USERNAME="leogillet"
PASSWORD="lesbeteux"

try:
	conn = psycopg2.connect(host="localhost", dbname=USERNAME,user=USERNAME,password=PASSWORD)
except Exception as e :
	exit("Connexion impossible à la base de données: " + str(e))
print('Connecté à la base de données')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

create_command = 'CREATE TABLE public.chevaliers(matricule INT PRIMARY KEY NOT NULL, nom TEXT NOT NULL, parente TEXT NOT NULL, rang TEXT NOT NULL, etat TEXT NOT NULL); '
cur.execute(create_command)

command = "INSERT INTO chevaliers(matricule, nom, parente, rang, etat) VALUES (%s,%s,%s,%s,%s)"
values = (1, 'Martin', 'Bernard','comte','blesse')
values_2 = (2, 'Bernard', 'Arthur','roi','mort')
values_3 = (3, 'Roman', 'Bernard','chevalier2','croisade')
print("Exécution sur la base de données de la commande d'insertion avec les valeurs", "values")

try:
# Lancement de la requ^ete.
	cur.execute(command, values)
	cur.execute(command, values_2)
	cur.execute(command, values_3)
except Exception as e :
# en cas d"erreur, fermeture de la connexion
	cur.close()
	conn.close()
	exit("error when running: " + command + " : " + str(e))

command_query = "SELECT C1.nom FROM chevaliers C1 JOIN chevaliers C2 ON C1.parente=C2.nom WHERE C2.rang = 'roi'"
cur.execute(command_query)
rows = cur.fetchall()
for row in rows:
	print(row)

cur.close()
conn.commit()
conn.close()