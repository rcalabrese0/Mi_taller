import tkinter as tk

def mostrar_ventana_alta_usuario():
    ventana_alta_usuario.deiconify()

def mostrar_ventana_alta_vehiculo():
    ventana_alta_vehiculo.deiconify()

def mostrar_ventana_alta_informacion():
    ventana_alta_informacion.deiconify()

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Menú Principal")

# Crear un menú
menu = tk.Menu(ventana_principal)
ventana_principal.config(menu=menu)

# Crear un submenú "Alta"
submenu_alta = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Alta", menu=submenu_alta)
submenu_alta.add_command(label="Usuario", command=mostrar_ventana_alta_usuario)
submenu_alta.add_command(label="Vehículo", command=mostrar_ventana_alta_vehiculo)
submenu_alta.add_command(label="Información Adicional", command=mostrar_ventana_alta_informacion)
submenu_alta.add_separator()
submenu_alta.add_command(label="Salir", command=ventana_principal.quit)

# Ventana de alta de usuario
ventana_alta_usuario = tk.Toplevel(ventana_principal)
ventana_alta_usuario.title("Alta de Usuario")
ventana_alta_usuario.withdraw()

# Ventana de alta de vehículo
ventana_alta_vehiculo = tk.Toplevel(ventana_principal)
ventana_alta_vehiculo.title("Alta de Vehículo")
ventana_alta_vehiculo.withdraw()

# Ventana de alta de información adicional
ventana_alta_informacion = tk.Toplevel(ventana_principal)
ventana_alta_informacion.title("Alta de Información Adicional")
ventana_alta_informacion.withdraw()

ventana_principal.mainloop()
