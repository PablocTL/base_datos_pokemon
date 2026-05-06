import sqlite3

conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()


cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        edad INTEGER,
        email TEXT UNIQUE
    )
""")
conexion.commit()

cursor.execute("""
    INSERT INTO usuarios (nombre, edad, email)
    VALUES ('Pablo', 25, 'pablo@uax.com')
""")
conexion.commit()