import sqlite3


class Conexion():
    def __init__(self):
        try:
            self.con = sqlite3.connect('db.sqlite')
            self.crearTablas()
        except Exception as ex:
            print(ex)

    def crearTablas(self):
        sql_create_table1 = ''' CREATE TABLE IF NOT EXISTS usuarios 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, usuario TEXT UNIQUE, clave TEXT) '''
        cur = self.con.cursor()
        # cur.execute("DROP TABLE IF EXISTS usuarios")
        cur.execute(sql_create_table1)
        cur.close()
        self.crearAdmin()

    def crearAdmin(self):
        try:
            sql_insert_admin = 'INSERT INTO usuarios (nombre,usuario,clave) VALUES (?,?,?)'
            cur = self.con.cursor()
            cur.execute(sql_insert_admin,
                        ('Administrador', 'Admin', 'root1979'))
            self.con.commit()
        except Exception as ex:
            print(ex, 'Ya se creo el usuario Admin')


con = Conexion()

