# https://leetcode.com/problems/day-of-the-week/
from datetime import date
from calendar import day_name

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        dt = date(year, month, day)
        wd = dt.weekday()
        return day_name[wd]
