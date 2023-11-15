import tkinter as tk

def mostrar_mensaje_alta_usuario():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    correo = entry_correo.get()
    mensaje_usuario = f"Alta exitosa:\nNombre: {nombre}\nApellido: {apellido}\nCorreo: {correo}"
    label_mensaje_usuario.config(text=mensaje_usuario)
    ventana_carga_vehiculo.deiconify()  # Muestra la ventana de carga de vehículo

def mostrar_mensaje_alta_vehiculo():
    marca = entry_marca.get()
    modelo = entry_modelo.get()
    color = entry_color.get()
    patente = entry_patente.get()
    mensaje_vehiculo = f"Vehículo cargado exitosamente:\nMarca: {marca}\nModelo: {modelo}\nColor: {color}\nPatente: {patente}"
    label_mensaje_vehiculo.config(text=mensaje_vehiculo)
    ventana_carga_informacion.deiconify()  # Muestra la ventana de carga de información adicional

def mostrar_mensaje_alta_informacion():
    correa = entry_correa.get()
    freno = entry_freno.get()
    cubiertas = entry_cubiertas.get()
    aceite = entry_aceite.get()
    kilometros = entry_kilometros.get()
    mensaje_informacion = f"Información adicional cargada exitosamente:\nCorrea: {correa}\nFreno: {freno}\nCubiertas: {cubiertas}\nAceite: {aceite}\nKilómetros: {kilometros}"
    label_mensaje_informacion.config(text=mensaje_informacion)

# Ventana principal
ventana = tk.Tk()
ventana.title("Formulario de Alta de Usuario")

# Crear etiquetas y campos de entrada para el usuario
label_nombre = tk.Label(ventana, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

label_apellido = tk.Label(ventana, text="Apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(ventana)
entry_apellido.pack()

label_correo = tk.Label(ventana, text="Correo:")
label_correo.pack()
entry_correo = tk.Entry(ventana)
entry_correo.pack()

# Botón de alta de usuario
btn_alta_usuario = tk.Button(ventana, text="Alta Usuario", command=mostrar_mensaje_alta_usuario)
btn_alta_usuario.pack()

# Etiqueta para mostrar el mensaje de alta de usuario
label_mensaje_usuario = tk.Label(ventana, text="")
label_mensaje_usuario.pack()

ventana.geometry("300x200")

# Ventana de carga de vehículo
ventana_carga_vehiculo = tk.Toplevel(ventana)
ventana_carga_vehiculo.title("Carga de Vehículo")
ventana_carga_vehiculo.withdraw()  # Oculta la ventana de carga de vehículo al inicio

# Crear etiquetas y campos de entrada para el vehículo
label_marca = tk.Label(ventana_carga_vehiculo, text="Marca:")
label_marca.pack()
entry_marca = tk.Entry(ventana_carga_vehiculo)
entry_marca.pack()

label_modelo = tk.Label(ventana_carga_vehiculo, text="Modelo:")
label_modelo.pack()
entry_modelo = tk.Entry(ventana_carga_vehiculo)
entry_modelo.pack()

label_color = tk.Label(ventana_carga_vehiculo, text="Color:")
label_color.pack()
entry_color = tk.Entry(ventana_carga_vehiculo)
entry_color.pack()

label_patente = tk.Label(ventana_carga_vehiculo, text="Patente:")
label_patente.pack()
entry_patente = tk.Entry(ventana_carga_vehiculo)
entry_patente.pack()

# Botón de carga de vehículo
btn_carga_vehiculo = tk.Button(ventana_carga_vehiculo, text="Cargar Vehículo", command=mostrar_mensaje_alta_vehiculo)
btn_carga_vehiculo.pack()

# Etiqueta para mostrar el mensaje de alta de vehículo
label_mensaje_vehiculo = tk.Label(ventana_carga_vehiculo, text="")
label_mensaje_vehiculo.pack()

# Ventana de carga de información adicional
ventana_carga_informacion = tk.Toplevel(ventana_carga_vehiculo)
ventana_carga_informacion.title("Carga de Información Adicional")
ventana_carga_informacion.withdraw()  # Oculta la ventana de carga de información al inicio

# Crear etiquetas y campos de entrada para la información adicional
label_correa = tk.Label(ventana_carga_informacion, text="Correa:")
label_correa.pack()
entry_correa = tk.Entry(ventana_carga_informacion)
entry_correa.pack()

label_freno = tk.Label(ventana_carga_informacion, text="Freno:")
label_freno.pack()
entry_freno = tk.Entry(ventana_carga_informacion)
entry_freno.pack()

label_cubiertas = tk.Label(ventana_carga_informacion, text="Cubiertas:")
label_cubiertas.pack()
entry_cubiertas = tk.Entry(ventana_carga_informacion)
entry_cubiertas.pack()

label_aceite = tk.Label(ventana_carga_informacion, text="Aceite:")
label_aceite.pack()
entry_aceite = tk.Entry(ventana_carga_informacion)
entry_aceite.pack()

label_kilometros = tk.Label(ventana_carga_informacion, text="Kilómetros:")
label_kilometros.pack()
entry_kilometros = tk.Entry(ventana_carga_informacion)
entry_kilometros.pack()

# Botón de carga de información adicional
btn_carga_informacion = tk.Button(ventana_carga_informacion, text="Cargar Información", command=mostrar_mensaje_alta_informacion)
btn_carga_informacion.pack()

# Etiqueta para mostrar el mensaje de alta de información adicional
label_mensaje_informacion = tk.Label(ventana_carga_informacion, text="")
label_mensaje_informacion.pack()

ventana.mainloop()


