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

query = "INSERT INTO jobs (description, name, url) VALUES (?, ?, ?)"
cursor.execute(query, ("", "Discord"))
connection.commit()

rows = cursor.execute("SELECT * FROM passwords")
for row in rows:
    print(row)