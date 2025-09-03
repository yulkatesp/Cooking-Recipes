import sqlite3

class Database:
    """
    Clase para manejar la conexión y operaciones con SQLite.
    """
    def __init__(self, db_path):
        self.db_path = db_path

    def connect(self):
        """Establece la conexión a la base de datos SQLite."""
        try:
            conn = sqlite3.connect(self.db_path)
            return conn
        except Exception as e:
            print(f"❌ Error al conectar a SQLite: {e}")
            return None

    def save_dataframe(self, df, table_name="recetas"):
        """Guarda un DataFrame en la base de datos SQLite."""
        try:
            conn = self.connect()
            if conn is not None:
                df.to_sql(table_name, conn, if_exists="replace", index=False)
                conn.close()
                print(f"✅ Datos guardados en la tabla '{table_name}' de {self.db_path}")
        except Exception as e:
            print(f"❌ Error al guardar en SQLite: {e}")
