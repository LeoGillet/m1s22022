import csv
import psycopg2
import psycopg2.extras
import pandas as pd

global curr, con
USERNAME = "leogillet"
PASSWORD = "lesbeteux"
try:
    conn = psycopg2.connect(host="localhost", dbname=USERNAME, user=USERNAME, password=PASSWORD)
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
except Exception as e:
    exit("Connexion impossible à la base de données: " + str(e))
print('Connecté à la base de données')

def importExcelFile(filename, sheetname, rules):
    file = pd.ExcelFile(filename)
    data = pd.read_excel(file, sheetname)
    print(file)

def importCSVFile(filename):
    """
    Importe un fichier CSV et retourne un dictionnaire sous forme {"attribut": [n_uplets], ...}
    :param filename (string): Nom du fichier à importer
    :return (dict): dictionnaire converti
    """
    data = []
    with open(filename, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(dict(row))
    return data


def createTable(filename: str, table_name: str, attributes: tuple, verbose=False):
    """
    Créé une table et y insère les valeurs pertinentes
    :param table_name (string): nom de la table
    :param data (dict): données importées du fichier
    :param attributes (tuple): attributs souhaités et type de variable à insérer dans la BDD
    """
    if type(filename) is not str:
        raise TypeError('given filename is not a string')

    if filename.endswith('.csv'):
        # Import du fichier .csv comportant les données
        data = importCSVFile(filename)
    elif filename.endswith('.xls') or filename.endswith('.xlsx'):
        # Import du fichier .xls ou .xlsx comportant les données
        data = importExcelFile(filename)
    else:
        TypeError("file is not of compatible format")

    create_command = "CREATE TABLE IF NOT EXISTS {}(".format(table_name)
    for i in range(0, len(attributes) - 1):
        create_command += "{} {}, ".format(attributes[i][0], attributes[i][1])
    create_command += "{} {});".format(attributes[len(attributes) - 1][0], attributes[len(attributes) - 1][1])
    [print(create_command) if verbose else ""]
    cur.execute(create_command)

    insert_command = "INSERT INTO {} (".format(table_name)
    for i in range(len(attributes) - 1):
        insert_command += "{}, ".format(attributes[i][0])
    insert_command += "{}) VALUES (".format(attributes[len(attributes) - 1][0])
    insert_command += "%s," * (len(attributes) - 1) + "%s) ON CONFLICT DO NOTHING;"
    [print(insert_command) if verbose else ""]
    for entry in data:
        list_entry = []
        [list_entry.append(entry[attribute[0]]) for attribute in attributes]
        [print(eval("insert_command % tuple(list_entry)")) if verbose else ""]
        cur.execute(insert_command, tuple(list_entry))


if __name__ == '__main__':
    # Nom de la table comportant les données liées aux régions
    region_name = "REGIONS"
    # Import du fichier .csv comportant les données liées aux régions
    # Attributs filtrés et types de variables souhaitées in fine
    region_attributes = (("reg", "INT PRIMARY KEY NOT NULL"),
                         ("ncc", "VARCHAR NOT NULL"),
                         ("libelle", "VARCHAR NOT NULL"))

    # Nom de la table comportant les données liées aux départements
    departement_name = "DEPARTEMENTS"
    # Attributs filtrés et types de variables souhaitées in fine
    departement_attributes = (("dep", "VARCHAR PRIMARY KEY NOT NULL"),
                              ("reg", "INT NOT NULL"),
                              ("ncc", "VARCHAR NOT NULL"),
                              ("libelle", "VARCHAR NOT NULL"))

    # Création des tables
    createTable('files/region2020.csv', region_name, region_attributes)
    createTable('files/region2020.csv', departement_name, departement_attributes)


    dimsoc_name = "DIMENSION_SOCIALE"
    dimsoc_attributes = (("dep", "VARCHAR PRIMARY KEY NOT NULL"),
                         ("annee", "INT NOT NULL CONSTRAINT annee CHECK (annee > 1900 AND annee < 9999)"),
                         ("esperance_vie", "FLOAT8 CONSTRAINT esperance_vie CHECK (esperance_vie >=0)"),
                         ("niveau_vie", "FLOAT8"),
                         ("taux_pauvrete", "FLOAT8 CONSTAINT taux_pauvrete CHECK (taux_pauvrete >= 0 AND taux_pauvrete <= 100"),
                         ("jeunes_non_inseres", "FLOAT8 CONSTAINT jeunes_non_inseres CHECK (jeunes_non_inseres >= 0 AND jeunes_non_inseres <= 100"),
                         ("soins_prox", "FLOAT8 CONSTAINT soins_prox CHECK (soins_prox >= 0 AND soins_prox <= 100"),
                         ("pop_innondation", "FLOAT8 CONSTAINT pop_innondation CHECK (pop_innondation >= 0 AND pop_innondation <= 100"))
    dimsoc_rules = {
        "header_size": 4,
        "footer_size": 5
    }
    dimsoc_data = importExcelFile("files/DD-indic-reg-dep_2008_2019.xls", "Social", dimsoc_rules)
    # Fermeture de la connexion
    cur.close()
    conn.commit()
    conn.close()
