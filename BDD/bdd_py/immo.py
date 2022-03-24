# immo.py

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

def create():
	create_immeubles = "CREATE TABLE public.immeuble(nomimmeuble TEXT PRIMARY KEY NOT NULL, adresse TEXT NOT NULL, nbetages INT NOT NULL, anneeconstruction INT NOT NULL, nomgerant TEXT NOT NULL); "
	cur.execute(create_immeubles)

	popul_immeubles = "INSERT INTO immeuble (nomimmeuble, adresse, nbetages, anneeconstruction,nomgerant) VALUES (%s, %s, %s, %s, %s);"
	values = (
		("Koudalou", "3 rue Blanche", 15, 1975, "Doug"),
		("Barabas", "2 allee Nikos", 2, 1973, "Ross")
		)
	for value in values:
		cur.execute(popul_immeubles, value)

	create_appart = "CREATE TABLE public.appart(nomimmeuble TEXT NOT NULL, noapprt INT NOT NULL, superficie DECIMAL NOT NULL, etage INT NOT NULL);"
	cur.execute(create_appart)
	popul_appart = "INSERT INTO appart (nomimmeuble, noapprt, superficie, etage) VALUES (%s,%s,%s,%s);"
	values = (
		("Koudalou", 1, 150, 14),
		("Koudalou", 34, 50, 15),
		("Koudalou", 51, 200, 2),
		("Koudalou", 52, 50, 5),
		("Barabas", 1, 250, 1),
		("Barabas", 2, 250, 2)
		)
	for value in values:
		cur.execute(popul_appart, value)

	create_personne = "CREATE TABLE public.personne (nom TEXT NOT NULL, age INT NOT NULL, profession TEXT NOT NULL);"
	cur.execute(create_personne)
	popul_personne = "INSERT INTO personne (nom, age, profession) VALUES (%s,%s,%s);"
	values = (
		("Ross", 51, "Informaticien"),
		("Alice", 34, "Cadre"),
		("Rachel", 23, "Stagiaire"),
		("William", 52, "Acteur"),
		("Doug", 34, "Rentier"),
		)
	for value in values:
		cur.execute(popul_personne, value)

	create_occupant = "CREATE TABLE public.occupant (nomimmeuble TEXT NOT NULL, noappart INT NOT NULL, nomoccupant TEXT NOT NULL, anneearrivee INT NOT NULL);"
	cur.execute(create_occupant)
	popul_occupant = "INSERT INTO occupant (nomimmeuble, noappart, nomoccupant, anneearrivee) VALUES (%s,%s,%s,%s);"
	values = (
		("Koudalou", 1, "Rachel", 1992),
		("Barabas", 1, "Doug", 1994),
		("Barabas", 2, "Ross", 1994),
		("Koudalou", 51, "William", 1996),
		("Koudalou", 34, "Alice", 1993)
		)
	for value in values:
		cur.execute(popul_occupant, value)

def questions():
	print("Questions :")
	print("Appart.superficie > 100")
	appart = "SELECT * FROM appart WHERE superficie>100 ;"
	cur.execute(appart)
	rows = cur.fetchall()
	for row in rows:
		print(row)

	print("Nom occupant >< gérant")
	occupant = "SELECT O.nomoccupant,I.nomgerant FROM occupant O JOIN immeuble I ON O.nomimmeuble=I.nomimmeuble;"
	cur.execute(occupant)
	rows = cur.fetchall()
	for row in rows:
		print(row)

	print("Superficie moyenne")
	superf = "SELECT nomimmeuble, AVG(superficie) AS superf FROM appart GROUP BY nomimmeuble"
	cur.execute(superf)
	rows = cur.fetchall()
	for row in rows:
		print(row)




if __name__ == "__main__":
	questions()
	cur.close()
	conn.commit()
	conn.close()

