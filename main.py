import kagglehub
from Extract import cookingrecipesExtract

# Descargar dataset de Kaggle
dataset_path = kagglehub.dataset_download("paultimothymooney/recipenlg")

# Ruta al archivo CSV dentro del dataset descargado
csv_path = "/home/codespace/.cache/kagglehub/datasets/paultimothymooney/recipenlg/versions/1/RecipeNLG_dataset.csv"

# Crear objeto
extractor = cookingrecipesExtract.CookingRecipesExtractor(csv_path)

# Cargar solo 5000 filas para pruebas
extractor.load(nrows=5000)

print(extractor.head(5))




