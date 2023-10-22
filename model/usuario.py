
class persona():
    def __init__(self,dni="dni_persona",nombre="nombre",apellido="apellido",correo="corro@corre.com",cel="1223444",id_persona="1") -> None:
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__correo=correo
        self.__cel=cel
        self.__id_persona=id_persona
    
    
    
    def getDni(self):
            return (self.__dni)
    def setDni(self,dni):
            self.__dni=dni
    
    def getNombre(self):
        return (self.__nombre)
    def setNombre(self,nombre):
        self.__nombre=nombre
    
    def getApellido(self):
        return (self.__apellido)
    def setApellido(self,apellido):
        self.__apellido=apellido
    
    def getCorreo(self):
        return (self.__correo)
    def setCorreo(self,correo):
        self.__correo=correo
    
    def getCel(self):
        return (self.__cel)
    def setCel(self,cel):
        self.__cel=cel
    
    def getIdpersona(self):
        return (self.__id_persona)
    def setIdpersona(self,id_persona):
        self.__id_persona=id_persona
    
    
    def __str__(self):
        return f"DNI: {self.__dni},NOMBRE: {self.__nombre},APELLIDO: {self.__apellido},CORREO: {self.__correo},CELUALAR: {self.__cel},NUMERO ID: {self.__id_persona}"             
       
    def alta_usuario():
                
        setDni=input("Ingrese dni:  ")
        setApellido=input("Ingrese apellido: ")
        setNombre=input("Ingrese nombre: ")
        setCel=input("Ingrese celular: ")
        setCorreo=input("Ingrese correo: ")
        setIdpersona=input("Id persona_: ")
        