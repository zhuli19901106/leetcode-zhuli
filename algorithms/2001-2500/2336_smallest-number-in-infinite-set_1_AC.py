# https://leetcode.com/problems/smallest-number-in-infinite-set/
# clean
from heapq import heappush, heappop

class SmallestInfiniteSet:

    def __init__(self):
        self.up = 1
        self.st = set()
        self.pq = []

    def popSmallest(self) -> int:
        res = -1
        if len(self.st) == 0:
            res = self.up
            self.up += 1
            return res

        res = heappop(self.pq)
        self.st.remove(res)

        return res

    def addBack(self, num: int) -> None:
        if num >= self.up:
            return
        if num == self.up - 1:
            self.up -= 1
            return

        if num in self.st:
            return
        self.st.add(num)
        heappush(self.pq, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)