from geopy.distance import geodesic
class DistanceTracker:
    def __init__(self):
        self.last_position = None  
        self.total_distance = 0.0
        
    def update_distance(self, new_position):
        if self.last_position is not None:
            distance = geodesic(self.last_position, new_position).kilometers
            self.total_distance += distance
            print(f"Distancia Recorida: {distance:.2f} km")
            print(f"Total Recorrido: {self.total_distance:.2f} km")
        self.last_position = new_position

class persona():
    def __init__(self,dni,nombre,apellido,correo,cel,id_perosna) -> None:
        self.__dni=dni
        self.__nombre=nombre
        self.__apellido=apellido
        self.__correo=correo
        self.__cel=cel
        self.__id_persona=id_perosna
    
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
        self.__apelldio=apellido
    
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
    
        
    
        
        
class vendedor(persona):
    def __init__ (self,dni,nombre,apellido,correo,cel,id_persona):
        super().__init__(self,dni,nombre,apellido,correo,cel,id_persona)
class comprador(persona):
    def __init__(self,dni,nombre,apellido,correo,cel,id_persona):
        super().__init__(dni,nombre,apellido,correo,cel,id_persona)
            
            
class veiculo:
    def __init__(self,id_veiculo,patente,marca,modelo,anno,color,tipo,kilometro) -> None:
        self.__id_veiculo=id_veiculo
        self.__patente=patente
        self.__marca=marca
        self.__kilometro=kilometro
        self.__modelo=modelo
        self.__anno=anno
        self.__color=color
        self.__tipo=tipo
        
    def getIdveiculo(self):
        return (self.__id_veiculo)
    def setIdveiculo(self,id_veiculo):
        self.__id_veiculo=id_veiculo
    
    def getPatente(self):
        return (self.__patente)
    def setPatente(self,patente):
        self.__patente=patente
        
    def getMarca(self):
        return (self.__marca)
    def setMarca(self,marca):
        self.__marca=marca
    
    def getModelo(self):
        return (self.__modelo)
    def setModelo(self,modelo):
        self.__modelo=modelo
    
    def getAnno(self):
        return (self.__anno)
    def setAnno(self,anno):
        self.__anno=anno
    
    def getColor(self):
        return (self.__color)
    def setColor(self,color):
        self.__color=color
        
    def getTipo(self):
        return (self.__tipo)
    def setTipo(self,tipo):
        self.__tipo=tipo
    
    def getKilometro(self):
        return (self.__kilometro)
    def setKilometro(self,kilomeotro):
        self.__kilometro=kilomeotro
    
    def contarKilometro(kilometro,kilometroRecoridos):
        while kilometroRecoridos>0 :
            kilomotrosAlarmar=kilomotrosAlarmar+kilometroRecoridos
            