import kagglehub
from Config.Configuraciones import Config
from Extract.cookingrecipesExtract import CookingRecipesExtractor
from Transform.cookingrecipesTransform import CookingRecipesTransformer
from Load.cookingrecipeLoad import CookingRecipesLoader

def main():
    # Descargar dataset desde Kaggle
    dataset_path = kagglehub.dataset_download("paultimothymooney/recipenlg")

    print(f"📂 Dataset descargado en: {dataset_path}")

    # 1. Extract
    extractor = CookingRecipesExtractor(Config.INPUT_PATH)
    extractor.load(nrows=5000)  # Cargamos solo 5000 filas para pruebas
    df = extractor.data
    print("💗 Datos extraídos")
    print(extractor.head(10))

    # 2. Transform
    transformer = CookingRecipesTransformer(df)
    df_clean = transformer.clean()
    print("💗 Datos transformados (limpios)")

    # 3. Load
    loader = CookingRecipesLoader(df_clean)
    loader.to_csv(Config.OUTPUT_PATH)

    print("💗 Proceso ETL completado")

if __name__ == "__main__":
    main()





