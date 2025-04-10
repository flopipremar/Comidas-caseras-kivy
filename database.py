import sqlite3

class BaseDatos:
    def __init__(self, db_name="comida.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def crear_base_de_datos(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            direccion TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ventas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente TEXT NOT NULL,
            producto TEXT NOT NULL,
            cantidad INTEGER NOT NULL)''')

        self.conn.commit()

    def obtener_clientes(self):
        self.cursor.execute("SELECT * FROM clientes")
        return self.cursor.fetchall()

    def obtener_productos(self):
        self.cursor.execute("SELECT * FROM productos")
        return self.cursor.fetchall()

    def guardar_cliente(self, cliente):
        self.cursor.execute("INSERT INTO clientes (nombre, telefono, direccion) VALUES (?, ?, ?)",
                            (cliente['nombre'], cliente['telefono'], cliente['direccion']))
        self.conn.commit()

    def guardar_producto(self, producto):
        self.cursor.execute("INSERT INTO productos (nombre, precio) VALUES (?, ?)",
                            (producto['nombre'], producto['precio']))
        self.conn.commit()

    def insertar_venta(self, cliente, producto, cantidad):
        self.cursor.execute("INSERT INTO ventas (cliente, producto, cantidad) VALUES (?, ?, ?)",
                            (cliente, producto, cantidad))
        self.conn.commit()

    def cerrar(self):
        self.conn.close()