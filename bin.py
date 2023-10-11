datos= {
    "c_kilometros":0,  
    "c_aceite":11000,
    "c_freno":30000,
    "c_bateria":0,
    "c_cubiertas":50000,
    "c_correa":60000
    }

import pickle



def imprime_datos_bin():
    # Abre el archivo en modo de lectura binaria ('rb')
    with open('datos.bin', 'rb') as archivo_bin:
        # Carga el diccionario desde el archivo binario
        datos_recuperados = pickle.load(archivo_bin)

    # Ahora puedes trabajar con el diccionario recuperado
    print(datos_recuperados)

# Diccionario con datos de ejemplo

def carga_datos_enbin():
    # Abre el archivo en modo de escritura binaria ('wb')
    with open('datos.bin', 'wb') as archivo_bin:
        # Serializa y guarda el diccionario en el archivo binario
        pickle.dump(datos, archivo_bin)



with open('datos.bin', 'rb') as archivo_bin:
        # Carga el diccionario desde el archivo binario
        datos_recuperados = pickle.load(archivo_bin)

    # Ahora puedes trabajar con el diccionario recuperado
        print(datos_recuperados)

