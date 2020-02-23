# https://leetcode.com/problems/number-of-days-between-two-dates/
# lazy solution from builtin
# Runtime: 32 ms, faster than 100.00% of Python3 online submissions for Number of Days Between Two Dates.
# Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Number of Days Between Two Dates.
from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_fmt = '%Y-%m-%d'
        d1 = datetime.strptime(date1, date_fmt).date()
        d2 = datetime.strptime(date2, date_fmt).date()
        dt = d1 - d2
        return abs(dt.days)
