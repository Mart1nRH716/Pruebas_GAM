import pyodbc
import pandas as pd
# ============= CONEXIÓN A BASE DE DATOS =============
# Configuración con PyODBC
server = 'MTO02438WSAGC01'
username = 'sa'
password = 'Im550123'
driver = 'ODBC Driver 11 for SQL Server'


'''
Función para obtener los datos de cualquier tabla de sql SERVER
'''
def obtener_datos(database, nombre_tabla ):
	# Configuración de conexión a la base de datos
	connection_string = (
		f'DRIVER={driver};'
		f'SERVER={server};'
		f'DATABASE={database};'
		f'UID={username};'
		f'PWD={password}'
	)
	# Conectar a la base de datos y ejecutar la consulta
	conn = pyodbc.connect(connection_string)
	cursor = conn.cursor()
	query = f'SELECT * FROM {nombre_tabla}'
	cursor.execute(query)
	data = cursor.fetchall()
	data = pd.DataFrame.from_records(data, columns=[column[0] for column in cursor.description])

	return data

df = obtener_datos('Prueba', 'Grades')
print(df)