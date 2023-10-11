from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('index.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form.get('nombre')
    return f'Hola, {nombre}'

if __name__ == '__main__':
    app.run()

