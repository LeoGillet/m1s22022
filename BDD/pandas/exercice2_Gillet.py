import pandas as pd
import psycopg2
import psycopg2.extras
import numpy

global df_parc, df_bus, cur, conn
df_parc = pd.read_csv('files/ec_parc_s.csv', sep=';')
df_bus = pd.read_csv('files/sv_arret_p.csv', sep=';')

USERNAME="leogillet"
PASSWORD="lesbeteux"
try:
	conn = psycopg2.connect(host="localhost", dbname=USERNAME,user=USERNAME,password=PASSWORD)
except Exception as e :
	exit("Connexion impossible à la base de données: " + str(e))
print('Connecté à la base de données')
cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

def affichage_1():
	print("#### ec_parc_s ####")
	print("Colonnes : ", end='')
	for column in list(df_parc.columns):
		print(column, end=' ')
	print('\nNombre de lignes : ', end='')
	print(len(df_parc.index))
	print("10 premières lignes")
	print(df_parc.head(10), "\n\n")

	print("#### sv_arret_p ####")
	print("Colonnes : ", end='')
	for column in list(df_bus.columns):
		print(column, end=' ')
	print('\nNombre de lignes : ', end='')
	print(len(df_bus.index))
	print("10 premières lignes")
	print(df_bus.head(10), "\n\n")


def create_db_2():
	############## START ##############
	create_parc = "CREATE TABLE IF NOT EXISTS public.parcs(ident INT PRIMARY KEY NOT NULL, insee INT NOT NULL, nom TEXT NOT NULL, descript TEXT, milieu TEXT, paysage TEXT, service TEXT);"
	cur.execute(create_parc)

	cur.execute("SELECT * FROM public.parcs")
	if not bool(cur.rowcount): #If table is empty
		popul_parc = "INSERT INTO public.parcs (ident, insee, nom, descript, milieu, paysage, service) VALUES (%s,%s,%s,%s,%s,%s,%s)"
		for index in range(len(df_parc.index)):
			row = list(df_parc.iloc[index])
			for index, value in enumerate(row):
				if type(value) is numpy.int64:
					row[index] = int(value)
			try:
				cur.execute(popul_parc, row)
			except Exception as e:
				cur.close()
				conn.close()
				exit("Erreur survenue lors de l'insertion dans la table parcs\n{}".format(e))

	create_bus = "CREATE TABLE IF NOT EXISTS public.arretsbus(ident VARCHAR(12) PRIMARY KEY NOT NULL, libelle TEXT NOT NULL, vehicule TEXT NOT NULL CONSTRAINT vehicule CHECK (vehicule = 'BUS' OR vehicule = 'TRAM' OR vehicule = 'BATEAU'), voirie TEXT NOT NULL, insee VARCHAR NOT NULL);"
	cur.execute(create_bus)

	cur.execute("SELECT * FROM public.arretsbus")
	if not bool(cur.rowcount): #If table is empty
		popul_bus = "INSERT INTO public.arretsbus (ident, libelle, vehicule, voirie, insee) VALUES (%s,%s,%s,%s,%s)"
		for index in range(len(df_bus.index)):
			row = list(df_bus.iloc[index])
			for index, value in enumerate(row):
				if type(value) is numpy.int64:
					row[index] = int(value)
			try:
				cur.execute(popul_bus, row)
			except Exception as e:
				cur.close()
				conn.close()
				exit("Erreur survenue lors de l'insertion dans la table bus\n{}".format(e))

def query_db_3():
	query = ""
	select_a = "SELECT P.nom, P.milieu, P.service FROM arretsbus A JOIN parcs P ON P.nom LIKE A.libelle WHERE (P.service='HANDICAPES_PARTIEL' OR P.service='HANDICAPES_TOTAL');"
	try:
		cur.execute(select_a)
	except Exception as e :
		cur.close()
		conn.close()
		print(e)
	parc_handic = cur.fetchall()
	for row in parc_handic:
		print(row[0])
		print("Milieu :",row[1])
		print("Services :", row[2])
		print("----------")

	print("Environnements connus : 'BERGES FLEUVES', 'COTEAUX', 'EAU BOURDE', 'FORET_OUEST', 'JALLES', 'PRESQUILE', 'VILLE', 'BOIS', 'ZONE HUMIDE', 'COURS EAU', 'PLAN EAU', 'MARAIS', 'PAYSAGE'")
	env = input("Environnement (milieu/paysage) : ")
	env = env.upper()
	berges = ("BERGES_FLEUVES", "BERGE_FLEUVE", "BERGE_FLEUVES", "BERGES_FLEUVE", "BERGE FLEUVE", "BERGES FLEUVES", "BERGES FLEUVES", "BERGE FLEUVES")
	coteaux = ("COTEAUX", "COTEAU", "CÔTEAU", "CÔTEAUX")
	eau = ("EAU_BOURDE", "EAU BOURDE", "EAUX_BOURDES", "EAUX BOURDES")
	foret = ("FORET_OUEST", "FORET OUEST", "FORÊT OUEST", "FORÊT_OUEST", "FORETS_OUEST", "FORÊTS_OUEST", "FORETS OUEST", "FORÊTS OUEST")
	jalles = ("JALLES", "JALLE")
	presquile = ("PRESQUILE", "PRESQU'ILE", "PRESQUÎLE", "PRESQU'ÎLE", "PRESQUILES", "PRESQU'ILES", "PRESQUÎLES", "PRESQU'ÎLES")
	ville = ("VILLE", "VILLES")
	zhumide = ("ZONE_HUMIDE", "ZONE HUMIDE", "ZONES HUMIDES", "ZONES_HUMIDES")
	cours_eau = ("COURS_EAU", "COURS EAU")
	plan_eau = ("PLAN_EAU", "PLAN EAU", "PLANS_EAU", "PLANS EAU")
	prairie = ("PRAIRIE", "PRAIRIES")
	paysage = ("PAYSAGE", "PAYSAGES")

	homoglyphs = [berges, coteaux, eau, foret, jalles, presquile, ville, zhumide, cours_eau, plan_eau, prairie, paysage]
	for homog in homoglyphs:
		for case in homog:
			if env in case:
				env = homog[0]
				break

	show_command = "SELECT nom,milieu,paysage FROM parcs WHERE (paysage LIKE '%{}%' OR milieu LIKE '%{}%');".format(env, env)
	cur.execute(show_command)
	results = cur.fetchall()
	print('\n')
	for row in results:
		print(row[0])
		print("Milieu :",row[1])
		print("Paysage :", row[2])
		print("----------")

	writer = pd.ExcelWriter('parcs_handic.xlsx', engine='xlsxwriter')
	df = pd.DataFrame.from_records(parc_handic)
	df.to_excel(writer, sheet_name='Sheet1')
	writer.save()


if __name__ == '__main__':
	# affichage_1()
	# create_db_2()
	query_db_3()

	cur.close()
	conn.commit()
	conn.close()
	print("Terminé")

