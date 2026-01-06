import pandas as pd
import requests

# 1. Endpoint de la API de SpaceX
url = "https://api.spacexdata.com/v4/launches/latest"

# 2. Consumir API
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    
    # 3. Extraer datos relevantes
    lanzamiento = {
        "Nombre Misión": data.get("name"),
        "Fecha": data.get("date_utc"),
        "Éxito": data.get("success"),
        "Detalles": data.get("details"),
        "ID Rocket": data.get("rocket"),
        "ID Launchpad": data.get("launchpad")
    }
    
    # 4. Convertir a DataFrame y guardar en Excel
    df = pd.DataFrame([lanzamiento])
    df.to_excel("spacex_lanzamiento.xlsx", index=False)
    
    print("Datos del último lanzamiento guardados en 'spacex_lanzamiento.xlsx'")
else:
    print("Error al conectar con la API:", response.status_code)