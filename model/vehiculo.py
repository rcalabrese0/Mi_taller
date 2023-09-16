            
class vehiculo:
    def __init__(self,id_vehiculo="id_vehiculo",patente="123kkk",marca="uno",modelo="dos",anno="1234",color="nn",tipo="nn",kilometro="1234") -> None:
        self.__id_vehiculo=id_vehiculo
        self.__patente=patente
        self.__marca=marca
        self.__kilometro=kilometro
        self.__modelo=modelo
        self.__anno=anno
        self.__color=color
        self.__tipo=tipo
        
    def getIdvehiculo(self):
        return (self.__id_vehiculo)
    def setIdvehiculo(self,id_vehiculo):
        self.__id_vehiculo=id_vehiculo
    
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
        
    def __str__(self):
        return f"ID VEHICULO: {self.__id_vehiculo},PATENTE: {self.__patente},MARCA: {self.__marca},KILOMETRO: {self.__kilometro},MODELO: {self.__modelo},AÑO: {self.__anno}, COLOR: {self.__color}, TIPO: {self.__tipo}"             
