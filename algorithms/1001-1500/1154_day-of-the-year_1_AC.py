# easy
# https://leetcode.com/problems/day-of-the-year/
import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        dt = datetime.datetime.strptime(date, '%Y-%m-%d')
        dd = dt.date()
        d0 = datetime.date(dd.year, 1, 1)
        delta = dd - d0
        return delta.days + 1
