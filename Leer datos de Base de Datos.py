import sqlite3

conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

cursor.execute("SELECT nombre, edad FROM usuarios WHERE edad > 20")
cursor.execute("SELECT *FROM usuarios Where nombre LIKE '%a%'")

resultados = cursor.fetchall()
for fila  in resultados:
    print(fila)