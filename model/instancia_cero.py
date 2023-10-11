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
        
    
    def suma_km(self,km):
        self.setKilometros(self.getKilometros() + km)
        self.setCubiertas(self.getCubiertas() + km)
        self.setAceite(self.getAceite() + km)
        self.setFreno(self.getFreno() + km)
        self.setCorrea(self.getCorrea() + km)
        



""" from geopy.distance import geodesic

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
 """   
        

