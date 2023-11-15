
from model.instancia_cero import Instancia_auto
from model.usuario import Persona
from model.vehiculo import Vehiculo
import pickle

print("registrese como usuario!")
nombre=input("ingrese su nobre: ")
appellido=input("ingrese su apellidio: ")   #instancia del usuario
dni=input("ingresse su dni: ")
usuario1=Persona(dni,nombre,appellido)



print("registrese su vehiculo!")
id_vehiculo=input("ingrese id: ")
patente=input("ingrese la patente: ")
marca=input("ingrese marca: ")          #INSTACIA DE VEHICULO
kilometro=int(input("ingrese los kilometros :"))
modelo=input("ingrese modelo: ")
anno=input("ingrese año: ")
color=input("ingrese el colo: ")
tipo=input("ingrese su tipo: ")
auto1=Vehiculo(id_vehiculo,patente,marca,modelo,anno,color,tipo,kilometro,usuario1)

print("registre el estado inicial de su vehiculo!")
cubiertas=int(input("ingrese los km recorridos de cubiertas: "))
aceite=int(input("ingrese los km recorridos de aceite: ")) #INTACIA DE MATENIMIENTO
freno=int(input("ingrese los km recorridos de los frenos: "))
correa=int(input("ingrese los km recorridos de la transmicion: "))
mante1=Instancia_auto(kilometro,cubiertas,aceite,freno,correa,auto1)



with open('datos.bin', 'rb') as archivo_bin:
        # Carga el diccionario desde el archivo binario
        diccio_intancia_0 = pickle.load(archivo_bin)

""" 
diccio_intancia_0= {
    "c_kilometros":0,  
    "c_aceite":11000,
    "c_freno":30000,           #SE RECUPERA DEL ARCHIVO BINARIO
    "c_bateria":0,
    "c_cubiertas":50000,
    "c_correa":60000
    } """


while True:
    print(
    """ELEJA LA OPCION DESEADA
    0-Exit
    1-Viajar
    2-Consultar
    """
    )
    op=input("operacion: ")
    
    if op =="1":
        kilometros_contador=(input("ingrese los kilometros a recorrer: "))
        if kilometros_contador.isdigit():
            kilometros_contador=int(kilometros_contador)
        else: 
                print("ingrese solo numeros enteros")
                continue
            
            
        mante1.nuevo_viaje(kilometros_contador)

        print(f""" El estado actual del auto {auto1.getMarca()} {auto1.getModelo()} es:
        kilometros:         {mante1.getKilometros()}
        aceite:             {mante1.getAceite()}/{diccio_intancia_0["c_aceite"]}
        freno:              {mante1.getFreno()}/{diccio_intancia_0["c_freno"]}
        correa:             {mante1.getCorrea()}/{diccio_intancia_0["c_correa"]}
        cubiertas:          {mante1.getCubiertas()}/{diccio_intancia_0["c_cubiertas"]}

        del titular {usuario1.getApellido()} {usuario1.getNombre()}""")

        if mante1.getAceite()>=(diccio_intancia_0["c_aceite"]):
            print(f"realice cambio de servicio correspondiete a : ACEITE")
            reset_aceite=input("A REALIZADO CAMBIO ACEITE ?(s/n)")
            if reset_aceite=="s" or reset_aceite=="S":
                mante1.setAceite(0)

        if mante1.getFreno()>=diccio_intancia_0["c_freno"]:
            print(f"realice cambio de servicio correspondiete a : FRENO")
            reset_freno=input("A RENOBADO LOS FRENOS ?(s/n)")
            if reset_freno=="s" or reset_freno=="S":
                mante1.setFreno(0)

        if mante1.getCorrea()>=diccio_intancia_0["c_correa"]:
            print(f"realice cambio de servicio correspondiete a : CORREA")
            reset_corre=input("A REALIZADO CAMBIO CORREA ?(s/n)")
            if reset_aceite=="s" or reset_aceite=="S":
                mante1.setCorrea(0)

        if mante1.getCubiertas()>=diccio_intancia_0["c_cubiertas"]:
            print(f"realice cambio de servicio correspondiete a : CUBIERTAS")
            reset_cubiertas=input("A REALIZADO CAMBIO CUBIERTAS ?(S/N)")
            if reset_cubiertas=="s" or reset_cubiertas=="S":
                mante1.setCubiertas(0)


        if kilometros_contador==0:
            break 
    
    if op=="2":
        while True:
            print(
                """ BIENBENIDO AL MENU CONSULTAS DE:
                1-KM DE LA CORREA DISTRIBUCION
                2-KM DE LAS CUBIERTAS
                3-KM DEL ACEITE
                4-KM DEL FRENO
                5-TODO
                6-Exit
                """
            )    
            opCons=input("elija la operacion: ")
            if opCons=="1":
                print(f""" El estado actual del auto {auto1.getMarca()} {auto1.getModelo()} es:
                correa:{mante1.getCorrea()}/{diccio_intancia_0["c_correa"]}
                """)
            if opCons=="2":
                print(f""" El estado actual del auto {auto1.getMarca()} {auto1.getModelo()} es:
                cubiertas:{mante1.getCubiertas()}/{diccio_intancia_0["c_cubiertas"]}
                """)
            if opCons=="3":
                print(f""" El estado actual del auto {auto1.getMarca()} {auto1.getModelo()} es:
                aceite:{mante1.getAceite()}/{diccio_intancia_0["c_aceite"]}
                """)
            if opCons=="4":
                print(f""" El estado actual del auto {auto1.getMarca()} {auto1.getModelo()} es:
                freno:{mante1.getFreno()}/{diccio_intancia_0["c_freno"]}
                """)
            if opCons=="5":
                print(f""" El estado actual del auto {auto1.getMarca()} {auto1.getModelo()} es:
                kilometros:         {mante1.getKilometros()}
                aceite:             {mante1.getAceite()}/{diccio_intancia_0["c_aceite"]}
                freno:              {mante1.getFreno()}/{diccio_intancia_0["c_freno"]}
                correa:             {mante1.getCorrea()}/{diccio_intancia_0["c_correa"]}
                cubiertas:          {mante1.getCubiertas()}/{diccio_intancia_0["c_cubiertas"]}
                """)
            if opCons=="6":
                break
    if op=="0":
        break