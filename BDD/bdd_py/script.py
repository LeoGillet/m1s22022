import psycopg2 # Python SQL driver for PostgreSQL
import psycopg2.extras

# Try to connect to an existing database
print('Connexion à la base de données...')
USERNAME="leogillet"
PASSWORD="lesbeteux" # `a remplacer par le mot de passe d"acc`es aux bases
try:
	conn = psycopg2.connect(host="localhost", dbname=USERNAME,user=USERNAME,password=PASSWORD)
except Exception as e :
	exit("Connexion impossible à la base de données: " + str(e))
print('Connecté à la base de données')
#pr ́eparation de l"ex ́ecution des requ^etes (`a ne faire qu"une fois)
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

cur.execute("CREATE TABLE public.person(id INT PRIMARY KEY NOT NULL, name TEXT NOT NULL, address TEXT NOT NULL); ")
print("Table person créée")

command = "INSERT INTO person (id, name, address) VALUES (%s,%s,%s)"
values = (123, "Martin", "Bordeaux")
values_2 = (124, "Bernard", "Talence")
print("Exécution sur la base de données de la commande d'insertion avec les valeurs", "values")

try:
# Lancement de la requ^ete.
	cur.execute(command, values)
	cur.execute(command, values_2)
except Exception as e :
# en cas d"erreur, fermeture de la connexion
	cur.close()
	conn.close()
	exit("error when running: " + command + " : " + str(e))

# Nombre de lignes inser ́ees
count = cur.rowcount
print (count, "enregistrement(s) inséré(s) avec succès dans la table person.")

command = "SELECT * FROM person"
print("Exécution sur la base de données de la requête: ", command)
try:
# Lancement de la requ^ete.
	cur.execute(command)
except Exception as e :
#fermeture de la connexion
	cur.close()
	conn.close()
	exit("error when running: " + command + " : " + str(e))

# R ́ecup ́eration du r ́esultat de la requ^ete:
# rows => liste des lignes s ́electionn ́ees dans la table person
rows = cur.fetchall()

if(not rows):
	print("No result found")
# pour chaque ligne r du dictionnaire, affiche les donn ́ees associ ́ees aux diff ́erentes cl ́es:
for r in rows:
	print("Id = ", r["id"], )
	print("Name = ", r["name"])
	print("Address = ", r["address"], "\n")

command = "SELECT * FROM person WHERE name = %s"
# Les param`etres de la requ^ete sont `a saisir dans une liste
name=["Martin"]
cur.execute(command,name)
print("Sélection de la ligne \"Martin\" dans la table person")
p = cur.fetchone() #il n"y a qu"un seul r ́esultat
print(p["name"], "habite", p["address"])

cur.close()
conn.commit()
conn.close()
print("La connexion PostgreSQL est fermée")