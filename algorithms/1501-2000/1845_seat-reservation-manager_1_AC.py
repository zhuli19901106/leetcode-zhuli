# https://leetcode.com/problems/seat-reservation-manager/
from sortedcontainers import SortedSet

class SeatManager:

    def __init__(self, n: int):
        self.n = n
        self.st_reserved = set()
        self.st_free = SortedSet()
        for i in range(1, n + 1):
            self.st_free.add(i)

    def reserve(self) -> int:
        if len(self.st_free) == 0:
            return None
        x = self.st_free[0]
        self.st_free.remove(x)
        self.st_reserved.add(x)

        return x

    def unreserve(self, seatNumber: int) -> None:
        x = seatNumber
        if not x in self.st_reserved:
            return
        self.st_reserved.remove(x)
        self.st_free.add(x)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)