class Config:
    """
    Configuración de rutas y parámetros del ETL de recetas.
    """
    # Ruta al dataset descargado con KaggleHub
    INPUT_PATH = "/home/codespace/.cache/kagglehub/datasets/paultimothymooney/recipenlg/versions/1/RecipeNLG_dataset.csv"
    
    # Ruta donde guardar dataset limpio
    OUTPUT_PATH = "/workspaces/COOKING-RECIPES/Extract/Files/recipenlg_clean.csv"
