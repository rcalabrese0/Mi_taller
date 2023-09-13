import datetime
from datetime import datetime

bateria=0
kilometros=0
cubiertas=0
aceite=0
frenos=0
correa=0
kilometros_contador=0
reset_aceite=""
reset_corre=""
reset_cubiertas=""
reset_freno=""

diccio_intancia_0= {
    "c_kilometros":0,  
    "c_aceite":11000,
    "c_freno":30000,
    "c_bateria":0,
    "c_cubiertas":50000,
    "c_correa":60000
    }



while True:   #WHILE DE LA VALIDACION  DE LA FECHA BATERIA
    bateria= input("Por favor, ingresa una fecha en formato aaaa/mm/dd: ")

    # Intentar convertir la cadena en una fecha
    try:
        bateria_fecha = datetime.strptime(bateria, "%Y/%m/%d")
        print("Fecha ingresada:", bateria_fecha)
        
        diccio_intancia_0["bateria"]=int("".join(filter(lambda caracter: caracter != "/", bateria)))
        diccio_intancia_0["bateria"]=diccio_intancia_0["bateria"] 
        print (diccio_intancia_0["bateria"])
        break
    except ValueError:
        print("Fecha no válida. Asegúrate de ingresarla en formato dd/mm/aaaa.")




kilometros=int(input("ingrese los km acutles?"))
cubiertas=int(input("hace cuantos km cambio las cubiertas?"))
aceite=int(input("hace cuantos km cambio las aceite?"))
freno=int(input("hace cuantos km cambio los fenos?"))
correa=int(input("hace cuantos km cambio la correa distribucion?"))

diccio_estado_actual={
    "kilometros":kilometros,
    "aceite":aceite,
    "freno":freno,
    "bateria":"",
    "cubiertas":cubiertas,
    "correa":correa
    }

 
while True:
    kilometros_contador=(input("ingrese los kilometros a recorrer: "))
    if kilometros_contador.isdigit():
        kilometros_contador=int(kilometros_contador)
    else: 
            print("ingrese solo numeros enteros")
            continue
    diccio_estado_actual["kilometros"]+=kilometros_contador
    diccio_estado_actual["aceite"]+=kilometros_contador
    diccio_estado_actual["freno"]+=kilometros_contador
    diccio_estado_actual["correa"]+=kilometros_contador
    diccio_estado_actual["cubiertas"]+=kilometros_contador
    
    # Obtener la fecha y hora actual
    fecha_hora_actual = datetime.now()

    # Formatear la fecha y hora como una cadena en el formato deseado (AAAAMMDDHHMMSS)
    fecha_hora_actual_str = fecha_hora_actual.strftime("%Y%m%d%H%M%S")
    
    diccio_estado_actual["bateria"]=(int(fecha_hora_actual_str[0:8]))
    
    print(f""" El estado actual del auto es:
    kilometros:         {diccio_estado_actual["kilometros"]}
    aceite:             {diccio_estado_actual["aceite"]}
    freno:              {diccio_estado_actual["freno"]}
    correa:             {diccio_estado_actual["correa"]}
    cubiertas:          {diccio_estado_actual["cubiertas"]}
    bateria en dias:    {diccio_estado_actual["bateria"]- diccio_intancia_0['bateria']}
    """)
    
    if (diccio_estado_actual["aceite"])>=(diccio_intancia_0["c_aceite"]):
        print(f"realice cambio de servicio correspondiete a : ACEITE")
        reset_aceite=input(print("A REALIZADO CAMBIO ACEITE ?(s/n)"))
        if reset_aceite=="s" or reset_aceite=="S":
            diccio_estado_actual["aceite"]=0
    
    if diccio_estado_actual["freno"]>=diccio_intancia_0["c_freno"]:
        print(f"realice cambio de servicio correspondiete a : FRENO")
        reset_freno=input(print("A RENOBADO LOS FRENOS ?(s/n)"))
        if reset_freno=="s" or reset_freno=="S":
            diccio_estado_actual["freno"]=0
    
    if diccio_estado_actual["correa"]>=diccio_intancia_0["c_correa"]:
        print(f"realice cambio de servicio correspondiete a : CORREA")
        reset_corre=input(print("A REALIZADO CAMBIO CORREA ?(s/n)"))
        if reset_aceite=="s" or reset_aceite=="S":
            diccio_estado_actual["correa"]=0
    
    if diccio_estado_actual["cubiertas"]>=diccio_intancia_0["c_cubiertas"]:
        print(f"realice cambio de servicio correspondiete a : CUBIERTAS")
        reset_cubiertas=input(print("A REALIZADO CAMBIO CUBIERTAS ?(S/N)"))
        if reset_cubiertas=="s" or reset_cubiertas=="S":
            diccio_estado_actual["cubiertas"]=0
    
    if ((diccio_estado_actual["bateria"])-(diccio_intancia_0["bateria"]))>730:
        print(f"debe cambiar la bateria tiene 2 años")
        reset_cubiertas=input(print("A REALIZADO CAMBIO BATERIA ?(S/N)"))
        
        if reset_cubiertas=="s" or reset_cubiertas=="S":
             
            fecha_hora_actual = datetime.now()
    
            fecha_hora_actual_str = fecha_hora_actual.strftime("%Y%m%d%H%M%S")
    
            diccio_intancia_0["bateria"]=(int(fecha_hora_actual_str[0:8]))
            
    
    if kilometros_contador==0:
        break
    
    
    

print (f"""
       los kilometros recorridos son: {diccio_estado_actual["kilometros"]} km
       la bateria tiene {diccio_estado_actual["bateria"]- diccio_intancia_0['bateria']} meses de antiguedad
       las cubiertas tienen: {diccio_estado_actual["cubiertas"]} km
       los frenos se repararon hace {diccio_estado_actual["freno"]} km
       el aceite se cabio {diccio_estado_actual["aceite"]} km atras
       la correa tiene {diccio_estado_actual["correa"]} km
       """)
