import sqlite3

connection = sqlite3.connect('database.db')

# Definimos la estructura de la base de datos
schema = """
DROP TABLE IF EXISTS usuarios;
DROP TABLE IF EXISTS posts;

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    contenido TEXT NOT NULL,
    autor_id INTEGER,
    FOREIGN KEY (autor_id) REFERENCES usuarios (id)
);
"""

connection.executescript(schema)
connection.close()
print("¡Base de datos creada con éxito!")
