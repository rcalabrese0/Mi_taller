from model.altas import alta_auto,alta_mantenimineto,alta_usuario

#auto1=alta_auto()
instancia_m=alta_mantenimineto()
#usuario1=alta_usuario()

diccio_intancia_0= {
    "c_kilometros":0,  
    "c_aceite":11000,
    "c_freno":30000,
    "c_bateria":0,
    "c_cubiertas":50000,
    "c_correa":60000
    }

while True:
    kilometros_contador=(input("ingrese los kilometros a recorrer: "))
    if kilometros_contador.isdigit():
        kilometros_contador=int(kilometros_contador)
    else: 
            print("ingrese solo numeros enteros")
            continue
    cont_aceite=int((instancia_m.getAceite))
    cont_aceite=kilometros_contador + cont_aceite
    instancia_m.setAceite(cont_aceite)
    
    cont_correa=instancia_m.getCorrea+kilometros_contador
    instancia_m.setCorrea(cont_correa)
    
    cont_freno=instancia_m.getFreno+kilometros_contador
    instancia_m.setFreno(cont_freno)
    
    cont_cubiertas=instancia_m.getCubiertas+kilometros_contador
    instancia_m.setCubiertas(cont_cubiertas)
    
    cont_km=instancia_m.getKilometros+kilometros_contador
    instancia_m.setKilometros(cont_km)
        
    print(f""" El estado actual del auto es:
    kilometros:         {instancia_m.getKilometros}
    aceite:             {instancia_m.getAceite}
    freno:              {instancia_m.getFreno}
    correa:             {instancia_m.getCorrea}
    cubiertas:          {instancia_m.getCubiertas}
    FALTA LA BATERIA 
    """)
    
    if instancia_m.getAceite>=(diccio_intancia_0["c_aceite"]):
        print(f"realice cambio de servicio correspondiete a : ACEITE")
        reset_aceite=input(print("A REALIZADO CAMBIO ACEITE ?(s/n)"))
        if reset_aceite=="s" or reset_aceite=="S":
            instancia_m.setAceite=0
    
    if instancia_m.getFreno>=diccio_intancia_0["c_freno"]:
        print(f"realice cambio de servicio correspondiete a : FRENO")
        reset_freno=input(print("A RENOBADO LOS FRENOS ?(s/n)"))
        if reset_freno=="s" or reset_freno=="S":
            instancia_m.setFreno=0
    
    if instancia_m.getCorrea>=diccio_intancia_0["c_correa"]:
        print(f"realice cambio de servicio correspondiete a : CORREA")
        reset_corre=input(print("A REALIZADO CAMBIO CORREA ?(s/n)"))
        if reset_aceite=="s" or reset_aceite=="S":
            instancia_m.getCorrea=0
    
    if instancia_m.getCubiertas>=diccio_intancia_0["c_cubiertas"]:
        print(f"realice cambio de servicio correspondiete a : CUBIERTAS")
        reset_cubiertas=input(print("A REALIZADO CAMBIO CUBIERTAS ?(S/N)"))
        if reset_cubiertas=="s" or reset_cubiertas=="S":
            instancia_m.setCubiertas=0
    
    #if ((diccio_estado_actual["bateria"])-(diccio_intancia_0["bateria"]))>730:
    #    print(f"debe cambiar la bateria tiene 2 años")
    #    reset_cubiertas=input(print("A REALIZADO CAMBIO BATERIA ?(S/N)"))
        
    if kilometros_contador==0:
        break



#print(auto1)
print(instancia_m)
#print(usuario1)