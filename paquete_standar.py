import pandas as pd
import requests

# consumir API(JSONPlaceholder)
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # 2 Convertir datos a DataFrame
    df = pd.DataFrame(data)

    # 3 Guardar datos en Excel
    df.to_excel('api_data.xlsx', index=False)
    print("Datos de la API guardados en 'api_data.xlsx'")
else:
    print(f"Error al consumir la API: {response.status_code}")

