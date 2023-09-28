from model.vehiculo import vehiculo
from model.usuario import persona
from model.instancia_cero import instancia_auto
from bin import datos

#usuario1=persona.alta_usuario()
#auto1=vehiculo.alta_auto()
mante1=instancia_auto()
mante1.alta_mantenimineto()

while True:
    kilometros_contador=(input("ingrese los kilometros a recorrer: "))
    if kilometros_contador.isdigit():
        kilometros_contador=int(kilometros_contador)
    else: 
            print("ingrese solo numeros enteros")
            continue
    
    
    mante1.suma_km(kilometros_contador)
    
    print(f""" El estado actual del auto es:
    kilometros:         {mante1.getKilometros()}
    aceite:             {mante1.getAceite()}
    freno:              {mante1.getFreno()}
    correa:             {mante1.getCorrea()}
    cubiertas:          {mante1.getCubiertas()}
    FALTA LA BATERIA 
    """)
    
    if mante1.getAceite()>=(datos["c_aceite"]):
        print(f"realice cambio de servicio correspondiete a : ACEITE")
        reset_aceite=input(print("A REALIZADO CAMBIO ACEITE ?(s/n)"))
        if reset_aceite=="s" or reset_aceite=="S":
            mante1.setAceite(0)
    
    if mante1.getFreno()>=datos["c_freno"]:
        print(f"realice cambio de servicio correspondiete a : FRENO")
        reset_freno=input(print("A RENOBADO LOS FRENOS ?(s/n)"))
        if reset_freno=="s" or reset_freno=="S":
            mante1.setFreno(0)
    
    if mante1.getCorrea()>=datos["c_correa"]:
        print(f"realice cambio de servicio correspondiete a : CORREA")
        reset_corre=input(print("A REALIZADO CAMBIO CORREA ?(s/n)"))
        if reset_aceite=="s" or reset_aceite=="S":
            mante1.setCorrea(0)
    
    if mante1.getCubiertas()>=datos["c_cubiertas"]:
        print(f"realice cambio de servicio correspondiete a : CUBIERTAS")
        reset_cubiertas=input(print("A REALIZADO CAMBIO CUBIERTAS ?(S/N)"))
        if reset_cubiertas=="s" or reset_cubiertas=="S":
            mante1.setCubiertas(0)
    
    #if ((diccio_estado_actual["bateria"])-(diccio_intancia_0["bateria"]))>730:
    #    print(f"debe cambiar la bateria tiene 2 años")
    #    reset_cubiertas=input(print("A REALIZADO CAMBIO BATERIA ?(S/N)"))
        
    
    if kilometros_contador==0:
        break



#print(auto1)
#print(mante1)
#print(usuario1)