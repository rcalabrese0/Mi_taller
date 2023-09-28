import mysql.connector

# Establecer la conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234567",
    database="mytaller_db"
        )



 
# Crear un cursor para interactuar con la base de datos
cursor = conexion.cursor()

# Sentencia SQL para la consulta
consulta_query = "SELECT * FROM mantenimiento_vehiculo"

# Ejecutar la consulta
cursor.execute(consulta_query)

# Obtener todos los resultados de la consulta
resultados = cursor.fetchall()

# Imprimir los resultados
for fila in resultados:
    print(fila)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
