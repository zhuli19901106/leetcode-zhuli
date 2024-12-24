# medium
# https://leetcode.com/problems/design-underground-system/
# 1AC, without exception
class UndergroundSystem:
    def __init__(self):
        self.mt = {}
        self.mi = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        mi = self.mi
        mi[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        mi = self.mi
        mt = self.mt
        name1, t1 = mi[id]
        if not (name1, stationName) in mt:
            mt[(name1, stationName)] = []
        mt[(name1, stationName)].append(t - t1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        mt = self.mt
        if (startStation, endStation) in mt:
            a = mt[(startStation, endStation)]
            return sum(a) / len(a)
        return 0

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
