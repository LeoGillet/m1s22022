import psycopg2 # Python SQL driver for PostgreSQL
import psycopg2.extras
import sys

print('Connexion à la base de données...')
USERNAME="leogillet"
PASSWORD="lesbeteux"

try:
	conn = psycopg2.connect(host="localhost", dbname=USERNAME,user=USERNAME,password=PASSWORD)
except Exception as e :
	exit("Connexion impossible à la base de données: " + str(e))
print('Connecté à la base de données')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


def search(query):
	command = "SELECT Dragon,Sexe FROM Dragons"
	try:
		cur.execute(command)
	except Exception as e :
		cur.close()
		conn.close()
		print(e)
	rows = cur.fetchall()
	for row in rows:
		if row["dragon"] == query:
			sexe = "un mâle" if row["sexe"] == "M" else "une femelle"
			print("Le dragon", query, "est", sexe)


def run():
	command = "SELECT Dragon,Ecailles,EnAmour FROM Dragons"

	try:
		cur.execute(command)
	except Exception as e :
		cur.close()
		conn.close()
		print(e)

	rows = cur.fetchall()
	for row in rows:
		print("Dragon", row["dragon"], "- Ecailles", row["ecailles"], "- Comportement", row["enamour"])



if __name__ == "__main__":
	if len(sys.argv) == 1:
		run()
	elif len(sys.argv) == 2:
		search(sys.argv[1])
	cur.close()
	conn.commit()
	conn.close()


