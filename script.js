function agregarVehiculo() {
    // Obtener los valores ingresados por el usuario
    const patente = document.getElementById('patente').value;
    const marca = document.getElementById('marca').value;
    const kilometros = document.getElementById('kilometros').value;
    const modelo = document.getElementById('modelo').value;
    const ano = document.getElementById('ano').value;
    const color = document.getElementById('color').value;
    const tipo = document.getElementById('tipo').value;

    // Crear una nueva fila para la tabla
    const fila = document.createElement('tr');
    fila.innerHTML = `
        <td>${patente}</td>
        <td>${marca}</td>
        <td>${kilometros}</td>
        <td>${modelo}</td>
        <td>${ano}</td>
        <td>${color}</td>
        <td>${tipo}</td>
    `;

    // Agregar la fila a la tabla
    const tabla = document.getElementById('vehiculos');
    tabla.appendChild(fila);

    // Limpiar los campos del formulario
    document.getElementById('patente').value = '';
    document.getElementById('marca').value = '';
    document.getElementById('kilometros').value = '';
    document.getElementById('modelo').value = '';
    document.getElementById('ano').value = '';
    document.getElementById('color').value = '';
    document.getElementById('tipo').value = '';
}

function mostrarPopup() {
    const modal = document.getElementById('myModal');
    modal.style.display = 'block';
}

function cerrarPopup() {
    const modal = document.getElementById('myModal');
    modal.style.display = 'none';
}

document.getElementById('mostrarPopup').addEventListener('click', mostrarPopup);

document.querySelector('.close').addEventListener('click', cerrarPopup);

window.addEventListener('click', function (event) {
    const modal = document.getElementById('myModal');
    if (event.target === modal) {
        cerrarPopup();
    }
});
