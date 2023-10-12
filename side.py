""" 
importer sqlite3
connecter au fichier

requête
"""
import sqlite3

DATABASE = 'database.db'
SCHEMA = 'db_schema.sql'

connection = sqlite3.connect(DATABASE)
cursor = connection.cursor()

with open(SCHEMA, 'r') as f:
    schema = f.read()
connection.executescript(schema)

connection.commit

query = "INSERT INTO jobs (description, name, location, url, type) VALUES (?, ?, ?, ?, ?)"
cursor.execute(query,("Les équipes TECH CANAL+ comptent plus de 500 experts dédiés à l'innovation technologique. Ils visent à améliorer l'expérience des abonnés par le biais d'une approche agile et novatrice, tout en étendant leur influence sur les marchés internationaux.", "Développeur Front React.JS", "6 Rue Godefroy, 92800 Puteaux, France", "https://www.chooseyourboss.com/candidates/offers/developpeur-front-react-js-h-f-canal-group?utm_campaign=annonces&utm_medium=agregateur&utm_source=indeed&utm_content=prem_stage&utm_term=boost", "CDI"))
connection.commit()

query = "INSERT INTO jobs (description, name, location, url, type) VALUES (?, ?, ?, ?, ?)"
cursor.execute(query, ("Rejoignez une entreprise innovante spécialisée dans les technologies de pointe. Nous sommes à la recherche d'un ingénieur en intelligence artificielle pour rejoindre notre équipe de recherche.", "Ingénieur en Intelligence Artificielle", "Paris, France", "https://www.example.com/offers/ingenieur-en-ia?utm_source=indeed&utm_medium=agregateur", "Alternance"))
connection.commit()

query = "INSERT INTO jobs (description, name, location, url, type) VALUES (?, ?, ?, ?, ?)"
cursor.execute(query, ("Rejoignez notre start-up en pleine croissance et contribuez à développer des applications mobiles innovantes. Nous recherchons un développeur mobile passionné pour rejoindre notre équipe.", "Développeur Mobile", "Berlin, Allemagne", "https://www.example.com/offers/developpeur-mobile-berlin?utm_source=indeed&utm_medium=agregateur", "Stage"))
connection.commit()

rows = cursor.execute("SELECT * FROM jobs")
for row in rows:
    print(row)