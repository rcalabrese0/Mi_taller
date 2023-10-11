class instancia_auto:
    
    def __init__(self,kilometros=0,cubiertas=0,aceite=0,freno=0,correa=0) -> None:
        self.__kilometros=kilometros
        self.__cubiertas=cubiertas
        self.__aceite=aceite
        self.__freno=freno
        self.__correa=correa
        
    
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
    
    
    def alta_mantenimineto(self,aceite,correa,cubiertas,freno,kilometros):
        
        self.setAceite(aceite)
        self.setCorrea(correa)
        self.setCubiertas(cubiertas)
        self.setFreno(freno)
        self.setKilometros(kilometros)
            
    
    def suma_km(self,sum_km):
        self.setKilometros(self.getKilometros() + sum_km)
        self.setCubiertas(self.getCubiertas() + sum_km)
        self.setAceite(self.getAceite() + sum_km)
        self.setFreno(self.getFreno() + sum_km)
        self.setCorrea(self.getCorrea() + sum_km)
        

 
auto=instancia_auto()
#auto.setAceite(1)
#auto.setCorrea(1)


auto.alta_mantenimineto(1,2,3,4,5)
auto.suma_km(9)
print(auto)

 