import os
import pandas as pd

class CookingRecipesExtractor:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.data = None

    def load(self, nrows: int = None, chunksize: int = None):
        if chunksize:
            self.data = pd.read_csv(self.csv_path, chunksize=chunksize)
        else:
            self.data = pd.read_csv(self.csv_path, nrows=nrows)

    def head(self, n: int = 5):
        if self.data is None:
            raise ValueError("Primero ejecuta load().")
        
        if isinstance(self.data, pd.io.parsers.TextFileReader):
            chunk = next(self.data)
            return chunk.head(n)
        
        return self.data.head(n)

    def save(self, filename: str, directory: str = "Extract/Files"):
        """Guarda los datos en un CSV dentro de un directorio seguro."""
        if self.data is None:
            raise ValueError("Primero carga los datos con load().")

        os.makedirs(directory, exist_ok=True)  # Asegura que el directorio exista

        if isinstance(self.data, pd.io.parsers.TextFileReader):
            # Si se cargó en chunks, solo guardamos el primero
            chunk = next(self.data)
            chunk.to_csv(os.path.join(directory, filename), index=False)
        else:
            self.data.to_csv(os.path.join(directory, filename), index=False)
