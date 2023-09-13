bateria=0
kilometros=0
cubiertas=0
aceite=0
frenos=0
correa=0
kilometros_contador=0

diccio_intancia_0= {
    "c_kilometros":0,  
    "c_aceite":11000,
    "c_freno":30000,
    "c_bateria":24 ,
    "c_cubiertas":50000,
    "c_correa":60000
    }

kilometros=int(input("ingrese los km acutles?"))
bateria=int(input("hace cuantos meses compro la bateria?"))
cubiertas=int(input("hace cuantos km cambio las cubiertas?"))
aceite=int(input("hace cuantos km cambio las aceite?"))
freno=int(input("hace cuantos km cambio los fenos?"))
correa=int(input("hace cuantos km cambio la correa distribucion?"))

diccio_estado_actual={
    "kilometros":kilometros,
    "aceite":aceite,
    "freno":freno,
    "bateria":bateria,
    "cubiertas":cubiertas,
    "correa":correa
    }

 
while True:
    kilometros_contador=int(input("ingrese los kilometros a recorrer: "))
    diccio_estado_actual["kilometros"]+=kilometros_contador
    diccio_estado_actual["aceite"]+=kilometros_contador
    diccio_estado_actual["freno"]+=kilometros_contador
    diccio_estado_actual["correa"]+=kilometros_contador
    diccio_estado_actual["cubiertas"]+=kilometros_contador
    
    print(f"""
    {diccio_estado_actual["kilometros"]}
    {diccio_estado_actual["aceite"]}
    {diccio_estado_actual["freno"]}
    {diccio_estado_actual["correa"]}
    {diccio_estado_actual["cubiertas"]}
    """)
    
    if (diccio_estado_actual["aceite"])>=(diccio_intancia_0["c_aceite"]):
        print(f"realice cambio de servicio correspondiete a : ACEITE")
    if diccio_estado_actual["freno"]>=diccio_intancia_0["c_freno"]:
        print(f"realice cambio de servicio correspondiete a : FRENO")
    if diccio_estado_actual["correa"]>=diccio_intancia_0["c_correa"]:
        print(f"realice cambio de servicio correspondiete a : CORREA")
    if diccio_estado_actual["cubiertas"]>=diccio_intancia_0["c_cubiertas"]:
        print(f"realice cambio de servicio correspondiete a : CUBIERTAS")
    if kilometros_contador==1:
        break
    
    
    

print (f"""
       los kilometros recorridos son: {kilometros} km
       la bateria tiene {bateria} meses de antiguedad
       las cubiertas tienen: {cubiertas} km
       los frenos se repararon hace {freno} km
       el aceite se cabio {aceite} km atras
       la correa tiene {correa} km
       """)
