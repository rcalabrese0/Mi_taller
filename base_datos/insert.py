import mysql.connector
import pymysql

# Establecer la conexión a la base de datos
def obtener_conexion():
    pymysql.connect(
        host="localhost",
        user="root",
        password="1234567",
        database="mytaller_db",
        cursorclass=pymysql.cursors.DictCursor
    )

# Sentencia SQL para insertar un nuevo registro en una tabla insert_query = "INSERT INTO mantenimiento_vehiculo () VALUES (%s, %s, %s,%s, %s, %s, %s)"
#INSERT INTO persona () VALUES (8, 2, "s","s"," s", "s") inser de persona dos numericos 
#INSERT INTO vehiculo () VALUES (9, "jjj333","rr","mm","1234","rojo","sedan",1234)
# Datos que deseas insertar



