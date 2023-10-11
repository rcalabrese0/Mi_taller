
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    patente = request.form['patente']
    marca=request.form['marca']
    modelo=request.form['modelo']
    color=request.form['color']
    return render_template('formulario.html', f_patente=patente,f_marca=marca,f_modelo=modelo,f_color=color)

if __name__ == '__main__':
    app.run(debug=True)
