// Función para agregar un vehículo
function agregarVehiculo() {
    const patente = document.getElementById('patente').value;
    const marca = document.getElementById('marca').value;
    const kilometros = document.getElementById('kilometros').value;
    const modelo = document.getElementById('modelo').value;
    const ano = document.getElementById('ano').value;
    const color = document.getElementById('color').value;
    const tipo = document.getElementById('tipo').value;

    const fila = document.createElement('tr');
    fila.innerHTML = `
        <td>${patente}</td>
        <td>${marca}</td>
        <td class="kilometros">${kilometros} <button class="editar-button"><i class="fas fa-edit"></i></button></td>
        <td>${modelo}</td>
        <td>${ano}</td>
        <td>${color}</td>
        <td>${tipo}</td>
        <td><button class="eliminar-button" onclick="eliminarVehiculo(this)"><i class="fas fa-trash"></i></button></td>
    `;

    const tabla = document.getElementById('vehiculos');
    tabla.appendChild(fila);

    document.getElementById('patente').value = '';
    document.getElementById('marca').value = '';
    document.getElementById('kilometros').value = '';
    document.getElementById('modelo').value = '';
    document.getElementById('ano').value = '';
    document.getElementById('color').value = '';
    document.getElementById('tipo').value = '';

    // evento de edición para el nuevo botón
    const editarButton = fila.querySelector('.editar-button');
    editarButton.addEventListener('click', () => {
        editarKilometros(fila);
    });
}

// Función para eliminar un vehículo de la lista
function eliminarVehiculo(button) {
    const fila = button.parentNode.parentNode; // Obtén la fila actual
    const tabla = document.getElementById('vehiculos');
    tabla.removeChild(fila);

    // Obtener la lista de vehículos actualizada
    const listaDeVehiculos = obtenerListaDeVehiculos();

    // Obtener la patente del vehículo a eliminar (puedes ajustar esto según tu estructura HTML)
    const patenteAEliminar = fila.querySelector('td').textContent;

    // Filtrar la lista de vehículos para excluir el vehículo eliminado
    const listaActualizada = listaDeVehiculos.filter((vehiculo) => vehiculo.patente !== patenteAEliminar);

    // Actualizar la lista de vehículos en el almacenamiento local
    guardarVehiculosEnJSON(listaActualizada);
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

window.addEventListener('click', function (event) {
    const modal = document.getElementById('myModal');
    if (event.target === modal) {
        cerrarPopup();
    }
});

document.getElementById('patente').focus();

// Función para editar los kilómetros
function editarKilometros(row) {
    const kilometersCell = row.querySelector('.kilometros'); // Obtén la celda de los kilómetros
    const currentKilometers = kilometersCell.textContent.trim(); // Obtén el valor actual

    // Crea un campo de entrada
    const inputField = document.createElement('input');
    inputField.type = 'number';
    inputField.value = currentKilometers;

    // Crea un botón de guardar
    const saveButton = document.createElement('button');
    saveButton.textContent = 'Guardar';
    saveButton.addEventListener('click', () => {
        const newKilometers = inputField.value;
        kilometersCell.textContent = newKilometers;
        // Puedes agregar lógica aquí para guardar el nuevo valor en tu base de datos o en otro lugar si es necesario.
        kilometersCell.appendChild(button); // Vuelve a agregar el botón de edición
    });

    // Remueve el botón de edición
    const button = kilometersCell.querySelector('.editar-button');
    button.remove();

    // Agrega el campo de entrada y el botón de guardar
    kilometersCell.appendChild(inputField);
    kilometersCell.appendChild(saveButton);

    inputField.focus(); // Enfoca el campo de entrada automáticamente
}
