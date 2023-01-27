class Person:
    def __init__(self, id, checkInStation="", checkInTime=0, checkOutStation="", checkOutTime=0):
        self.id = id
        self.checkInStation, self.checkInTime = checkInStation, checkInTime
        self.checkOutStation, self.checkOutTime = checkOutStation, checkOutTime
        
    def setCheckOut(self,checkOutStation="", checkOutTime=0):
        self.checkOutStation, self.checkOutTime = checkOutStation, checkOutTime

    def getTravelTime(self):
        return self.checkOutTime - self.checkInTime
    
    def getSations(self):
        return(self.checkInStation, self.checkOutStation)
        
class UndergroundSystem:

    def __init__(self):
        self.personHash = {}
        self.stationTimes = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.personHash[id] = Person(id,stationName, t)        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        p = self.personHash[id]
        p.setCheckOut(stationName, t)
        stations = p.getSations()
        time = p.getTravelTime()
        
        if stations in self.stationTimes:
            totalTime , trips = self.stationTimes[stations]
            self.stationTimes[stations] = (totalTime + time, trips + 1)
        else:
            self.stationTimes[stations] = (time, 1)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime , trips = self.stationTimes[(startStation, endStation)]
        return totalTime / trips

        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)