# https://leetcode.com/problems/my-calendar-iii/
# that's smart

from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        self.mm = SortedDict()

    def book(self, startTime: int, endTime: int) -> int:
        self.mm[startTime] = self.mm.get(startTime, 0) + 1
        self.mm[endTime] = self.mm.get(endTime, 0) - 1
        res = 0
        cur = 0
        for x in self.mm:
            cur += self.mm[x]
            res = max(res, cur)

        return res


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(startTime,endTime)