import pandas as pd

class CookingRecipesTransformer:
    """
    Clase para transformar y limpiar los datos de recetas.
    """
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def clean(self) -> pd.DataFrame:
        # Hacemos una copia para no modificar el original
        df = self.df.copy()

        # 1. Eliminar duplicados
        df = df.drop_duplicates()

        # 2. Eliminar filas completamente vacías
        df = df.dropna(how="all")

        # 3. Limpiar espacios en columnas de texto (solo tipo object o string)
        text_columns = df.select_dtypes(include=["object", "string"]).columns
        for col in text_columns:
            df[col] = df[col].astype(str).str.strip()
            # ⚠️ Si quieres mantener NaN en lugar de "nan" como texto:
            df[col] = df[col].replace("nan", pd.NA)

        # 4. Rellenar valores nulos en texto con "Unknown"
        for col in text_columns:
            df[col] = df[col].fillna("Unknown")

        # 5. Rellenar valores nulos en números con 0
        numeric_columns = df.select_dtypes(include="number").columns
        for col in numeric_columns:
            df[col] = df[col].fillna(0)

        # Guardamos el resultado limpio en el objeto
        self.df = df
        return self.df
