class UndergroundSystem:

    def __init__(self):
        self.check_In = defaultdict(list)
        self.check_Out = defaultdict(list)
        self.TotalTime = defaultdict(int)
        self.NumberOfTravel = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_In[id].append(stationName)
        self.check_In[id].append(t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        self.check_Out[id].append(stationName)
        self.check_Out[id].append(t)
        k = (self.check_In[id][-2] , stationName)
        time = t - self.check_In[id][-1]
        self.TotalTime[k] += time
        self.NumberOfTravel[k] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.TotalTime[(startStation,endStation)] /  self.NumberOfTravel[(startStation,endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)