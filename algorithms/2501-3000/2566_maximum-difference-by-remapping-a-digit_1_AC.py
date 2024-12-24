# easy
# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/
class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        n = len(s)

        min_s = None
        for i in range(n):
            if s[i] != '0':
                min_s = s.replace(s[i], '0')
                break
        if min_s is None:
            min_s = s

        max_s = None
        for i in range(n):
            if s[i] != '9':
                max_s = s.replace(s[i], '9')
                break
        if max_s is None:
            max_s = s

        return int(max_s) - int(min_s)
