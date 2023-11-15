class Instancia_auto:
    
    def __init__(self,kilometros,cubiertas,aceite,freno,correa,vehiculo) -> None:
        self.__kilometros=kilometros
        self.__cubiertas=cubiertas
        self.__aceite=aceite
        self.__freno=freno
        self.__correa=correa
        vehiculo=vehiculo
        
    
    def getKilometros(self):
        return (self.__kilometros)
    def setKilometros(self,kilometros):
        self.__kilometros=kilometros
    
    def getCubiertas(self):
        return (self.__cubiertas)
    def setCubiertas(self,cubiertas):
        self.__cubiertas=cubiertas
    
    def getAceite(self):
        return (self.__aceite)
    def setAceite(self,aceite):
        self.__aceite=aceite
        
    def getFreno(self):
        return (self.__freno)
    def setFreno(self,freno):
        self.__freno=freno
        
    def getCorrea(self):
        return (self.__correa)
    def setCorrea(self,correa):
        self.__correa=correa
    
    
    def __str__(self):
        return f"kilometros: {self.__kilometros},cubiertas: {self.__cubiertas},freno: {self.__freno},correa: {self.__correa},aceite: {self.__aceite}"             
            
    def nuevo_viaje(self,km):
        
        self.setAceite    (self.getAceite()+km)
        self.setCorrea    (self.getCorrea()+km)
        self.setCubiertas (self.getCubiertas()+km)
        self.setFreno     (self.getFreno()+km)
        self.setKilometros(self.getKilometros()+km)   
        
        
        
    def consultar():
        pass         