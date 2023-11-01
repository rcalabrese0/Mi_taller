from flask import Flask, request, render_template, redirect, url_for
import pymysql

app = Flask(__name__)

 # Configura la conexión a la base de datos MySQL
db = pymysql.connect(
    host="localhost",
    user="root",
    password="1234567",
    database="mytaller_db",
    cursorclass=pymysql.cursors.DictCursor
)


@app.route('/')
def formulario():
    return render_template('index.html')

def insertar_auto(patente, marca, modelo, color):
    try:
        cursor = db.cursor()
        sql = "INSERT INTO vehiculo (patente, marca, modelo, color) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (patente, marca, modelo, color))
        db.commit()
        cursor.close()
        return True
    except Exception as e:
        db.rollback()
        return str(e)


@app.route('/procesar', methods=['POST'])
def procesar():
    patente = request.form['patente']
    marca = request.form['marca']
    modelo = request.form['modelo']
    color = request.form['color']

    resultado = insertar_auto(patente, marca, modelo, color)

    if resultado == True:
        mensaje = "Registro insertado con éxito"
    else:
        mensaje = f"Error al insertar registro: {resultado}"

    return render_template('addauto.html', f_mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
