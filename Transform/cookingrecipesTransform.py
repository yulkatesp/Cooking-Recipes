import pandas as pd

class CookingRecipesTransformer:
    """
    Clase para transformar y limpiar los datos de recetas.
    """
    def __init__(self, df):
        self.df = df

    def clean(self):
        df = self.df.copy()

        # Eliminar duplicados
        df = df.drop_duplicates()

        # Eliminar filas completamente vacías
        df = df.dropna(how="all")

        # Limpiar espacios en texto
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].str.strip()

        # Rellenar valores nulos en texto con "Unknown"
        for col in df.select_dtypes(include="object").columns:
            df[col] = df[col].fillna("Unknown")

        # Rellenar valores nulos en números con 0
        for col in df.select_dtypes(include="number").columns:
            df[col] = df[col].fillna(0)

        self.df = df
        return self.df
