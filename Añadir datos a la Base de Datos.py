import sqlite3

conexion = sqlite3.connect("mi_base.db")
cursor = conexion.cursor()

while True:
    name = input("Dime el nombre:")
    edad = int(input("¿Cunatos años tienes?"))
    email = input("Dime el email (debe ser único):")
    cursor.execute(f"""
        INSERT INTO usuarios (nombre, edad, email)
        Values ("{name}", "{edad}", "{email}")
        """)
    conexion.commit()
    print(f"{name} añadiendo correctamente")    