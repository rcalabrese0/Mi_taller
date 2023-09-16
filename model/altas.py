from model.instancia_cero import instancia_auto
from model.usuario import persona
from model.vehiculo import vehiculo
 

auto=vehiculo()
usuario=persona()
intancia_cero=instancia_auto()

def alta_auto():
    auto.setIdvehiculo=input("ingrese id vehiculo viene de labase datos")
    auto.setAnno=input("ingrese año: " )
    auto.setColor=input("color: ")
    auto.setMarca=input("marca: ")
    auto.setModelo=input("modelo: ")
    auto.setTipo=input("tipo: ")
    auto.setPatente=input("patente: ")
    auto.setKilometro=int(input("kilometros"))
    return auto

def alta_usuario():
                
    usuario.setDni=input("Ingrese dni:  ")
    usuario.setApellido=input("Ingrese apellido: ")
    usuario.setNombre=input("Ingrese nombre: ")
    usuario.setCel=input("Ingrese celular: ")
    usuario.setCorreo=input("Ingrese correo: ")
    usuario.setIdpersona=input("Id persona_: ")
    return usuario

def alta_mantenimineto():
    intancia_cero.setAceite=int(input("ingrese los km del aceite: "))
    intancia_cero.setCorrea=int(input("los km de la correa: "))
    intancia_cero.setCubiertas=int(input("km de las cubiertas: "))
    intancia_cero.setFreno=int(input("km de los frenos: "))
    intancia_cero.setKilometros=int(input("km del vehiculo: "))
    return intancia_cero