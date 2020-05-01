# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/531/week-4/3313/
# 1AC
from collections import deque

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.uq = deque()
        self.mm = {}
        for x in nums:
            self.add(x)

    def showFirstUnique(self) -> int:
        mm = self.mm
        uq = self.uq

        while len(uq) > 0 and mm[uq[0]] > 1:
            uq.popleft()
        if len(self.uq) == 0:
            return -1
        return uq[0]

    def add(self, value: int) -> None:
        mm = self.mm
        uq = self.uq

        if not value in mm:
            mm[value] = 1
            uq.append(value)
        else:
            mm[value] += 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
