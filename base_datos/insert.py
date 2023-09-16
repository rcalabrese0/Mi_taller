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

# Sentencia SQL para insertar un nuevo registro en una tabla
insert_query = "INSERT INTO mantenimiento_vehiculo () VALUES (%s, %s, %s,%s, %s, %s, %s)"

# Datos que deseas insertar
datos_a_insertar = (7,1,2,3,4,5,6)

# Ejecutar la sentencia SQL con los datos proporcionados
cursor.execute(insert_query, datos_a_insertar)

# Confirmar la inserción
conexion.commit()

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
