class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.total = defaultdict(lambda: defaultdict(list))

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id]=(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, intial_time = self.checkin[id]
        self.total[startStation][stationName].append(t - intial_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_times = self.total[startStation][endStation]
        average = sum(total_times) / len(total_times) 
        return average
    
# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)