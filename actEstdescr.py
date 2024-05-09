import pandas as pd

# Cargar el archivo CSV
df = pd.read_csv('housing.csv')

# Mostrar las primeras filas para verificar la carga correcta de los datos
print(df.head())

# Verificar la cantidad de datos y las variables
print("Cantidad de datos:", df.shape[0])
print("Variables:", df.shape[1])

# Identificar el tipo de variables
print(df.dtypes)

# Obtener estadísticas descriptivas
print(df.describe())
