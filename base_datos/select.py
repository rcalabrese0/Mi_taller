from insert import obtener_conexion

def hola():
    return 'Hola'

def get_a():
    conexion = obtener_conexion()
    try:
        cursor = conexion.cursor()
        # Ejecutar una consulta SELECT
        consulta = "SELECT * FROM Vehiculo"
        cursor.execute(consulta)

        #   Obtener los resultados
        resultados = cursor.fetchall()

        # Cerrar el cursor
        cursor.close()
    
        return resultados
    except:
        print("Error")
    finally:
        conexion.close()
