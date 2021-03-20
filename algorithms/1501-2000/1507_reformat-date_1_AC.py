# https://leetcode.com/problems/reformat-date/
# 1AC, string manipulation
import re

class Solution:
    def reformatDate(self, date: str) -> str:
        months = [
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec',
        ]
        md = dict(zip(months, list(range(1, 13))))

        tk = date.split()
        yy = int(tk[2])
        mm = md[tk[1]]
        dd = int(re.search('^\d+', tk[0]).group(0))
        return '{:4d}-{:02d}-{:02d}'.format(yy, mm, dd)
