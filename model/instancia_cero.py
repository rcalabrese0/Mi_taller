class instancia_auto:
    
    def __init__(self,kilometros="000000",cubiertas="00000",aceite="000",freno="000",correa="0000") -> None:
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
        

