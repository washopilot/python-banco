import sqlite3
import random

# Conectarse a la base de datos (o crearla si no existe)
conn = sqlite3.connect('db.sqlite')

# Crear un cursor
cursor = conn.cursor()

# Eliminar la tabla si ya existe (para limpiarla)
cursor.execute("DROP TABLE IF EXISTS usuarios")

# Crear una nueva tabla
cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER
    )
''')

# Generar y insertar 1000 registros aleatorios
for _ in range(1000):
    nombre = f'Usuario_{random.randint(1, 1000)}'
    edad = random.randint(18, 99)
    cursor.execute(
        "INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
