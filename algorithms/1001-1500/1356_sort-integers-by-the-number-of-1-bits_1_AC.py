# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def countOne(x):
            cnt = 0
            while x != 0:
                x = (x & x - 1)
                cnt += 1
            return cnt

        ap = list(map(lambda x: (countOne(x), x), arr))
        # tuples sort by each key, one after another
        ap.sort()
        res = list(map(lambda x: x[1], ap))
        return res
