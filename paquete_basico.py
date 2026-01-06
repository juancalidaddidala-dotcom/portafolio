#Limpieza de datos
import pandas as pd


#Cargar archivo excel 
df = pd.read_excel("automatizacion y api/ventas_mal.xlsx")

# 1. Normalizar texto en columnas especificas 

df["cliente"] = df['cliente'].str.strip().str.title() #quita espacios  y pone capital inicial
df['producto'] = df['producto'].str.strip().str.upper() #quita espacios y pone todo en mayusculas

formatos = ["%Y/%m/%d", "%d-%m-%Y", "%Y-%m-%d"]
def parse_fecha(x):
    for f in formatos:
        try:
            return pd.to_datetime(x, format=f)
        except:
            continue
    return pd.NaT

df['fecha'] = df['fecha'].apply(parse_fecha)

# 3. Eliminar Duplicados
df = df.drop_duplicates()

# 4. Guardar archivo Limpio 

df.to_excel('ventas_limpio.xlsx', index=False)

print("Limpieza de datos completada. Archivo guardado como 'ventas_limpio.xlsx'")
