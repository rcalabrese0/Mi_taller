from flask import Flask
import pymysql

app = Flask(__name__)

# Configura la conexión a la base de datos MySQL
db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234567",
    database="mytaller_db",
    cursorclass=pymysql.cursors.DictCursor # Esto convierte los resultados en diccionarios
)

@app.route('/') #RUTA A LA AGINA PRINCIPAL 
def consulta_select():
    try:
        # Crear un cursor para interactuar con la base de datos
        cursor = db.cursor()

        # Ejecutar una consulta SELECT EN LA TABLA REQUERIDA
        #consulta = "SELECT * FROM persona"
        consulta = "SELECT * FROM vehiculo"
        cursor.execute(consulta)

        # Obtener los resultados
        resultados = cursor.fetchall()

        # Cerrar el cursor
        cursor.close()

        # Procesar los resultados
        # Por ejemplo, convertirlos en una cadena para mostrar en la respuesta HTTP
        #print(resultados) muestra por consola
        #resultado_str ="\n".join([f"ID: {row['dni']}, Nombre: {row['nombre']}" for row in resultados])
        resultado_str ="\n".join([f"ID: {row['idvehiculo']}, año: {row['anno']}, patente: {row['patente']}, marca: {row['marca']}, modelo: {row['modelo']}" for row in resultados])
        return resultados
    except Exception as e:
        return f"Error en la consulta: {str(e)}"
    finally:
        # Cerrar la conexión a la base de datos
        db.close()

if __name__ == '__main__':
    app.run()