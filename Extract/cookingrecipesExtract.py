import pandas as pd

class CookingRecipesExtractor:
    def __init__(self, csv_path: str):
        self.csv_path = csv_path
        self.data = None

    def load(self, nrows: int = None, chunksize: int = None):
        """Carga el CSV completo o una parte."""
        if chunksize:
            self.data = pd.read_csv(self.csv_path, chunksize=chunksize)
        else:
            self.data = pd.read_csv(self.csv_path, nrows=nrows)

    def head(self, n: int = 5):
        if self.data is None:
            raise ValueError("Primero ejecuta load().")
        
        if isinstance(self.data, pd.io.parsers.TextFileReader):  
            # Si es un generator (chunks)
            chunk = next(self.data)
            return chunk.head(n)
        
        return self.data.head(n)
