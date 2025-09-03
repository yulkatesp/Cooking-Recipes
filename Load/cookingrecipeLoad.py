class CookingRecipesLoader:
    """
    Clase para cargar datos limpios.
    """
    def __init__(self, df):
        self.df = df

    def to_csv(self, output_path):
        try:
            self.df.to_csv(output_path, index=False)
            print(f"💗 Datos limpios guardados en {output_path}")
        except Exception as e:
            print(f"❌ Error al guardar datos: {e}")

    def to_sqlite(self, db_path, table_name="rides"):
        try:
            db = Database(db_path)
            db.connect()
            db.create_table(table_name, self.df)
            db.insert_data(table_name, self.df)
            db.close()
        except Exception as e:
            print(f"Error al guardar en SQLite: {e}")